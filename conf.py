import serial
import sys
import time
import platform

READ_TIMEOUT = 8

# Funksjon for plattformuavhengig portvalg
def get_serial_port():
    if platform.system() == "Windows":
        return 'COM' + input('\nEnter Port Number (1,2,3...) -> ')
    else:
        return '/dev/tty' + input('\nEnter Port Name (USB0, S0...) -> ').upper()

# Funksjon for trygg skriving til konsollen
def send_commands(console, commands, delay=1):
    for cmd in commands:
        console.write(f"{cmd}\r\n".encode())
        time.sleep(delay)

# Hovedfunksjon
def main():
    SerialPortName = get_serial_port()

    try:
        console = serial.Serial(
            port=SerialPortName,
            baudrate=9600,
            parity="N",
            stopbits=1,
            bytesize=8,
            timeout=READ_TIMEOUT
        )
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        sys.exit(1)

    device = input("\nRouter = R | Switch = S -> ").upper()

    if device not in ["R", "S"]:
        print("Invalid choice! Choose 'R' or 'S'.")
        sys.exit(1)

    commands = ["en", "conf t"]

    hostName = input("\nEnter desired hostname -> ")
    commands.append(f"hostname {hostName}")

    if device == "R":
        mgmtPort = input("\nEnter management interface (ex: GigabitEthernet0/0) -> ")
        ipAddress = input("\nEnter IP address and subnet (ex: 192.168.1.1 255.255.255.0) -> ")
        sshUser = input("\nEnter SSH username -> ")
        sshSecret = input("\nEnter SSH password -> ")
        enableSecret = input("\nEnter enable secret -> ")

        commands += [
            f"interface {mgmtPort}",
            f"ip address {ipAddress}",
            "no shutdown",
            "exit",
            "ip domain name mynetwork.local",
            "crypto key generate rsa modulus 1024",
            f"username {sshUser} privilege 15 secret {sshSecret}",
            "line vty 0 15",
            "transport input ssh",
            "login local",
            "exec-timeout 60 0",
            "exit",
            f"enable secret {enableSecret}",
            "exit"
        ]

    elif device == "S":
        mgmtPort = input("\nEnter port for configuration (ex: GigabitEthernet0/1) -> ")
        mgmtVlan = input("\nEnter management VLAN -> ")
        ipAddress = input("\nEnter IP address and subnet (ex: 192.168.1.2 255.255.255.0) -> ")
        switchPortMode = input("\nSwitchport mode (access/trunk) -> ").lower()

        commands += [
            f"interface vlan{mgmtVlan}",
            f"ip address {ipAddress}",
            "no shutdown",
            "exit",
            "ip default-gateway 10.10.99.11",
            f"vlan {mgmtVlan}",
            "name MGMT",
            "exit",
            f"interface {mgmtPort}"
        ]

        if switchPortMode == "access":
            commands += [
                "switchport mode access",
                f"switchport access vlan {mgmtVlan}",
                "no shutdown",
                "exit"
            ]
        elif switchPortMode == "trunk":
            trunkAllowedVlans = input("\nEnter allowed VLANs (ex: 1,10,20) -> ")
            commands += [
                "switchport mode trunk",
                f"switchport trunk allowed vlan {trunkAllowedVlans}",
                "no shutdown",
                "exit"
            ]
        else:
            print("Invalid switchport mode!")
            sys.exit(1)

        sshUser = input("\nEnter SSH username -> ")
        sshSecret = input("\nEnter SSH password -> ")
        enableSecret = input("\nEnter enable secret -> ")

        commands += [
            "ip domain name mynetwork.local",
            "crypto key generate rsa modulus 1024",
            f"username {sshUser} privilege 15 secret {sshSecret}",
            "line vty 0 15",
            "transport input ssh",
            "login local",
            "exec-timeout 60 0",
            "exit",
            f"enable secret {enableSecret}",
            "exit"
        ]

    # Sender kommandoer
    send_commands(console, commands)

    # Leser og skriver ut svar fra konsollen
    time.sleep(2)
    while console.in_waiting:
        output = console.read(console.in_waiting).decode('utf-8', 'ignore')
        print(output)

    # Lukker konsollen etter bruk
    console.close()

if __name__ == "__main__":
    main()


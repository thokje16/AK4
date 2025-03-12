import serial
import sys
import time

READ_TIMEOUT = 8
SerialPortName = input('\nEnter Port Name ->')
SerialPortName = '/dev/tty' + SerialPortName






def main():
        device = input("\nRouter = R Switch = S")
        console = serial.Serial(
                port=SerialPortName,
                baudrate=9600,
                parity="N",
                stopbits=1,
                bytesize=8,
                timeout=READ_TIMEOUT
        )



        if not console.isOpen():
                sys.exit()
        if device == "R":
                hostName = input("\nEnter desired hostname -> ")
                hostName = "hostname " + hostName + "\r\n"
                mgmtPort = input("\nEnter desired port -> ")
                mgmtPort = "int " + mgmtPort + "\r\n"
                ipAddress = input("\nEnter ip add and subnet example(1.1.1.1 255.255.255.255 -> ")
                ipAddress = "ip address " + ipAddress + "\r\n"
                sshSecret = input("\nEnter ssh password -> ")
                sshUser = input("\nEnter Username -> ")
                sshUS = "username " + sshUser + " privilege 15 secret " + sshSecret + "\r\n"
                enableSecret = input("\nEnter enable secret -> ")
                enableSecret = "enable secret " + enableSecret + "\r\n"
                console.write("exit\r\n".encode())
                time.sleep(1)
                #console.write("exit\r\n".encode())
                #time.sleep(1)
                console.write("\r\n\r\n".encode())
                time.sleep(1)
                print ('\nStatus -> ',console)
                console.write("en\r\n".encode())
                console.write("conf t\r\n".encode())
                console.write(hostName.encode())
                console.write(mgmtPort.encode())
                console.write(ipAddress.encode())
                console.write("no shutdown\r\n".encode())
                console.write("exit\r\n".encode())
                console.write("ip domain name mynetwork.local\r\n".encode())
                console.write("crypto key generate rsa modulus 1024\r\n".encode())
                console.write(sshUS.encode())
                console.write("line vty 0 15\r\n".encode())
                console.write("transport input ssh\r\n".encode())
                console.write("login local\r\n".encode())
                console.write("exec-timeout 60 0\r\n".encode())
                console.write("exit\r\n".encode())
                console.write(enableSecret.encode())
                console.write("exit\r\n".encode())
                console.write("exit\r\n".encode())
                input_data = console.read(console.inWaiting())
                print(input_data)
                time.sleep(3)
                #console.close()
        elif device == "S":
                level = input("\nFull conf? [yes]/[no]")
                if level == "yes":
                        hostName = input("\nEnter desired hostname -> ")
                        hostName = "hostname " + hostName + "\r\n"
                        mgmtPort = input("\nEnter desired port -> ")
                        mgmtPort = "int " + mgmtPort + "\r\n"
                        switchPortMode = input("\nEnter trunk or access ->")
                        switchPortMode = "switchport mode " + switchPortMode + "\r\n"
                        #ipAddress = input("\nEnter ip add and subnet example(1.1.1.1 255.255.255.255 -> ")
                        #ipAddress = "ip address " + ipAddress + "\r\n"
                        sshSecret = input("\nEnter ssh password -> ")
                        sshUser = input("\nEnter Username -> ")
                        sshUS = "username " + sshUser + " privilege 15 secret " + sshSecret + "\r\n"
                        enableSecret = input("\nEnter enable secret -> ")
                        enableSecret = "enable secret " + enableSecret + "\r\n"
                        console.write("exit\r\n".encode())
                        time.sleep(1)
                        #console.write("exit\r\n".encode())
                        #time.sleep(1)
                        console.write("\r\n\r\n".encode())
                        time.sleep(1)
                        print ('\nStatus -> ',console)
                        console.write("en\r\n".encode())
                        console.write("conf t\r\n".encode())
                        console.write(hostName.encode())
                        console.write(mgmtPort.encode())
                        console.write(switchPortMode.encode())
                        console.write("no shutdown\r\n".encode())
                        console.write("exit\r\n".encode())
                        console.write("ip domain name mynetwork.local\r\n".encode())
                        console.write("crypto key generate rsa modulus 1024\r\n".encode())
                        console.write(sshUS.encode())
                        console.write("line vty 0 15\r\n".encode())
                        console.write("transport input ssh\r\n".encode())
                        console.write("login local\r\n".encode())
                        console.write("exec-timeout 60 0\r\n".encode())
                        console.write("exit\r\n".encode())
                        console.write(enableSecret.encode())
                        console.write("exit\r\n".encode())
                        console.write("exit\r\n".encode())
                        input_data = console.read(console.inWaiting())
                        print(input_data)
                        time.sleep(3)
                        #console.close()
                elif level == "no":
                        mgmtPort = input("\nEnter desired port -> ")
                        mgmtPort = "int " + mgmtPort + "\r\n"
                        switchPortMode = input("\nEnter trunk or access ->")
                        switchPortMode = "switchport mode " + switchPortMode + "\r\n"
                        console.write("en\r\n".encode())
                        console.write("cisco\n\r".encode())
                        console.write("conf t\r\n".encode())
                        #console.write(hostName.encode())
                        console.write(mgmtPort.encode())
                        console.write(switchPortMode.encode())
                        console.write("no shutdown\r\n".encode())
                        console.write("exit\r\n".encode())
        else:
                print("\nR OR S IDIOT")
if __name__ == "__main__":
        main()


import serial
import sys
import time

READ_TIMEOUT = 8
SerialPortName = input('\nEnter Port Name ->')
SerialPortName = '/dev/tty' + SerialPortName.upper()






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
                        mgmtConf = input("\nEnter MGMT vlan -> ")
                        mgmtConf2 = "int vlan" + mgmtConf + "\r\n"
                        addVlanData = "vlan " + mgmtConf + "\r\n"
                        switchPortMode = input("\nEnter trunk or access ->")

                        switchPortMode2 = "switchport mode " + switchPortMode + "\r\n"
                        switchPortModeAcc = "switchport mode access vlan " + mgmtConf + "\r\n"
                        switchPortModeTrunk = "switchport mode trunk vlan " + "\r\n"
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
                        console.write(mgmtConf2.encode())
                        console.write(ipAddress.encode())
                        console.write("no shutdown\r\n".encode())
                        console.write("exit\r\n".encode())
                        console.write(addVlanData.encode())
                        console.write(mgmtPort.encode())
                        if switchPortMode == "access":
                                console.write(switchPortModeAcc.encode())
                                console.write("no shutdown\r\n".encode())
                                console.write("exit\r\n".encode())
                        elif switchPortMode == "trunk":
                                modeVlan = input("\nConfigure vlan on port? [yes]/[no] ")
                                if modeVlan == "no":
                                        console.write(switchPortMode2.encode())
                                        console.write("no shutdown\r\n".encode())
                                        console.write("exit\r\n".encode())
                                        console.write(addVlanData.encode())
                                        console.write("name MGMT\r\n".encode())
                                        console.write("exit\r\n".encode())
                                elif modeVlan == "yes":
                                        console.write(switchPortModeTrunk.encode())
                                        console.write("no shutdown\r\n".encode())
                                        console.write("exit\r\n".encode())
                                        console.write(addVlanData.encode())
                                        console.write("name MGMT\r\n".encode())
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
                        switchPortMode2 = "switchport mode " + switchPortMode + "\r\n"
#                       switchPortModeAcc = "switchport mode access vlan " + mgmtConf + "\r\n"
#                       switchPortModeTrunk = "switchport mode trunk vlan " + mgmtConf + "\r\n"
#                       addVlanData = "vlan " + mgmtConf + "\r\n"
                        console.write("en\n\r".encode())
                        console.write("cisco\n\r".encode())
                        console.write("conf t\r\n".encode())
                        if switchPortMode == "access":
                                ipAddress = input("\nEnter ip add and subnet example(1.1.1.1 255.255.255.255 -> ")
                                ipAddress = "ip address " + ipAddress + "\r\n"
                                mgmtConf = input("\nEnter MGMT vlan -> ")
                                mgmtConf2 = "int vlan" + mgmtConf + "\r\n"
                                addVlanData = "vlan " + mgmtConf + "\r\n"
                                modeVlan = input("\nConfigure vlan on port? [yes]/[no] ")
                                switchPortModeAcc = "switchport mode access vlan " + mgmtConf + "\r\n"
                                console.write(switchPortModeAcc.encode())
                                console.write("no shutdown\r\n".encode())
                                console.write("exit\r\n".encode())
                                console.write(addVlanData.encode())
                        elif switchPortMode == "trunk":
                                modeVlan = input("\nConfigure vlan on port? [yes]/[no] ")
                                if modeVlan == "no":
                                        switchPortMode2 = "switchport mode " + switchPortMode + "\r\n"
                                        console.write("en\r\n".encode())
                                elif modeVlan == "yes":
                                        ipAddress = input("\nEnter ip add and subnet example(1.1.1.1 255.255.255.255 -> ")
                                        mgmtConf = input("\nEnter MGMT vlan -> ")
                                        mgmtConf2 = "int vlan" + mgmtConf + "\r\n"
                                        addVlanData = "vlan " + mgmtConf + "\r\n"
                                        ipAddress = "ip address " + ipAddress + "\r\n"
                                        switchPortModeTrunk = "switchport mode trunk\r\n"
                                        console.write("exit\r\n".encode())
                                        console.write(mgmtPort.encode())
                                        console.write(switchPortModeTrunk.encode())
                                        console.write("no shutdown\r\n".encode())
                                        console.write("exit\r\n".encode())
                                        console.write(addVlanData.encode())
                                        console.write("name MGMT\r\n".encode())
                                        console.write("exit\r\n".encode())
                        #console.write(hostName.encode())
                        console.write(mgmtPort.encode())
                        console.write(switchPortMode.encode())
                        console.write("no shutdown\r\n".encode())
                        console.write("exit\r\n".encode())
        else:
                print("\nR OR S IDIOT")
if __name__ == "__main__":
        main()













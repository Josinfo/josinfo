from netmiko import ConnectHandler

import getpass


#ipv4 = (input("Qual IP do Device:? "))
user = (input("Digite seu Usuario:? "))
pswd = getpass.getpass() 
ip_address = open("Devices.txt","r")


#First create the device object using a dictionary
for i in ip_address.readlines():
    print(i)
    LEGADO = {
        'device_type': 'cisco_nxos',
        'ip': i,
        'username': user,
        'password': pswd
    }
 
    #  Next establish the SSH connection
    
    net_connect = ConnectHandler(**LEGADO)
    
    filename = i.replace('\n','')
    with open(f"{filename}.txt", "a") as file:
        # Then send the command and print the output
        file.write("\n SHOW VERSION \n")
        file.write(net_connect.send_command('show version'))
        file.write("\n SHOW RUNNING-CONFIG \n")
        file.write(net_connect.send_command('show running-config'))
        file.write("\n SHOW IP ROUTE \n")
        file.write(net_connect.send_command('show ip route'))
        
ip_address.close()
# Finally close the connection
net_connect.disconnect()
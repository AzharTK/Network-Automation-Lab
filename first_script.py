from netmiko import ConnectHandler 
router = { 
"device_type": "cisco_ios", 
"host": "192.168.227.131", 
"username": "azhar", 
"password": "azhar", 
"secret": "cisco123", 
"global_delay_factor": 2, 
} 
net_connect = ConnectHandler(**router) 
net_connect.enable() 
output = net_connect.send_command("show ip int brief") 
print(output) 
net_connect.disconnect()


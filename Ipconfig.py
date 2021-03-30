# open cmd and convert the text into strings.
import subprocess
process = subprocess.check_output("ipconfig" ).decode('utf-8')
text = str(process)

# here you substract the ipv6 address from the text.
device_ipv6 = text.index("IPv6 Address") +36 
temporary = text.index("Temporary")
ipv6_address = text[device_ipv6:temporary]
print("Your device's IPv6 address:", ipv6_address)

# here you substract the ipv4 address from the text.
device_ip = text.index("IPv4 Address") +36 
subnet_mask = text.index("Subnet Mask")
ip_address = text[device_ip:subnet_mask]
print("Your device's IPv4 address:", ip_address)

# here you substract the subnet mask from the text.
subnet_mask = text.index("Subnet Mask") +36
default_gate = text.index("Default Gateway")
subnet = text[subnet_mask:default_gate]
print("Your internet's Subnet Mask:", subnet)

# here you substract the gateway from the text.
default_gate = text.index("Default Gateway") +104
end = text.index("Ethernet adapter VMware Network Adapter VMnet1:")
gateway = text[default_gate:end]
print("Your internet's Gateway:", gateway)

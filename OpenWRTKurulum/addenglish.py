import sys
import telnetlib
import subprocess
import ftplib

line4 = subprocess.check_output(["cmd","/c","chcp","437","&","tracert","-d","-h","1","1.1.1.1"]).decode().split("\r\n")[4].strip().split(" ")

for data in line4:
	if len(data.split(".")) == 4:
		router_ip_address = data
		break
		
try:	
	ftp=ftplib.FTP(router_ip_address)
except:
	print ("ftp server not found")
	sys.exit(1)
try:	
	file1=open('data/base.en.lmo', 'rb')
except:
	print ("lmo not found")
	sys.exit(1)
try:	
	file2=open('data/english.sh', 'rb')
except:
	print ("script not found")
	sys.exit(1)
ftp.storbinary(f'STOR /tmp/base.en.lmo', file1)
ftp.storbinary(f'STOR /tmp/english.sh', file2)
file1.close()
file2.close()
ftp.quit()
print ("Upload done")

tn = telnetlib.Telnet(router_ip_address)
tn.read_until(b"login:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Patching....")
tn.write(b"sh /tmp/english.sh\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"exit\n")
print ("Done")
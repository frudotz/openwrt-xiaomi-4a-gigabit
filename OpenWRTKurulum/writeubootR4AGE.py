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
	file=open('data/ubootR4AGE.bin', 'rb')
except:
	print ("ubootR4AGE.bin not found")
	sys.exit(1)
print ("Uploading ubootR4AGE.bin ...")
ftp.storbinary(f'STOR /tmp/ubootR4AGE.bin', file)
file.close()
ftp.quit()
print ("Upload done")

tn = telnetlib.Telnet(router_ip_address)
tn.read_until(b"login:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Writing Bootloader...")
tn.write(b"mtd -e Bootloader write /tmp/ubootR4AGE.bin Bootloader\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"exit\n")
print ("Done")

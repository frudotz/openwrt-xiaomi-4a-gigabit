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
	file1=open('data/backup.bin', 'rb')
except:
	print ("backup.bin not found")
	sys.exit(1)
try:	
	file2=open('data/flashall.sh', 'rb')
except:
	print ("flash script not found")
	sys.exit(1)
print ("Uploading data ...")
ftp.storbinary(f'STOR /tmp/backup.bin', file1)
ftp.storbinary(f'STOR /tmp/flashall.sh', file2)
file1.close()
file2.close()
ftp.quit()
print ("Upload done")

tn = telnetlib.Telnet(router_ip_address)
tn.read_until(b"login:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"sh /tmp/flashall.sh >/dev/null 2>&1 &\n")
tn.read_until(b"root@XiaoQiang:~#",10)
print ("Router just started overwriting flash memory.")
print ("Do not switch off the router.")
print ("Router will automatically reboot.")
print ("The current window can be closed.")



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
	tn = telnetlib.Telnet(router_ip_address)
except:
	print ("telnet server not found")
	sys.exit(1)
tn.read_until(b"login:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Creating backup")
tn.write(b"dd if=/dev/mtd0 of=/tmp/backup.bin\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"exit\n")
print ("Done")

ftp=ftplib.FTP(router_ip_address)
file=open('data/backup.bin', 'wb')
print ("Downloading backup")
ftp.retrbinary(f'RETR /tmp/backup.bin', file.write)
file.close()
ftp.quit()
print ("Done")

tn = telnetlib.Telnet(router_ip_address)
tn.read_until(b"login:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
print ("Removing tmp")
tn.write(b"rm /tmp/backup.bin\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"exit\n")
print ("Done")

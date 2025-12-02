# Cybersecurity Learning Roadmap

## Phase 1: Foundations (4-8 weeks)

### Computer Fundamentals
- How computers work (CPU, memory, storage)
- Operating systems basics (Linux, Windows)
- File systems and permissions
- Processes and services

### Networking Fundamentals
- OSI and TCP/IP models
- IP addressing and subnetting (IPv4/IPv6)
- DNS, DHCP, ARP protocols
- Common ports and services (HTTP/80, HTTPS/443, SSH/22, FTP/21)
- Routing and switching basics
- Firewalls and NAT
- Wireshark for packet analysis

### Linux Essentials
- Command line navigation
- File manipulation (cp, mv, rm, chmod, chown)
- User and group management
- Package management (apt, yum, pacman)
- System logs (/var/log/)
- Cron jobs and systemd
- SSH and remote access

### Programming Basics
- Python for security (scripting, automation)
- Bash scripting
- Basic understanding of C/C++ (memory management)
- Understanding compiled vs interpreted languages

### Web Technologies
- HTML, CSS, JavaScript basics
- HTTP/HTTPS protocols
- Request/response cycle
- Cookies and sessions
- Same-origin policy
- REST APIs

## Phase 2: Security Fundamentals (6-8 weeks)

### Core Security Concepts
- CIA Triad (Confidentiality, Integrity, Availability)
- Authentication vs Authorization
- Principle of least privilege
- Defense in depth
- Zero trust architecture
- Security by design

### Cryptography
- Symmetric encryption (AES, DES, 3DES)
- Asymmetric encryption (RSA, ECC)
- Hashing algorithms (MD5, SHA-1, SHA-256, bcrypt)
- Digital signatures and certificates
- PKI (Public Key Infrastructure)
- SSL/TLS protocols
- Key management
- Encryption vs encoding vs hashing

### Identity & Access Management
- Authentication methods (passwords, MFA, biometrics)
- SSO (Single Sign-On)
- OAuth 2.0 and OpenID Connect
- LDAP and Active Directory
- RBAC (Role-Based Access Control)
- PAM (Privileged Access Management)

### Security Tools & Practices
- Antivirus and endpoint protection
- SIEM basics
- IDS/IPS (Snort, Suricata)
- VPNs and secure tunneling
- Password managers
- Secure configuration management

## Phase 3: Offensive Security (8-12 weeks)

### Reconnaissance
- Passive reconnaissance (OSINT)
- Active reconnaissance
- Google dorking
- Subdomain enumeration
- DNS enumeration (dig, nslookup, host)
- Tools: Maltego, theHarvester, Recon-ng, Shodan

### Scanning & Enumeration
- Port scanning (Nmap, Masscan)
- Service enumeration
- Banner grabbing
- Vulnerability scanning (Nessus, OpenVAS, Nikto)
- SMB enumeration
- SNMP enumeration

### Web Application Security
**Common Vulnerabilities:**
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Authentication flaws
- Broken access control
- Security misconfigurations
- XML External Entity (XXE)
- Server-Side Request Forgery (SSRF)
- Insecure deserialization
- Command injection

**Tools:**
- Burp Suite
- OWASP ZAP
- sqlmap
- Nikto
- WPScan (WordPress)

### Network Exploitation
- Man-in-the-Middle (MITM) attacks
- ARP spoofing
- DNS spoofing
- Session hijacking
- Network sniffing
- Tools: Ettercap, Bettercap, Responder

### System Exploitation
- Buffer overflows
- Privilege escalation (Linux/Windows)
- Exploit development basics
- Metasploit framework
- Reverse shells and bind shells
- Payload generation (msfvenom)
- Common exploits (EternalBlue, Shellshock)

### Wireless Security
- WEP/WPA/WPA2/WPA3 protocols
- Wireless attack types
- Rogue access points
- Evil twin attacks
- Tools: Aircrack-ng, Wireshark, Reaver

### Password Attacks
- Brute force attacks
- Dictionary attacks
- Rainbow tables
- Hash cracking
- Password spraying
- Tools: Hashcat, John the Ripper, Hydra, Medusa

### Social Engineering
- Phishing techniques
- Pretexting
- Baiting
- Tailgating
- Vishing and smishing
- Tools: SET (Social Engineering Toolkit), Gophish

## Phase 4: Defensive Security (8-12 weeks)

### Security Operations
- Security monitoring
- Log analysis and correlation
- Incident detection
- Alert triage
- SOC (Security Operations Center) workflows
- Threat hunting

### Incident Response
- Incident response lifecycle (NIST, SANS)
- Detection and analysis
- Containment strategies
- Eradication and recovery
- Post-incident analysis
- Digital forensics basics
- Chain of custody
- Tools: Volatility, Autopsy, FTK

### Digital Forensics
- Disk imaging and analysis
- Memory forensics
- Network forensics
- File system forensics
- Timeline analysis
- Artifact recovery
- Tools: Sleuth Kit, EnCase, Wireshark

### Malware Analysis
- Static analysis
- Dynamic analysis
- Behavioral analysis
- Reverse engineering basics
- Indicators of Compromise (IoC)
- Malware families and types
- Tools: IDA Pro, Ghidra, Cuckoo Sandbox, VirusTotal

### Threat Intelligence
- Threat modeling
- MITRE ATT&CK framework
- Indicators of Compromise (IoCs)
- Threat feeds and sharing
- Cyber kill chain
- Diamond Model
- Tools: MISP, OpenCTI, ThreatConnect

### Hardening & Configuration
- System hardening (Linux/Windows)
- CIS benchmarks
- Patch management
- Baseline security configurations
- Secure coding practices
- Configuration management tools

### Network Security
- Firewall configuration (iptables, pf, Windows Firewall)
- Network segmentation
- DMZ architecture
- VLANs and network isolation
- IDS/IPS deployment and tuning
- Network Access Control (NAC)

## Phase 5: Specialized Domains

### Cloud Security
**Platforms:**
- AWS security services
- Azure security features
- Google Cloud security

**Concepts:**
- Cloud security posture management (CSPM)
- Container security (Docker, Kubernetes)
- Serverless security
- IAM in cloud environments
- Cloud compliance and governance
- S3 bucket security
- API security

### Application Security (AppSec)
- Secure SDLC
- Code review and static analysis (SAST)
- Dynamic application security testing (DAST)
- Dependency scanning
- Security testing integration (DevSecOps)
- Threat modeling
- Tools: SonarQube, Snyk, Checkmarx, Fortify

### Mobile Security
- Android security
- iOS security
- Mobile app pentesting
- Reverse engineering mobile apps
- Tools: MobSF, Frida, Objection, APKTool

### IoT Security
- IoT protocols (MQTT, CoAP, Zigbee)
- Firmware analysis
- Hardware hacking basics
- Embedded device security
- Tools: Binwalk, Firmwalker

### Red Teaming
- Advanced persistent threats (APT) simulation
- C2 (Command and Control) frameworks
- Evasion techniques
- Living off the land (LoL)
- Advanced exploitation
- Tools: Cobalt Strike, Empire, Covenant

### Purple Teaming
- Combining offensive and defensive techniques
- Collaborative security testing
- Gap analysis
- Security control validation

## Phase 6: Compliance & Governance

### Security Frameworks & Standards
- NIST Cybersecurity Framework
- ISO 27001/27002
- CIS Controls
- COBIT
- PCI DSS (Payment Card Industry)
- HIPAA (Healthcare)
- GDPR (Privacy)
- SOC 2

### Risk Management
- Risk assessment methodologies
- Vulnerability management
- Business impact analysis
- Risk treatment strategies
- Security metrics and KPIs

### Security Policies
- Information security policy
- Acceptable use policy
- Incident response policy
- Business continuity and disaster recovery
- Data classification policies

## Certifications Roadmap

### Entry Level
- CompTIA Security+ (foundational)
- CompTIA Network+
- CompTIA A+
- Certified in Cybersecurity (CC) - ISC2

### Intermediate
- CEH (Certified Ethical Hacker)
- GIAC Security Essentials (GSEC)
- CompTIA CySA+ (Cybersecurity Analyst)
- SSCP (Systems Security Certified Practitioner)

### Advanced - Offensive
- OSCP (Offensive Security Certified Professional)
- GPEN (GIAC Penetration Tester)
- GXPN (GIAC Exploit Researcher and Advanced Penetration Tester)
- OSEP (Offensive Security Experienced Penetration Tester)
- OSWE (Offensive Security Web Expert)

### Advanced - Defensive
- GCIH (GIAC Certified Incident Handler)
- GCFA (GIAC Certified Forensic Analyst)
- GCIA (GIAC Certified Intrusion Analyst)
- CISSP (Certified Information Systems Security Professional)

### Specialized
- CCSP (Certified Cloud Security Professional)
- CISM (Certified Information Security Manager)
- CISA (Certified Information Systems Auditor)
- AWS Certified Security - Specialty
- Azure Security Engineer Associate

## Practice Labs & Platforms

### Beginner Friendly
- TryHackMe (guided learning paths)
- PicoCTF
- OverTheWire (wargames)
- Cybrary

### Intermediate
- HackTheBox
- VulnHub
- PentesterLab
- Root-Me

### Advanced
- HackTheBox Pro Labs
- Offensive Security Proving Grounds
- SANS NetWars
- ImmersiveLabs

### CTF Competitions
- CTFtime.org (competition listings)
- Google CTF
- DEFCON CTF
- picoCTF

### Web Application
- DVWA (Damn Vulnerable Web Application)
- WebGoat
- bWAPP
- Juice Shop
- PortSwigger Web Security Academy

### Vulnerable VMs
- Metasploitable 2/3
- OWASP Broken Web Apps
- Kioptrix series
- VulnHub machines

## Essential Tools by Category

### Reconnaissance
- Nmap, Masscan
- theHarvester
- Maltego
- Recon-ng
- Shodan, Censys
- Amass, Subfinder

### Web Application Testing
- Burp Suite
- OWASP ZAP
- Nikto
- sqlmap
- Gobuster, Dirbuster
- Wfuzz, ffuf

### Exploitation
- Metasploit Framework
- Exploit-DB
- SearchSploit
- msfvenom

### Post-Exploitation
- Mimikatz
- BloodHound
- PowerSploit
- LinPEAS, WinPEAS
- Empire, Covenant

### Networking
- Wireshark, tcpdump
- Ncat, Netcat
- Ettercap, Bettercap
- Scapy

### Password Cracking
- Hashcat
- John the Ripper
- Hydra
- Medusa
- CeWL (wordlist generator)

### Forensics
- Autopsy
- Volatility
- Sleuth Kit
- Foremost
- Binwalk

### Reverse Engineering
- Ghidra
- IDA Pro
- Radare2
- OllyDbg, x64dbg
- Hopper

### Security Monitoring
- Splunk
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Graylog
- Wazuh
- Security Onion

## Career Paths

### Security Analyst (SOC Analyst)
- Monitor security events
- Analyze alerts and logs
- Incident response
- Threat hunting

### Penetration Tester
- Ethical hacking
- Vulnerability assessment
- Exploitation and reporting
- Client engagement

### Security Engineer
- Design security architectures
- Implement security controls
- Automate security processes
- Tool development and integration

### Incident Responder
- Respond to security incidents
- Forensic analysis
- Malware investigation
- Recovery and remediation

### Security Researcher
- Vulnerability research
- Exploit development
- Security tool development
- Bug bounty hunting

### Security Architect
- Design enterprise security
- Security strategy and roadmap
- Compliance and governance
- Risk management

### Security Consultant
- Security assessments
- Advisory services
- Policy development
- Client training

### Malware Analyst
- Reverse engineering
- Behavioral analysis
- Threat intelligence
- IoC development

## Learning Resources

### Books
- "The Web Application Hacker's Handbook" - Dafydd Stuttard
- "Metasploit: The Penetration Tester's Guide"
- "The Art of Exploitation" - Jon Erickson
- "Black Hat Python" - Justin Seitz
- "Practical Malware Analysis" - Michael Sikorski
- "Blue Team Handbook" - Don Murdoch
- "RTFM: Red Team Field Manual"
- "BTFM: Blue Team Field Manual"

### Online Courses
- Cybrary
- INE Security
- Offensive Security training
- SANS courses
- Udemy (cybersecurity courses)
- Coursera (cybersecurity specializations)

### YouTube Channels
- IppSec (HackTheBox walkthroughs)
- John Hammond
- NetworkChuck
- LiveOverflow
- HackerSploit
- The Cyber Mentor

### Websites & Blogs
- OWASP
- Krebs on Security
- Schneier on Security
- Darknet Diaries (podcast)
- Null Byte
- Hack The Box blog

### Communities
- Reddit: r/netsec, r/cybersecurity, r/AskNetsec
- Discord servers (HackTheBox, TryHackMe)
- Twitter #infosec community
- DEF CON forums
- Security Stack Exchange

## Daily Practice Routine

1. **Read security news** (15-30 min)
   - BleepingComputer, The Hacker News
   - Security subreddits
   - CVE announcements

2. **Practice skills** (1-2 hours)
   - Complete CTF challenges
   - Work on vulnerable VMs
   - Build lab environments

3. **Study and research** (30-60 min)
   - Read documentation
   - Watch tutorials
   - Study for certifications

4. **Build and document** (ongoing)
   - Create security tools
   - Write blog posts
   - Document your learning

5. **Engage with community**
   - Participate in forums
   - Share knowledge
   - Attend meetups/conferences

## Home Lab Setup

### Essential Components
- Virtualization (VirtualBox, VMware, Proxmox)
- Kali Linux (attacking machine)
- Vulnerable VMs (targets)
- Windows Server (Active Directory)
- Security Onion (monitoring)
- pfSense (firewall/router)

### Lab Scenarios
- Active Directory pentesting
- Web application testing
- Network exploitation
- Malware analysis sandbox
- Incident response simulation
- Blue team detection lab

## Milestones

- [ ] Complete basic networking course
- [ ] Set up home security lab
- [ ] Root your first HackTheBox machine
- [ ] Complete OWASP Top 10 challenges
- [ ] Earn Security+ certification
- [ ] Complete 20 CTF challenges
- [ ] Write a security blog post
- [ ] Contribute to open source security tool
- [ ] Earn OSCP or equivalent
- [ ] Land first cybersecurity job
- [ ] Participate in bug bounty program
- [ ] Present at security conference/meetup

## Important Notes

### Ethics & Legality
- **NEVER** attack systems without permission
- Always get written authorization for pentests
- Understand local computer crime laws
- Respect responsible disclosure practices
- Use skills only for defensive purposes or authorized testing

### Continuous Learning
- Cybersecurity is constantly evolving
- New vulnerabilities discovered daily
- Stay updated with latest threats
- Never stop learning and practicing

### Specialization
- Start broad, then specialize
- Find what interests you most
- Depth in one area is valuable
- But maintain broad knowledge

# Resources 
A list of Capture The Flag (CTF) frameworks, libraries, tools, tutorials, and challenges for the WashU Bearshell CTF club. 

##### Symbols:
- (* -> ***) - how difficult a CTF or Resource is
- (#) - tool is preinstalled on Kali (**WIP**)

Note: A lot of this repo was taken from Apsdehal's [Awesome-CTF](https://github.com/apsdehal/awesome-ctf/blob/master/README.md)

-   [OS](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#create)
-   [Tools](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Tools)
	-   [Web](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Web)
	-   [Crypto](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Crypto)
	-   [Bruteforcers](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Bruteforcers)
	-  [Exploits](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Exploits)
	- [Networking](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Networking)
	- [Reversing](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Reversing)
	-   [Forensics](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Forensics)
	-   [Steganography](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Steganography)
- [Tutorials](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Tutorials)
- [Wargames](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Wargames)
- [Websites](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Websites)
- [Readings](https://github.com/wustl-bearshell/bearshell-ctf/tree/master/Resources#Readings)

## OS
We recommend installing Kali Linux because of its extensive library of prebuilt tools. 
- [How to install Kali on Virtual Box](https://itsfoss.com/install-kali-linux-virtualbox/) 

## Tools
### Web
_Tools used for solving Web challenges_
- [Burp Suite](https://portswigger.net/burp) (#) - In-depth tool on web page analysis. Includes proxy server, scanner, intruder tools. 
- [Sqlmap](http://sqlmap.org/) (#) - automatic SQL injection.
- [The Browser Exploitation Framework (BeEF)](http://beefproject.com/) (#) - targets web browsers by hooking and then exploiting.
- [commix](https://github.com/stasinopoulos/commix) - Command injection and exploitation tool for web.
- [dirsearch](https://github.com/maurosoria/dirsearch) - Web path scanner.
- [mitmproxy](https://mitmproxy.org/) - CLI Web proxy and python library.
- [subbrute](https://github.com/TheRook/subbrute) - A DNS meta-query spider that enumerates DNS records, and subdomains.
- [Hackbar](https://addons.mozilla.org/en-US/firefox/addon/hackbartool/)  - Firefox addon for easy web exploitation.
- [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)  - Add on for chrome for debugging network requests.
- [Raccoon](https://github.com/evyatarmeged/Raccoon)  - A high performance offensive security tool for reconnaissance and vulnerability scanning.
-  [W3af](https://github.com/andresriancho/w3af)  - Web Application Attack and Audit Framework.
-  [XSSer](http://xsser.sourceforge.net/)  - Automated XSS testor.
-  [OWASP ZAP](https://www.owasp.org/index.php/Projects/OWASP_Zed_Attack_Proxy_Project)  - Intercepting proxy to replay, debug, and fuzz HTTP requests and responses.

### Crypto
_Tools used for solving Crypto challenges_
-	[Cryptovenom](https://github.com/lockedbyte/cryptovenom) - All-around command line tool for encrypting/decrypting
-   [CyberChef](https://gchq.github.io/CyberChef)  - Web app for analysing and decoding data.
-   [FeatherDuster](https://github.com/nccgroup/featherduster)  - An automated, modular cryptanalysis tool.
-   [Hash Extender](https://github.com/iagox86/hash_extender)  - A utility tool for performing hash length extension attacks.
-   [padding-oracle-attacker](https://github.com/KishanBagaria/padding-oracle-attacker)  - A CLI tool to execute padding oracle attacks.
-   [PkCrack](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html)  - A tool for Breaking PkZip-encryption.
-   [RSACTFTool](https://github.com/Ganapati/RsaCtfTool)  - A tool for recovering RSA private key with various attack.
-   [RSATool](https://github.com/ius/rsatool)  - Generate private key with knowledge of p and q.
-   [XORTool](https://github.com/hellman/xortool)  - A tool to analyze multi-byte xor cipher.
-   [fastcoll](https://www.win.tue.nl/hashclash/) - An md5sum collision generator.
-   [hash-identifier](https://code.google.com/p/hash-identifier/source/checkout) - Simple hash algorithm identifier.
-   [yafu](http://sourceforge.net/projects/yafu/) - Automated integer factorization.
-   [Esolang](https://esolangs.org/wiki/Main_Page) - Esoteric Programming Languages.

### Bruteforcers

_Tools used for various kind of bruteforcing (passwords etc.)_

-   [Hashcat](https://hashcat.net/hashcat/) (#) - Password Cracker
-   [Hydra](https://tools.kali.org/password-attacks/hydra)  - A parallelized login cracker which supports numerous protocols to attack
-   [John The Jumbo](https://github.com/magnumripper/JohnTheRipper)  - Community enhanced version of John the Ripper.
-   [John The Ripper](http://www.openwall.com/john/) (#) - Password Cracker.
-   [Nozzlr](https://github.com/intrd/nozzlr)  - Nozzlr is a bruteforce framework, trully modular and script-friendly.
-   [Ophcrack](http://ophcrack.sourceforge.net/)  - Windows password cracker based on rainbow tables.
-   [Patator](https://github.com/lanjelot/patator)  - Patator is a multi-purpose brute-forcer, with a modular design.
-  [HashDecryption.com](HashDecryption.com) -Web page with some decrypted hashes stored
-   [PDFCrack](http://pdfcrack.sourceforge.net/) - A Password Recovery Tool for PDF-files.

### Exploits

_Tools used for solving Exploits challenges_

-   [DLLInjector](https://github.com/OpenSecurityResearch/dllinjector)  - Inject dlls in processes.
-   [libformatstr](https://github.com/hellman/libformatstr)  - Simplify format string exploitation.
-   [Metasploit](http://www.metasploit.com/) (#) - Penetration testing software.
    -   [Cheatsheet](https://www.comparitech.com/net-admin/metasploit-cheat-sheet/)
-   [one_gadget](https://github.com/david942j/one_gadget)  - A tool to find the one gadget  `execve('/bin/sh', NULL, NULL)`  call.
    -   `gem install one_gadget`
-   [Pwntools](https://github.com/Gallopsled/pwntools)  - CTF Framework for writing exploits.
-   [Qira](https://github.com/BinaryAnalysisPlatform/qira)  - QEMU Interactive Runtime Analyser.
-   [ROP Gadget](https://github.com/JonathanSalwan/ROPgadget)  - Framework for ROP exploitation.
-   [V0lt](https://github.com/P1kachu/v0lt)  - Security CTF Toolkit.


### Networking

_Tools used for solving Networking challenges_

-   [Masscan](https://github.com/robertdavidgraham/masscan)  - Mass IP port scanner, TCP port scanner.
-   [Monit](https://linoxide.com/monitoring-2/monit-linux/)  - A linux tool to check a host on the network (and other non-network activities).
-   [Nipe](https://github.com/GouveaHeitor/nipe)  - Nipe is a script to make Tor Network your default gateway.
-   [Nmap](https://nmap.org/)  - An open source utility for network discovery and security auditing.
-   [Wireshark](https://www.wireshark.org/)  - Analyze the network dumps.
    -   `apt-get install wireshark`
-   [Zeek](https://www.zeek.org/)  - An open-source network security monitor.
-   [Zmap](https://zmap.io/)  - An open-source network scanner.

### Reversing

_Tools used for solving Reversing challenges_

-   [Androguard](https://github.com/androguard/androguard)  - Reverse engineer Android applications.
-   [Angr](https://github.com/angr/angr)  - platform-agnostic binary analysis framework.
-   [Apk2Gold](https://github.com/lxdvs/apk2gold)  - Yet another Android decompiler.
-   [ApkTool](http://ibotpeaches.github.io/Apktool/)  - Android Decompiler.
-   [Barf](https://github.com/programa-stic/barf-project)  - Binary Analysis and Reverse engineering Framework.
-   [Binary Ninja](https://binary.ninja/)  - Binary analysis framework.
-   [BinUtils](http://www.gnu.org/software/binutils/binutils.html)  - Collection of binary tools.
-   [BinWalk](https://github.com/devttys0/binwalk)  - Analyze, reverse engineer, and extract firmware images.
-   [Boomerang](https://github.com/nemerle/boomerang)  - Decompile x86 binaries to C.
-   [ctf_import](https://github.com/docileninja/ctf_import)  – run basic functions from stripped binaries cross platform.
-   [cwe_checker](https://github.com/fkie-cad/cwe_checker)  - cwe_checker finds vulnerable patterns in binary executables.
-   [demovfuscator](https://github.com/kirschju/demovfuscator)  - A work-in-progress deobfuscator for movfuscated binaries.
-   [Frida](https://github.com/frida/)  - Dynamic Code Injection.
-   [GDB](https://www.gnu.org/software/gdb/)  - The GNU project debugger.
-   [GEF](https://github.com/hugsy/gef)  - GDB plugin.
-   [Ghidra](https://ghidra-sre.org/)  - Open Source suite of reverse engineering tools. Similar to IDA Pro.
-   [Hopper](http://www.hopperapp.com/)  - Reverse engineering tool (disassembler) for OSX and Linux.
-   [IDA Pro](https://www.hex-rays.com/products/ida/)  - Most used Reversing software.
-   [Jadx](https://github.com/skylot/jadx)  - Decompile Android files.
-   [Java Decompilers](http://www.javadecompilers.com/)  - An online decompiler for Java and Android APKs.
-   [Krakatau](https://github.com/Storyyeller/Krakatau)  - Java decompiler and disassembler.
-   [Objection](https://github.com/sensepost/objection)  - Runtime Mobile Exploration.
-  [OllyDbg](http://www.ollydbg.de/) - Binary analysis framework
-   [PEDA](https://github.com/longld/peda)  - GDB plugin (only python2.7).
-   [Pin](https://software.intel.com/en-us/articles/pin-a-dynamic-binary-instrumentation-tool)  - A dynamic binary instrumentaion tool by Intel.
-   [PINCE](https://github.com/korcankaraokcu/PINCE)  - GDB front-end/reverse engineering tool, focused on game-hacking and automation.
-   [PinCTF](https://github.com/ChrisTheCoolHut/PinCTF)  - A tool which uses intel pin for Side Channel Analysis.
-   [Plasma](https://github.com/joelpx/plasma)  - An interactive disassembler for x86/ARM/MIPS which can generate indented pseudo-code with colored syntax.
-   [Pwndbg](https://github.com/pwndbg/pwndbg)  - A GDB plugin that provides a suite of utilities to hack around GDB easily.
-   [radare2](https://github.com/radare/radare2)  - A portable reversing framework.
-   [Triton](https://github.com/JonathanSalwan/Triton/)  - Dynamic Binary Analysis (DBA) framework.
-   [Uncompyle](https://github.com/gstarnberger/uncompyle)  - Decompile Python 2.7 binaries (.pyc).
-   [WinDbg](http://www.windbg.org/)  - Windows debugger distributed by Microsoft.
-   [Xocopy](http://reverse.lostrealm.com/tools/xocopy.html)  - Program that can copy executables with execute, but no read permission.
-   [Z3](https://github.com/Z3Prover/z3)  - A theorem prover from Microsoft Research.

_JavaScript Deobfuscators_

-   [Detox](http://relentless-coding.org/projects/jsdetox/install)  - A Javascript malware analysis tool.
-   [Revelo](http://www.kahusecurity.com/posts/revelo_javascript_deobfuscator.html)  - Analyze obfuscated Javascript code.

_SWF Analyzers_

-   [RABCDAsm](https://github.com/CyberShadow/RABCDAsm)  - Collection of utilities including an ActionScript 3 assembler/disassembler.
-   [Swftools](http://www.swftools.org/)  - Collection of utilities to work with SWF files.
-   [Xxxswf](https://bitbucket.org/Alexander_Hanel/xxxswf)  - A Python script for analyzing Flash files.

### Forensics

_Tools used for solving Forensics challenges_

-   [Aircrack-Ng](http://www.aircrack-ng.org/)  - Crack 802.11 WEP and WPA-PSK keys.
    -   `apt-get install aircrack-ng`
-   [Audacity](http://sourceforge.net/projects/audacity/)  - Analyze sound files (mp3, m4a, whatever).
    -   `apt-get install audacity`
-  [sound-visualizer](http://www.sonicvisualiser.org/) - Audio file visualization.
-   [Bkhive and Samdump2](http://sourceforge.net/projects/ophcrack/files/samdump2/)  - Dump SYSTEM and SAM files.
    -   `apt-get install samdump2 bkhive`
-   [CFF Explorer](http://www.ntcore.com/exsuite.php)  - PE Editor.
-   [Creddump](https://github.com/moyix/creddump)  - Dump windows credentials.
-   [DVCS Ripper](https://github.com/kost/dvcs-ripper)  - Rips web accessible (distributed) version control systems.
-   [Exif Tool](http://www.sno.phy.queensu.ca/~phil/exiftool/)  - Read, write and edit file metadata.
-   [Extundelete](http://extundelete.sourceforge.net/)  - Used for recovering lost data from mountable images.
-   [Fibratus](https://github.com/rabbitstack/fibratus)  - Tool for exploration and tracing of the Windows kernel.
-   [Foremost](http://foremost.sourceforge.net/)  - Extract particular kind of files using headers.
    -   `apt-get install foremost`
-   [Fsck.ext4](http://linux.die.net/man/8/fsck.ext3)  - Used to fix corrupt filesystems.
-   [Malzilla](http://malzilla.sourceforge.net/)  - Malware hunting tool.
-   [NetworkMiner](http://www.netresec.com/?page=NetworkMiner)  - Network Forensic Analysis Tool.
-   [PDF Streams Inflater](http://malzilla.sourceforge.net/downloads.html)  - Find and extract zlib files compressed in PDF files.
-   [Pngcheck](http://www.libpng.org/pub/png/apps/pngcheck.html)  - Verifies the integrity of PNG and dump all of the chunk-level information in human-readable form.
    -   `apt-get install pngcheck`
-   [ResourcesExtract](http://www.nirsoft.net/utils/resources_extract.html)  - Extract various filetypes from exes.
-   [Shellbags](https://github.com/williballenthin/shellbags)  - Investigate NT_USER.dat files.
-   [Snow](https://sbmlabs.com/notes/snow_whitespace_steganography_tool)  - A Whitespace Steganography Tool.
-   [USBRip](https://github.com/snovvcrash/usbrip)  - Simple CLI forensics tool for tracking USB device artifacts (history of USB events) on GNU/Linux.
-   [Volatility](https://github.com/volatilityfoundation/volatility)  - To investigate memory dumps.

_Registry Viewers_

-   [OfflineRegistryView](https://www.nirsoft.net/utils/offline_registry_view.html)  - Simple tool for Windows that allows you to read offline Registry files from external drive and view the desired Registry key in .reg file format.
-   [Registry Viewer®](https://accessdata.com/product-download/registry-viewer-2-0-0)  - Used to view Windows registries.

### Steganography

_Tools used for solving Steganography challenges_

-   [AperiSolve](https://aperisolve.fr/)  - Aperi'Solve is a platform which performs layer analysis on image (open-source).
-   [Convert](http://www.imagemagick.org/script/convert.php)  - Convert images b/w formats and apply filters.
-   [Exif](http://manpages.ubuntu.com/manpages/trusty/man1/exif.1.html)  - Shows EXIF information in JPEG files.
-   [Exiftool](https://linux.die.net/man/1/exiftool)  - Read and write meta information in files.
-   [Exiv2](http://www.exiv2.org/manpage.html)  - Image metadata manipulation tool.
-   [Image Steganography](https://sourceforge.net/projects/image-steg/)  - Embeds text and files in images with optional encryption. Easy-to-use UI.
-   [Image Steganography Online](https://incoherency.co.uk/image-steganography)  - This is a client-side Javascript tool to steganographically hide images inside the lower "bits" of other images
-   [ImageMagick](http://www.imagemagick.org/script/index.php)  - Tool for manipulating images.
-   [Outguess](https://www.freebsd.org/cgi/man.cgi?query=outguess+&apropos=0&sektion=0&manpath=FreeBSD+Ports+5.1-RELEASE&format=html)  - Universal steganographic tool.
-  [Pngcheck](http://www.libpng.org/pub/png/apps/pngcheck.html) - Checks if PNG is valid
-   [Pngtools](https://packages.debian.org/sid/pngtools)  - For various analysis related to PNGs.
    -   `apt-get install pngtools`
-   [SmartDeblur](https://github.com/Y-Vladimir/SmartDeblur)  - Used to deblur and fix defocused images.
-   [Steganabara](https://www.openhub.net/p/steganabara)  - Tool for stegano analysis written in Java.
-   [Stegbreak](https://linux.die.net/man/1/stegbreak)  - Launches brute-force dictionary attacks on JPG image.
-   [StegCracker](https://github.com/Paradoxis/StegCracker)  - Steganography brute-force utility to uncover hidden data inside files.
-   [stegextract](https://github.com/evyatarmeged/stegextract)  - Detect hidden files and text in images.
-   [Steghide](http://steghide.sourceforge.net/)  - Hide data in various kind of images.
-   [Stegsolve](http://www.caesum.com/handbook/Stegsolve.jar)  - Apply various steganography techniques to images.
-   [Zsteg](https://github.com/zed-0xff/zsteg/)  - PNG/BMP analysis.

## Tutorials

_Tutorials to learn how to play CTFs_

-   [CTF Field Guide](https://trailofbits.github.io/ctf/)  - Field Guide by Trails of Bits.
-   [CTF Resources](http://ctfs.github.io/resources/)  - Start Guide maintained by community.
-   [Damn Vulnerable Web Application](http://www.dvwa.co.uk/)  PHP/MySQL web application that is damn vulnerable.
-   [How to Get Started in CTF](https://www.endgame.com/blog/how-get-started-ctf)  - Short guideline for CTF beginners by Endgame
-   [LiveOverFlow](https://www.youtube.com/channel/UClcE-kVhqyiHCcjYwcpfj9w)  - Video tutorials on Exploitation.
-   [MIPT CTF](https://github.com/xairy/mipt-ctf)  - A small course for beginners in CTFs (in Russian).


## Wargames

_Always online CTFs_

-   [PicoCTF](https://picoctf.com/) (*) - Excellent CTF for beginners and experienced members alike! **We recommend all new members start here!** 
-   [Over The Wire](http://overthewire.org/wargames/)  (*)- Wargame maintained by OvertheWire Community. The inital wargames (Bandit, Natas) are great for beginners. 
-   [Cryptopals](https://cryptopals.com/) (*) - Introduction to Cryptography CTF
-   [Pwnable.kr](http://pwnable.kr/)  - All purpose CTF, starts fairly easy but gets pretty hard later on.
-   [Microcorruption](https://microcorruption.com/)  (**)- Embedded security CTF. Great stack/heap CTF, GUI is a lot of fun.
-   [Hack The Box](https://www.hackthebox.eu/)  (\*\*-\*\*\*)- Weekly CTFs for all types of security enthusiasts. Has lots of challenges and virtual machines.
  
  <br>
  
-   [Backdoor](https://backdoor.sdslabs.co/)  - Security Platform by SDSLabs.
-   [Crackmes](https://crackmes.one/)  - Reverse Engineering Challenges.
-   [Exploit Exercises](https://exploit-exercises.lains.space/)  - Variety of VMs to learn variety of computer security issues.
-   [Exploit.Education](http://exploit.education/)  - Variety of VMs to learn variety of computer security issues.
-   [Gracker](https://github.com/Samuirai/gracker)  - Binary challenges having a slow learning curve, and write-ups for each level.
-   [Hack This Site](https://www.hackthissite.org/)  - Training ground for hackers.
-   [Hacking-Lab](https://hacking-lab.com/)  - Ethical hacking, computer network and security challenge platform.
-   [Hone Your Ninja Skills](https://honeyourskills.ninja/)  - Web challenges starting from basic ones.
-   [IO](http://io.netgarage.org/)  - Wargame for binary challenges.
-   [PentesterLab](https://pentesterlab.com/)  - Variety of VM and online challenges (paid).
-   [PWN Challenge](http://pwn.eonew.cn/)  - Binary Exploitation Wargame.
-   [Pwnable.tw](https://pwnable.tw/)  - Binary wargame.
-   [Pwnable.xyz](https://pwnable.xyz/)  - Binary Exploitation Wargame.
-   [Reversin.kr](http://reversing.kr/)  - Reversing challenge.
-   [Ringzer0Team](https://ringzer0team.com/)  - Ringzer0 Team Online CTF.
-   [Root-Me](https://www.root-me.org/)  - Hacking and Information Security learning platform.
-   [ROP Wargames](https://github.com/xelenonz/game)  - ROP Wargames.
-   [SANS HHC](https://holidayhackchallenge.com/past-challenges/)  - Challenges with a holiday theme released annually and maintained by SANS.
-   [SmashTheStack](http://smashthestack.org/)  - A variety of wargames maintained by the SmashTheStack Community.
-   [Viblo CTF](https://ctf.viblo.asia/)  - Various amazing CTF challenges, in many different categories. Has both Practice mode and Contest mode.
-   [VulnHub](https://www.vulnhub.com/)  - VM-based for practical in digital security, computer application & network administration.
-   [W3Challs](https://w3challs.com/)  - A penetration testing training platform, which offers various computer challenges, in various categories.
-   [WebHacking](http://webhacking.kr/)  - Hacking challenges for web.
-  [Net Force](https://www.net-force.nl/) - Web & Steg CTF
-  [CSAW Challenges](https://365.csaw.io/)
-  [Google XSS](https://xss-game.appspot.com/)

## Websites

_Various general websites about and on CTF_

-   [CTF Time](https://ctftime.org/)  - General information on CTF occuring around the worlds.
-   [Reddit Security CTF](http://www.reddit.com/r/securityctf)  - Reddit CTF category.

## Readings
-   [bi0s Wiki](https://teambi0s.gitlab.io/bi0s-wiki/)  - Wiki from team bi0s.
-   [ISIS Lab](https://github.com/isislab/Project-Ideas/wiki)  - CTF Wiki by Isis lab.
-   [OpenToAll](https://github.com/OpenToAllCTF/Tips)  - CTF tips by OTA CTF team members.
-  [CTF Resources](http://ctfs.github.io/resources/)
-  [Trail of Bits](https://trailofbits.github.io/ctf/)
-  [CTF-pwn-tips](https://github.com/Naetw/CTF-pwn-tips)
- [Crypton](https://github.com/ashutosh1206/Crypton) - Extensive library of Cryptography. Extremely in-depth
- [Heap Exploitation](https://heap-exploitation.dhavalkapil.com/) - Great guide on Heap Exploitation

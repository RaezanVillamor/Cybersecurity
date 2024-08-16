# PicoGym problem set 3
# -static aint always noise
# -strings it
# -plumbing

# 1) static aint always noise

# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./ static
# bash: ./: Is a directory
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./static
# bash: ./static: Permission denied
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ chmod +x static 
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./static
# Oh hai! Wait what? A flag? Yes, it's around here somewhere!
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./static | i
# Display all 106 possibilities? (y or n)
# i386                         ip6tables-nft
# ibus                         ip6tables-nft-restore
# ibus-daemon                  ip6tables-nft-save
# ibus-setup                   ip6tables-restore
# ibus-table-createdb          ip6tables-restore-translate
# iceauth                      ip6tables-save
# ico                          ip6tables-translate
# icontopbm                    ipcmk
# iconv                        ipcrm
# iconvconfig                  ipcs
# id                           ipmaddr
# identify                     ipod-read-sysinfo-extended
# identify-im6                 ipod-time-sync
# identify-im6.q16             ippeveprinter
# iecset                       ippfind
# if                           ipptool
# ifconfig                     ipp-usb
# ijs_pxljr                    iptables
# ilbmtoppm                    iptables-apply
# imagetops                    iptables-legacy
# im-config                    iptables-legacy-restore
# imgtoppm                     iptables-legacy-save
# im-launch                    iptables-nft
# import                       iptables-nft-restore
# --More--                          ^C
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./static | itdis.sh
# itdis.sh: command not found
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ i
# Display all 106 possibilities? (y or n)
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ i
# i: command not found
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./ ltdis.sh 
# bash: ./: Is a directory
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./ltdis.sh 
# bash: ./ltdis.sh: Permission denied
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ chmod +x ltdis.sh 
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./ltdis.sh 
# Attempting disassembly of  ...
# objdump: 'a.out': No such file
# objdump: section '.text' mentioned in a -j option, but not found in any input file
# Disassembly failed!
# Usage: ltdis.sh <program-file>
# Bye!
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./ltdis.sh | static
# objdump: 'a.out': No such file
# objdump: section '.text' mentioned in a -j option, but not found in any input file
# Command 'static' not found, but can be installed with:
# sudo apt install python3-static3
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./ltdis.sh | ./static
# Oh hai! Wait what? A flag? Yes, it's around here somewhere!
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./static | ltdis.sh
# ltdis.sh: command not found
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./static | ./ltdis.sh
# Attempting disassembly of  ...
# objdump: 'a.out': No such file
# objdump: section '.text' mentioned in a -j option, but not found in any input file
# Disassembly failed!
# Usage: ltdis.sh <program-file>
# Bye!
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./ ltdis.sh static
# bash: ./: Is a directory
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ./ltdis.sh static
# Attempting disassembly of static ...
# Disassembly successful! Available at: static.ltdis.x86_64.txt
# Ripping strings from binary with file offsets...
# Any strings found in static have been written to static.ltdis.strings.txt with file offset
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ ls
# big-zip-files      files      static
# big-zip-files.zip  files.zip  static.ltdis.strings.txt
# file               ltdis.sh   static.ltdis.x86_64.txt
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ grep -i static
# static                    static.ltdis.strings.txt  static.ltdis.x86_64.txt
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ grep -i static.ltdis.strings.txt 
# ^C
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ grep -i "pico" static.ltdis.strings.txt 
#    1020 picoCTF{d15a5m_t34s3r_6f8c8200}
# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ 




# 2) strings it
# Can you find the flag in file without running it?

# rae@rae-Swift-SF314-511:~/Documents/ETH/Codes!/Cybersecurity/PICOCodes/problem set downloads$ strings strings | grep "pico"
# picoCTF{5tRIng5_1T_7f766a23}

# 3) plumbing
# picoGym problem set 2
# -Obedient cat (follow the hints and solve this challenge using the shell)
# -wave a flag
# -convertme.py
# -whats a net cat

# 1) Obedient cat
# To get the file accessible in your shell, enter the following in the Terminal prompt: 
# $ wget https://mercury.picoctf.net/static/0e428b2db9788d31189329bed089ce98/flag
# then use cat flag to see the flag 

# 2) wave a flag
# get it using wget https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm
# then you should run ./warm in the terminal but however it may not be executable right away
# so then use chmod +x warm to make it executable then run the thing above

# 3) in convertme.py
# Run the Python script and convert the given number from decimal to binary to get the flag.
# using cyberchef

# 4) what's a net cat

# raev-picoctf@webshell:~$ nc -h
# OpenBSD netcat (Debian patchlevel 1.218-4ubuntu1)
# usage: nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl]
#           [-m minttl] [-O length] [-P proxy_username] [-p source_port]
#           [-q seconds] [-s sourceaddr] [-T keyword] [-V rtable] [-W recvlimit]
#           [-w timeout] [-X proxy_protocol] [-x proxy_address[:port]]
#           [destination] [port]
#         Command Summary:
#                 -4              Use IPv4
#                 -6              Use IPv6
#                 -b              Allow broadcast
#                 -C              Send CRLF as line-ending
#                 -D              Enable the debug socket option
#                 -d              Detach from stdin
#                 -F              Pass socket fd
#                 -h              This help text
#                 -I length       TCP receive buffer length
#                 -i interval     Delay interval for lines sent, ports scanned
#                 -k              Keep inbound sockets open for multiple connects
#                 -l              Listen mode, for inbound connects
#                 -M ttl          Outgoing TTL / Hop Limit
#                 -m minttl       Minimum incoming TTL / Hop Limit
#                 -N              Shutdown the network socket after EOF on stdin
#                 -n              Suppress name/port resolutions
#                 -O length       TCP send buffer length
#                 -P proxyuser    Username for proxy authentication
#                 -p port         Specify local port for remote connects
#                 -q secs         quit after EOF on stdin and delay of secs
#                 -r              Randomize remote ports
#                 -S              Enable the TCP MD5 signature option
#                 -s sourceaddr   Local source address
#                 -T keyword      TOS value
#                 -t              Answer TELNET negotiation
#                 -U              Use UNIX domain socket
#                 -u              UDP mode
#                 -V rtable       Specify alternate routing table
#                 -v              Verbose
#                 -W recvlimit    Terminate after receiving a number of packets
#                 -w timeout      Timeout for connects and final net reads
#                 -X proto        Proxy protocol: "4", "5" (SOCKS) or "connect"
#                 -x addr[:port]  Specify proxy address and port
#                 -Z              DCCP mode
#                 -z              Zero-I/O mode [used for scanning]
#         Port numbers can be individual or ranges: lo-hi [inclusive]
# raev-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 41120
# You're on your way to becoming the net cat master
# picoCTF{nEtCat_Mast3ry_3214be47}

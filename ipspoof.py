import sys

from scapy.all import *


if len(sys.argv) != 4:
    print ("Usage: ./spoof.py <target> <spoofed_ip>")
    sys.exit(1)


A = sys.argv[1] # spoofed source IP address
B = sys.argv[2] # destination IP address
payload = sys.argv[3]
C = RandShort() # source port
D = 80 # destination  port
#payload = "test_paylod" # packet payload


for i in range (0,5):
    spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
    send(spoofed_packet)


# Exactly what is happening !
# int sd;
# unsigned long dest_addr;
# unsigned long src_addr;
# src_addr = inet_addr(argv[1]);
# dest_addr = inet_addr(argv[2]);
# sd = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);
# setsockopt(sd, IPPROTO_IP, IP_HDRINCL, &on, sizeof(on));
# setsockopt(sd, SOL_SOCKET, SO_BROADCAST, &on, sizeof(on));
# int pack_size = sizeof(struct iphdr) + sizeof(struct icmphdr) + pay_load_size;
# char* packet = (char*)malloc(pack_size);
# ip->version = 4;
# ip->ihl = 5;
# ip->tos = 0;
# ip->tot_len=htons(pack_size);
# ip->id = rand();
# ip->frag_off=0;
# ip->ttl = 255;
# ip->protocol= IPPROTO_ICMP;
# ip->saddr=src_addr;
# ip->daddr=dest_addr;
# icmp->type= ICMP_ECHO;
# icmp->code=0;
# icmp->un.echo.sequence=rand();
# icmp->un.echo.id=rand();
# icmp->checksum=0;
# std::memset(packet + sizeof(struct iphdr) + sizeof(struct icmphdr), rand() % 255, pay_load_size);
# sendto(sd, packet, pack_size,0, (struct sockaddr*)&servaddr, sizeof(servaddr));

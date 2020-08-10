import whois
import socket

def get_info_by_domain(domain_name):

    try:

        ip_addr = socket.gethostbyname(domain_name)
        print("ip address : ",ip_addr)

        w = whois.whois(domain_name)

        print(w)

    except Exception as exp:
        print(exp)

 
my_domain = input("Enter a domain name : ")

get_info_by_domain(my_domain)



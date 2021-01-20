from pip._vendor.distlib.compat import raw_input
import subprocess
import pyfiglet

art = pyfiglet.figlet_format("DDoS-T.S", font="5lineoblique")
print(art)

print("Before starting Please Check the requirement first")
print("Otherwise the toolkit might not work")

print("[A]- Requirement ")       #installation and what not 
print("[B]- DNS to Ip Address ") #ping
print("[C]- PORT finder ")       #port
print("[D]- DDoS ")              #DDoS

while True:
    option = input("choose option between A - D >" " ")
    if option in ['A','B','C','D']:
        break

if option == "A": #requirement installation
    print("Requirement")
    print("pip")
    print("nmap - https://nmap.org/book/inst-windows.html")

    insnmap = input("Do you want to install nmap? [Y/N]")
    if insnmap in ['Y','N']:

        if insnmap == "Y":
            subprocess.run(['curl','https://nmap.org/dist/nmap-7.91-setup.exe','-o','nmap-7.91-setup.exe'])
            subprocess.Popen(['nmap-7.91-setup.exe'])
            subprocess.run(['python','start-1.py'])

        elif insnmap == "N":
            exit

elif option == "B": #ping website or ip
    dns = input("DNS? [Y/N] >" " ")
    if dns in ['Y','N']:

        if dns == "Y":
            print("ping DNS for ip")
            dnsip = raw_input("Input DNS" r""">>>--------> """)
            print("ctrl = c")
            subprocess.run(['ping', dnsip, '-t'])
        
        elif dns == "N":
            print("ping")
            ip = raw_input("Input IP" r""">>>--------> """)
            print("ctrl + c")
            subprocess.run(['ping', ip, '-t'])

elif option == "C": #port-find using nmap
    subprocess.run(['python', 'port-finder.py'])

elif option == "D": #DDoS
    subprocess.run(['python', 'dos.py'])

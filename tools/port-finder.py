from pip._vendor.distlib.compat import raw_input
import subprocess
import pyfiglet

pf = pyfiglet.figlet_format("S-PF", font="5lineoblique")
print(pf)

print("ip example 192.168.1.1")
ipadd = raw_input("Ip-Address" r"""-------->>>> """)

print("Port range example 20-40")
pr = raw_input("Port-range" r"""-------->>>> """)

subprocess.run(["nmap", "-p", pr, "-Pn", ipadd])

hold = input("exit? [Y] >" " ")
if hold in ['Y']:
    if dns == "Y":
        exit



#created By eiji-codename Sakura
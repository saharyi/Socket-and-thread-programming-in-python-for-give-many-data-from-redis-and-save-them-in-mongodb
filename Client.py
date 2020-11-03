# In The Name of Allah
# the Compassionate the Merciful

import socket
import time
import queue;
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.43.253', 1234))
c1=0
q = queue.Queue()
while True:
    q.put(bytes("{'user': 'bob'}","utf-8"))
    client.send(q.get())
    c1=c1+1
    print(c1)
    time.sleep(0.25)
con.close()
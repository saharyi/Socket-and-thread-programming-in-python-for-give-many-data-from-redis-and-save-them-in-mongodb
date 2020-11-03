# In The Name of Allah
# the Compassionate the Merciful

import time
import ast
import socket
import threading
import queue

from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor

try:
    con = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="192.168.1.119"

serv.bind(("",1234))
serv.listen(5)
db = con.database
collection = db.test_collection

c2=0

q = queue.Queue()
lock = threading.Lock()

def worker():
    while lock.locked():
     time.sleep(0.25)

    lock.acquire()
    #if lock == 0:
          #lock = 1
    x = q.get().decode("utf-8")
    x1 = ast.literal_eval(x)
    collection.insert_one(x1)
    lock.release()
    #lock = 0

executor = ThreadPoolExecutor(2000)
#future = executor.submit(task, ("Completed"))

def task():
    while lock.locked():
     time.sleep(0.25)
    #if lock == 0:
    #lock = 1
    lock.acquire()
    data = conn.recv(5000)
    q.put(data)
    #lock = 0
    lock.release()

#lock = 0future = executor.submit(task,(lock))

while 1:

        print("*********")
        conn, addr = serv.accept()
        while 1:
         future = executor.submit(task)

         #from_client = ''
         #print('one client connect!!')
         #data = conn.recv(5000)
         #q.put(data)
         thread1 = threading.Thread(target=worker())
         thread1.start()
         #print(data)
         #if not data: break
         #x = data.decode("utf-8")
         #from_client += x
         #print (from_client)
         #x1 = ast.literal_eval(x)
         #q.put(x1)
         #print(x1)
         #thread = threading.Thread(target=worker())
         #thread.start()
         #collection.insert_one(q.get())
         c2=c2+1
         print(c2)
         #print(type(x1))
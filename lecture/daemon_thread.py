#daemon thread runs in background; when main program completes executing 
#the threads are terminated even if they havent finished their tasks

# import threading
# import time

# def background_task():
#     for i in range(5):
#         print(f"Daemon thread running {i}")
#         time.sleep(2)

# t=threading.Thread(target=background_task,daemon=True)
# t.start()



import threading
import time

def background_task():
    for i in range(5):
        print(f"Daemon thread running {i}")
        time.sleep(2)

t=threading.Thread(target=background_task,daemon=True)
t.start()
t.join()

#here, t.join() makes sure the program isnt terminated until the thread finishes it tasks
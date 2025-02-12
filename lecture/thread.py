import threading
import time

# def single_task():
#     print("Task started")
#     time.sleep(2)
#     print("Task completed")

# thread= threading.Thread(target=single_task)
# thread.start()
# thread.join()       #this join() helps the iterator to wait until the target is achieved. if it is not used then, the main thread will be executing
# print("Main thread execution completed")

# def task1():
#     for i in range(1,10,2):
#         print(f"I print odd numbers Task-1 count: {i}")
#         time.sleep(1)
# def task2():
#     for i in range(2,10,2):
#         print(f"I print even numbers Task-2 count: {i}")
#         time.sleep(1)
# thread1=threading.Thread (target=task1)
# thread2=threading.Thread (target=task2)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("\nMain thread is executed")

# def download_file(file_name):
#     print(f"Starting download: {file_name}")
#     time.sleep(3)
#     print(f"Download complete: {file_name}")

# files=["file1.zip","file2.zip","file3.zip"]
# threads=[]

# for file in files:
#     thread=threading.Thread(target=download_file,args=(file,))
#     threads.append(thread)
#     thread.start()
    
# for thread in threads:
#     thread.join()

# print("All downloads completed")

class TicketBooking:
    def __init__(self,available_tickets):
        self.available_tickets=available_tickets
        self.lock=threading.Lock()
    
    def book_ticket(self,name):
        print(f"{name} is trying to book a ticket...")
        with self.lock:
            if self.available_tickets>0:
                time.sleep(1)
                self.available_tickets-=1
                print(f"{name} Successfully booked a ticket! Remaining: {self.available_tickets}")
            else:
                print(f"Sorry {name}, no tickets available")

booking_system=TicketBooking(1)

threads=[]
users=["Alice","Bob"]
for user in users:
    t=threading.Thread(target=booking_system.book_ticket,args=(user,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
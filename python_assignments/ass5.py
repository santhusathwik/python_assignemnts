class Email:
    def __init__(self):
        print("This is an Email")

    def send_email(self,s):
        print(f"The notification is '{s}' ")

class SMS:
    def __init__(self):
        print("This is an SMS")

    def send_sms(self,s):
        print(f"The notification is '{s}' ")

class Push:
    def __init__(self):
        print("This is a Push message")

    def send_push(self,s):
        print(f"The notification is '{s}' ")

def fn(obj):
    s=input("Add your text here")
    if hasattr(obj,'send_email'):
        obj.send_email(s)

    if hasattr(obj,'send_sms'):
        obj.send_sms(s)

    if hasattr(obj,'send_push'):
        obj.send_push(s)

print("1:Email\n2:SMS\n3:Push")
n=int(input("Enter the choice"))

if n==1:    
    email=Email()
    fn(email)
if n==2:    
    sms=SMS()
    fn(sms)
if n==3:     
    push=Push()
    fn(push)

import os
from twilio.rest import Client

# setup
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Số điện thoại nhận tin nhắn
#to_number = input("\nsdt: ")

# Số điện thoại của tài khoản Twilio
from_number = ''

# Nội dung tin nhắn
message = input("\nNoi Dung: ")

with open('sdt.txt') as f:
    numbers = f.readlines()
numbers = [x.strip() for x in numbers]

# send all list
for to_number in numbers:
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body=message)
    print('Message sent successfully to', to_number)

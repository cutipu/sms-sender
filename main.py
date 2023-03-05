import os
from twilio.rest import Client

# Thiết lập thông tin tài khoản Twilio
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Số điện thoại nhận tin nhắn
to_number = input("\nsdt: ")

# Số điện thoại của tài khoản Twilio
from_number = ''

# Nội dung tin nhắn
message = input("\nNoi Dung: ")

# Gửi tin nhắn
message = client.messages.create(
    to=to_number,
    from_=from_number,
    body=message)

print('Message sent successfully to', to_number)

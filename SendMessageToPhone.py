from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC975f26475695eb07b6c3c87963459a85"
# Your Auth Token from twilio.com/console
auth_token  = "2ed44a83dcda82e12c4c43faae25909f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8613855067647", # 区号+你的手机号码
    from_="+14047954295",  # 你的 twilio 电话号码
    body="Hello from Python!")

print(message.sid)
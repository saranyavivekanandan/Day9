from twilio.rest import Client
#
#
# account = 'AC2f93079cb2fc82562f1fd2fd45f4e55a'
# auth = '2ad1596f003dfb430f8caa55c18e340e'
# mycell= '+919940383040'
# mytwilio = '+12057368558'
#
# client = Client(account, auth)
# new= ''.join(['New Message' for i in range(10)])
# print((['New Message' for i in range(10)]))
# mymessage = client.messages.create(to=mycell, from_=mytwilio, body=new)


# from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC2f93079cb2fc82562f1fd2fd45f4e55a'
auth_token = '2ad1596f003dfb430f8caa55c18e340e'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+919940383040',
                        from_='+12057368558'
                    )

print(call.sid)

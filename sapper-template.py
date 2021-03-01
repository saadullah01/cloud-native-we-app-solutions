import pexpect
import time
import os

user = os.environ["username"]
token = os.environ["access_token"]

print("Pushing Code to GitHub:")
ch = pexpect.spawn('git push')
ch.expect('Username for .*:')
ch.sendline(user)
ch.expect('Password for .*:')
ch.sendline(token)
time.sleep(5)
print("Done")

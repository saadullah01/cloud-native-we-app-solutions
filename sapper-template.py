import pexpect
import time

print("Pushing Code to GitHub:")
ch = pexpect.spawn(' git push --set-upstream origin add-the-web-application')
ch.expect('Username for .*:')
ch.sendline('$username')
ch.expect('Password for .*:')
ch.sendline('$password')
time.sleep(5)
print("Done")
'''
    Auto Script to add, commit and push code to GitHub
    Arguments:
    ----------
    commands.txt
'''

import pexpect, os, sys, time


# Parameters
push_timeout = 10

# Variables
username = os.environ["username"]
password = os.environ["access_token"]
repo_name = os.environ["repository_name"]
cmd_dir = "/Educative/" + repo_name + "/"

pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m 'message'", cwd=cmd_dir)
ch = pexpect.spawn('git push', cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(push_timeout)
print("Done")

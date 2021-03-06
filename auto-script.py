'''
    Auto Script to add, commit and push code to GitHub

    Arguments:
    ----------
    1. timeout: int
    2. commit_comment: string
    3. branch_name: string or None
'''

import pexpect, os, sys, time

f = open(sys.argv[1], "r")

arguments = f.readline()[:-1].split(",")

timeout = int(arguments[0])
commit_comment = arguments[1]

# Environment Variables
username = os.environ["username"]
password = os.environ["access_token"]
cmd_dir = "/Educative/" + os.environ["repository_name"]
commit_cmd = "git commit -m '" + commit_comment + "'"
push_cmd = "git push"

if len(arguments) == 3:
    branch_name = arguments[0]
    push_cmd = "git push --set-upstream origin " + branch_name

commands = f.readlines()

print("Pushing Code to GitHub:")
for cmd in commands:
    cd = cmd[:-1].split(",")
    pexpect.run(cd[0], cwd=cd[1])
pexpect.run("git add .", cwd=cmd_dir)
pexpect.run(commit_cmd, cwd=cmd_dir)
ch = pexpect.spawn(push_cmd, cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(timeout)
print("Done")

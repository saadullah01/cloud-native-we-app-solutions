'''
    Auto Script to add, commit and push code to GitHub

    Arguments:
    ----------
    1. timeout: int
    2. commit_comment: string
    3. branch_name: string or None
'''

import pexpect, os, sys

timeout = int(sys.argv[1])
commit_comment = sys.argv[2]
branch_name = sys.argv[3]

username = os.environ["username"]
password = os.environ["access_token"]
cmd_dir = "/Educative/" + os.environ["repository_name"]
commit_cmd = "git commit -m '" + commit_comment + "'"
push_cmd = "git push"

if branch_name:
    push_cmd = "git push --set-upstream origin " + branch_name

print("Pushing Code to GitHub:")
pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m ", cwd=cmd_dir)
ch = pexpect.spawn(push_cmd, cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
ch.expect('root@educative:.*', timeout=timeout)
print("Done")

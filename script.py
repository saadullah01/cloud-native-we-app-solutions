'''
    Auto Script to add, commit and push code to GitHub
    Arguments:
    ----------
    commands.txt
'''

import pexpect, os, sys, time

f = open(sys.argv[1], "r")

parameters = f.readline()[:-1].split(",")

# Parameters from file
push_timeout = int(parameters[0])
commit_comment = parameters[1]
clone_branch = parameters[2]
commit_branch = parameters[3]

# Variables
username = os.environ["username"]
password = os.environ["access_token"]
repo_name = os.environ["repository_name"]
cmd_dir = "/Educative/" + repo_name + "/"

# Commit Command
commit_cmd = "git commit -m '" + commit_comment + "'"

# Push Command
push_cmd = "git push"
if commit_branch != "none":
    push_cmd = "git push --set-upstream origin " + commit_branch

# Clone Command
clone_cmd = "git clone https://github.com/"+username+"/"+repo_name+".git"
if clone_branch != "none":
    clone_cmd = "git clone -b " + clone_branch + " https://github.com/"+username+"/"+repo_name+".git"

print("Pushing Code to GitHub:")
pexpect.run(clone_cmd, cwd="/Educative")

# Add, commit and push
pexpect.run("git add .", cwd=cmd_dir)
pexpect.run(commit_cmd, cwd=cmd_dir)
ch = pexpect.spawn(push_cmd, cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(push_timeout)
print("Done")

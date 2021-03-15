'''
    Auto Script to add, commit and push code to GitHub
    Arguments:
    ----------
    commands.txt
'''

import pexpect, os, sys, time

# Variables
username = os.environ["username"]
password = os.environ["access_token"]
repo_name = os.environ["repository_name"]

print("Pushing to GitHub Repo '"+repo_name+"'...")
# Clone user's repo
pexpect.run(
    "git clone -b enable-firebase-hosting https://github.com/"+username+"/"+repo_name+".git",
    cwd="/Educative/")

cmd_dir = "/Educative/" + repo_name + "/"

pexpect.run("mkdir firebase", cwd=cmd_dir+"services/web/")
pexpect.run("cp /Educative/cnwa-solution-files/files/firebase/package.json "+cmd_dir+"services/web/firebase/")
pexpect.run("cp /Educative/cnwa-solution-files/files/firebase/package-lock.json "+cmd_dir+"services/web/firebase/")
pexpect.run("npm install -D firebase-tools", cwd=cmd_dir+"services/web/firebase")
pexpect.run("cp /Educative/cnwa-solution-files/files/services-web/package.json "+cmd_dir+"services/web/")

pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m 'Install Firebase CLI'", cwd=cmd_dir)
ch = pexpect.spawn('git push', cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(5)
print("Done")

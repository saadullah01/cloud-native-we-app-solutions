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
author = os.environ["author"]

print("Pushing code to GitHub Repo '"+repo_name+"'...")
# Clone user repo
pexpect.run(
    "git clone https://github.com/"+username+"/"+repo_name+".git",
    cwd="/Educative/")

# Running solution commands
cmd_dir = "/Educative/" + repo_name + "/"

pexpect.run("git switch -c add-the-web-application", cwd=cmd_dir)
pexpect.run("mkdir services", cwd=cmd_dir)
pexpect.run("npx degit \"sveltejs/sapper-template#rollup\" web", cwd=cmd_dir+"services/")
pexpect.run("git add -A services/", cwd=cmd_dir)
pexpect.run("git commit -m \"Add the web service, based on the Sapper template.\"", cwd=cmd_dir)
ch = pexpect.spawn("git push --set-upstream origin add-the-web-application", cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(5)
print("Done")

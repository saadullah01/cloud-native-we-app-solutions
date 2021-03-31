'''
    Auto Script to add, commit and push code to GitHub
    Arguments:
    ----------
    commands.txt
'''

import pexpect, os, sys, time, json

# Variables
username = os.environ["username"]
password = os.environ["access_token"]
repo_name = os.environ["repository_name"]
firebase_proj = os.environ["firebase_proj_name"]
cypress_projectID = os.environ["cypress_projectID"]
dev_api_key = os.environ["dev_api_key"]

print("Pushing code to GitHub repo '"+repo_name+"'...")
# Clone user's repo
pexpect.run(
    "git clone https://github.com/"+username+"/"+repo_name+".git",
    cwd="/Educative/")

cmd_dir = "/Educative/" + repo_name + "/"
sol_dir = "/Educative/cnwa-solution-files/files/"

pexpect.run("git switch -c speed-up-CI-CD", cwd=cmd_dir)
pexpect.run("cp "+sol_dir+"services-web-firebase-functions-src-firestoreposts-on-create-cross-post-to-devto.yml "+cmd_dir+".github/workflows/")
pexpect.run("cp "+sol_dir+"services-web.yml "+cmd_dir+".github/workflows/")
pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m 'Speed up CI/CD'", cwd=cmd_dir)
ch = pexpect.spawn('git push --set-upstream origin speed-up-CI-CD', cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(5)
print("Done")

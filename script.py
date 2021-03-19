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
firebase_proj = os.environ["firebase_proj_name"]

# Clone user's repo
pexpect.run(
    "git clone -b enable-firebase-hosting https://github.com/"+username+"/"+repo_name+".git",
    cwd="/Educative/")

cmd_dir = "/Educative/" + repo_name + "/"
sol_dir = "/Educative/cnwa-solution-files/files/"

# Handling .firebaserc
data = {
  "projects": {
    "default": firebase_proj
  }
}
with open(cmd_dir+"services/web/firebase/.firebaserc", "w") as jsonFile:
    json.dump(data, jsonFile, indent=2)

pexpect.run("rm -rf public", cwd=cmd_dir+"services/web/firebase/")
pexpect.run("cp "+sol_dir+"firebase/package-lock.json "+cmd_dir+"services/web/firebase/")
pexpect.run("cp "+sol_dir+"firebase/package.json "+cmd_dir+"services/web/firebase/")
pexpect.run("cp "+sol_dir+"services-web/package-lock.json "+cmd_dir+"services/web/")
pexpect.run("cp "+sol_dir+"services-web/package.json "+cmd_dir+"services/web/")
pexpect.run("cp "+sol_dir+"services-web/.gitignore "+cmd_dir+"services/web/")

pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m 'web application deployed'", cwd=cmd_dir)
ch = pexpect.spawn('git push', cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(5)
print("Done")

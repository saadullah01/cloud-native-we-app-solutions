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

pexpect.run("mkdir services/web/firebase", cwd=cmd_dir)
ch = pexpect.spawn("npm init", cwd=cmd_dir+"services/web/firebase")
ch.expect("package name: (firebase)")
ch.sendline("web-firebase")
ch.expect("version: (1.0.0)")
ch.sendline("")
ch.expect("description:")
ch.sendline("The web service's Firebase project.")
ch.expect("entry point: (index.js)")
ch.sendline("")
ch.expect("test command:")
ch.sendline("")
ch.expect("git repository:")
ch.sendline("")
ch.expect("keywords:")
ch.sendline("")
ch.expect("author:")
ch.sendline("")
ch.expect("license: (ISC)")
ch.sendline("")
ch.expect("Is this OK? (yes)")
ch.sendline("yes")
pexpect.run("npm install -D firebase-tools", cwd=cmd_dir+"services/web/firebase")

pexpect.run("cp /Educative/cnwa-solution-files/files/services-web/package.json "+cmd_dir+"services/web/")
pexpect.run("cp /Educative/cnwa-solution-files/files/services-web-firebase/package.json "+cmd_dir+"services/web/firebase/")

pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m 'Install Firebase CLI'", cwd=cmd_dir)
ch = pexpect.spawn('git push', cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(5)
print("Done")

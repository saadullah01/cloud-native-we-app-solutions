'''
    Auto Script to add, commit and push code to GitHub
    Arguments:
    ----------
    commands.txt
'''

import pexpect, os, sys, time

# Environment Variables
username = os.environ["username"]
password = os.environ["access_token"]
repo_name = os.environ["repository_name"]

# 1) Creating repo
print("Creating GitHub Project '" + repo_name + "':")
create_repo = pexpect.spawn("curl -u '" + username + "' https://api.github.com/user/repos -d '{\"name\":\"" + repo_name + "\"}'")
create_repo.expect("Enter host password for user .*:")
create_repo.sendline(password)
time.sleep(5)
print("Done")

# 2) Pushing monorepo template to GitHub
print("Pushing monorepo template to GitHub")
pexpect.run("mv /Educative/my_cloud_native_web_app " + repo_name) # Changing name

cmd_dir = "/Educative/" + repo_name + "/"

pexpect.run("git init", cwd=cmd_dir)
pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m 'my first commit'", cwd=cmd_dir)
pexpect.run("git branch -M main", cwd=cmd_dir)
pexpect.run("git remote add origin https://github.com/" + username + "/" + repo_name + ".git", cwd=cmd_dir)
ch = pexpect.spawn("git push -u origin main", cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(5)
print("Done")

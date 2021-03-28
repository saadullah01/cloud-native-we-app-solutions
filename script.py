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

print("Pushing code to GitHub repo '"+repo_name+"'...")
# Clone user's repo
pexpect.run(
    "git clone https://github.com/"+username+"/"+repo_name+".git",
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

# Handling cypress.json
data2 = {
  "baseUrl": "http://localhost:3000/",
  "componentFolder": "cypress/components",
  "experimentalComponentTesting": True,
  "projectId": cypress_projectID
}
with open(cmd_dir+"services/web/cypress.json", "w") as jsonFile:
  json.dump(data2, jsonFile, indent=2)

pexpect.run("git switch -c add-user-auth", cwd=cmd_dir)
pexpect.run("cp "+sol_dir+"template.html "+cmd_dir+"services/web/src/")
pexpect.run("git add .", cwd=cmd_dir)
pexpect.run("git commit -m 'configured Firebase Authentication and FirebaseUI'", cwd=cmd_dir)
ch = pexpect.spawn('git push --set-upstream origin add-user-auth', cwd=cmd_dir)
ch.expect('Username for .*:')
ch.sendline(username)
ch.expect('Password for .*:')
ch.sendline(password)
time.sleep(5)
print("Done")

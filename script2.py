import os, json

firebase_proj = os.environ["firebase_proj_name"]
cmd_dir = "/Educative/" + repo_name + "/"

# Handling .firebaserc
data = {
  "projects": {
    "default": firebase_proj
  }
}
with open(cmd_dir+"services/web/firebase/.firebaserc", "w") as jsonFile:
    json.dump(data, jsonFile, indent=2)
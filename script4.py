import os, json

dev_api_key = os.environ["dev_api_key"]
cmd_dir = "/Educative/"+repo_name+"/"

data = {
  "crossposttodevto": {
    "apikey": dev_api_key
  }
}
with open(cmd_dir+"services/web/firebase/functions/.runtimeconfig.json", "w") as jsonFile:
  json.dump(data, jsonFile, indent=2)
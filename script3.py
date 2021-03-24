import os, json

repo_name = os.environ["repository_name"]
cmd_dir = "/Educative/"+repo_name+"/"
# Handling .firebaserc
data = {
  "baseUrl": "http://localhost:3000/",
  "componentFolder": "cypress/components",
  "experimentalComponentTesting": True,
  "projectId": "wp6hgi"
}

with open(cmd_dir+"services/web/cypress.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=2)
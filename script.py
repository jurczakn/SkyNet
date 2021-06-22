import requests
import json
import pprint
import sys

from requests.api import request
from datetime import date, datetime, timedelta

#variable to store all associate contributions
contribuitions = {}

#set up headers and org accessing
config = json.load(open('SkyNetConfig.json'))

head = {"User-Agent": "SkyNet", "Authorization": "token {}".format(config["token"])}
org = config["org"]

since = ""

until = ""

dateformat = "%Y-%m-%dT%H:%M:%SZ"

if len(sys.argv) >= 2:

    since = sys.argv[1]

    print("len > 2")

    if len(sys.argv) >= 3:
        print("len > 3")
        until = sys.argv[2]

    else:    
        print("second date not given")
        sdatetime = datetime.strptime(since, dateformat)
        until = (sdatetime + timedelta(days=1)).strftime(dateformat)

else:
    until = datetime.now().strftime(dateformat)
    sdatetime = datetime.strptime(until, dateformat)
    since = (sdatetime - timedelta(days=1)).strftime(dateformat)

print("Start date: {}".format(since))
print("End date: {}".format(until))


def tally_commit(contributions, files, author):
    linesAdded = 0
    linesRemoved = 0

    for file in files:
        linesAdded += file["additions"]
        linesRemoved += file["deletions"]

    if author in contribuitions:
        contribuitions[author]["linesAdded"] += linesAdded
        contribuitions[author]["linesRemoved"] += linesRemoved
    else:
        contribuitions[author]={"linesAdded": linesAdded, "linesRemoved": linesRemoved}

def get_commit(contributions, commit):
    if type(commit) is not dict or "url" not in commit:
        print(commit)
        return
    commitReq = requests.get(commit["url"], headers=head)
    commitObj = json.loads(commitReq.text)
    if "committer" in commitObj:
        #print (commitObj["committer"])
        if commitObj["committer"] != None and"login" in commitObj["committer"]:
            author = commitObj["committer"]["login"]
            tally_commit(contribuitions, commitObj["files"], author)
        else:
            print("missing committer for commit ")#{}".format(commitObj))
    else:
        print("missing committer for commit ")#{}".format(commitObj))

def get_repo(repo):
    print("Checking repo: {}".format(repo["name"]) )
    repoCommits = requests.get(repo["url"]+"/commits?per_page=100&since={}&until={}".format(since, until), headers=head)
    reposCommitsObj = json.loads(repoCommits.text)
    #print (reposCommitsObj[0]["url"])

    #grab each commit
    for commit in reposCommitsObj:
        get_commit(contribuitions, commit)

#make request to repos on org
r = requests.get("http://api.github.com/orgs/"+org+"/repos?per_page=100", headers=head)
#print(r.text)
orgObject = json.loads(r.text)
#print(orgObject)
#print(orgObject[0]["url"])

#make request to commits on repo
for repo in orgObject:
    get_repo(repo)

#print ("author: {}".format(commit1Obj["author"]["login"]))

#tally lines added and removed for commit

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(contribuitions)
import requests as req
import json

userInfo = []
api = "https://codeforces.com/api/user.info?handles="

with open("data.txt", "r") as fp:
    for line in fp:
        info = line.split(";")
        userInfo.append([info[0], info[1], -1])

for item in userInfo:
    item[2] = json.loads(req.get(api + item[0]).text)["result"][0]["rating"]

sorted(userInfo, key=lambda x: x[2])

for item in userInfo:
    print("(%d) %s \"%s\"" % (item[2], item[1], item[0]))

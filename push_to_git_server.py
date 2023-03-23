import os
import subprocess
import xml.etree.ElementTree as ET

# Define the remote URL and project name
remote_url = "http://192.168.110.191:3000/exTHmUI/"
project_path = "/home/maribel/android13/exthm-13/"

# Parse the manifest.xml file
tree = ET.parse("/home/maribel/android13/exthm-13/android/snippets/exthm.xml")
root = tree.getroot()

for project in root.findall("project"):
    path = project.get("path")
    remote = remote_url + project.get("name")
    name = project.get("name")
    print("进入",path,"目录")
    os.chdir(project_path + path)
    #print("curl","-X","'POST'","'http://192.168.110.191:3000/api/v1/orgs/exTHmUI/repos'","-H","'accept: application/json'","-H","'authorization: Basic cm9vdDpTNzZqZm0wOQ=='","-H","'Content-Type: application/json'","-d","'"+'{"name": '+'"'+name+'"}'+"'")
    print("开始补全",name,"的历史提交")
    subprocess.run(["git","pull","exthm","Tenshi","--unshallow"])
    print("设定远程仓库")
    subprocess.run(["git","remote","add","local",remote])
    print("创建远端仓库")
    subprocess.run(["curl","-X","'POST'","'http://192.168.110.191:3000/api/v1/orgs/exTHmUI/repos'","-H","'accept: application/json'","-H","'authorization: Basic cm9vdDpTNzZqZm0wOQ=='","-H","'Content-Type: application/json'","-d","'"+'{"name": '+'"'+name+'"}'+"'"])
    print("推送仓库")
    subprocess.run(["git","push","local","HEAD:refs/heads/Tenshi"])
    print("=============结束=============")
    #print("path="+path,"remote="+remote)

#print("path="+project.get("path"),"remote="+remote_url+project.get("name"))
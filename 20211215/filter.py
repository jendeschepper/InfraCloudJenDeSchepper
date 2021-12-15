import json
from os import name
fname = "d:/School/2021-2022/infrastructure and cloud/InfraCloudJenDeSchepper/20211215/test.json"
with open(fname, "r") as file:
	docker_json = file.read()
docker_dict = json.loads(docker_json)
container_id = docker_dict[0]["Id"][0:6]
print(container_id)
Creatie_Datum = docker_dict[0]["Created"]
print(Creatie_Datum)
Status = docker_dict[0]["State"]["Status"]
print(Status)
Name_Container = docker_dict[0]["Name"]
print(Name_Container)
Host_Port = docker_dict[0]["HostConfig"]["PortBindings"]["5555/tcp"][0]["HostPort"]
print(Host_Port)
HostName = docker_dict[0]["Config"]["Hostname"]
print(HostName)
IP_Address = docker_dict[0]["NetworkSettings"]["IPAddress"]
print(IP_Address)
MAC_Address = docker_dict[0]["NetworkSettings"]["MacAddress"]
print(MAC_Address)
print(docker_dict[0].keys()[-1])
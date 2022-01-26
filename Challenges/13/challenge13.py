import json
from webexteamssdk import WebexTeamsAPI
import requests

current_access_token = "NjgxNjQ4NGQtZTM0Yi00MGEzLThiYTUtOWE5OTgyODllMjJjYTgzM2ZlOTUtMWI3_PE93_ca1cc44d-8847-4e5d-83d7-60b457809daa"
api = WebexTeamsAPI(access_token=current_access_token)
access_token = current_access_token

def JsonToWebex1(js_data):
    url = 'https://api.ciscospark.com/v1/rooms'

    headers = {'Authorization': 'Bearer {}'.format(access_token), 'Content-Type': 'application/json'}
    groups_struc = json.loads(js_data)

    for line in groups_struc["groups"]:
        createGroupName = line["group"]["group_name"]
        PayloadSpace = {"title": createGroupName}
        if PayloadSpace["title"] != None:
            res_space = requests.post(url, headers=headers, json=PayloadSpace)
            print(res_space)
            if res_space.status_code < 300:
                NEW_SPACE_ID = res_space.json()["id"]
                for mbr in line["group"]["members"]:
                    room_id = NEW_SPACE_ID
                    person_email = mbr["email"]
                    url2 = 'https://api.ciscospark.com/v1/memberships'
                    payload_member = {'roomId': room_id, 'personEmail': person_email}
                    res_member = requests.post(url2, headers=headers, json=payload_member)
                    print(res_member)

def main():

    js_groups = '''{"groups": [{"group": {"group_name": "Group_JDS", "members": [{"person_name": "Jen", "email": "jds@student.bxl.be"}]}}, {"group": {"group_name": "GROUP_ALPHA", "members": [{"person_name": "Vincent Cassata", "email": "vincent.cassata@student.bxl.be"}, {"person_name": "Giovanni Di Tulio", "email": "Giovanni.ditullio@student.bxl.be"}, {"person_name": "Milan Vandevelde", "email": "milan.vandevelde@student.bxl.be"}, {"person_name": "Tomas Vertessen", "email": "tomas.vertessen@student.bxl.be"}, {"person_name": "Mehdi Dahli", "email": "mehdi.dahli@student.bxl.be"}]}}, {"group": {"group_name": "GROUP_KAPPA", "members": [{"person_name": "Ur Salangpour", "email": "ur.salangpour@student.bxl.be"}, {"person_name": "Mon Gallin", "email": "mon.gallin@student.bxl.be"}, {"person_name": "Artur Ikiya", "email": "artur.lkiya@student.bxl.be"}, {"person_name": "Bram Vanbever", "email": "bram.vanbever@student.bxl.be"}, {"person_name": "JR Ibara", "email": "jr.ibara@student.bxl.be"}]}}, {"group": {"group_name": "GROUP_DELTA", "members": [{"person_name": "Jona Ferbiest", "email": "jona.ferbiest@student.bxl.be"}, {"person_name": "Bart Siperius", "email": "bart.siperius@student.bxl.be"}, {"person_name": "Joren Huysegoms", "email": "joren.huysegoms2@student.bxl.be"}, {"person_name": "Sam Bulduk", "email": "sam.bulduk@student.bxl.be"}, {"person_name": "Ferre Van Malder", "email": "ferre.vanmalder@student.bxl.be"}, {"person_name": "Mikail Defossez", "email": "mikail.defossez@student.bxl.be"}]}}, {"group": {"group_name": "* names are non-existent", "members": [{"person_name": "", "email": ""}]}}]}'''
    JsonToWebex1(js_groups)
    
if __name__ == '__main__':
    main()
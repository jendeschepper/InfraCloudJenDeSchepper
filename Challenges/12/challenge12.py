from turtle import shearfactor
import xlrd
import json

def FindPersonsAndGroups(ExcelFile):
    wb=xlrd.open_workbook(ExcelFile)
    sheet=wb.sheet_by_index(0)
    numberOfRows=sheet.nrows
    members=[]
    for idx in range(numberOfRows):
        if idx>0:
            member_dict={}
            member_dict["group"]=sheet.cell_value(idx,0)
            member_dict["name"]=sheet.cell_value(idx,1)
            member_dict["email"]=sheet.cell_value(idx,2)
            members.append(member_dict.copy())
    return members

def MakeListOfGroups(memberList):
    groups=[]
    member=None
    for member in memberList:
        group=member['group']
        if group not in groups:
            groups.append(group)
    return groups

def AttatchMembersToGroups(groupName, MemberList):
    memberDict={}
    allMembers=[memberDict]
    for member in MemberList:
        if member['group']==groupName:
            if member['name']!=None:
                memberDict['name']=member['name']
                memberDict['email']=member['email']
                allMembers.append(memberDict.copy())
    return allMembers

def main():
    memberList=FindPersonsAndGroups("/home/devasc/labs/GitJenDeSchepper/InfraCloudJenDeSchepper/Challenges/12/webexgroups.xlsx")
    groupList=MakeListOfGroups(memberList)
    allMembers=[]
    groups_struc={}
    groups_struc['groups']=[]
    for group in groupList:
        allMembers=AttatchMembersToGroups(group, memberList)
        del allMembers[0]
        groupDict={"group":{"groupName":group, "members":allMembers}}
        groups_struc['groups'].append(groupDict)
    js_groups=json.dumps(groups_struc, indent=2)
    print(js_groups)

if __name__=='__main__':
       main()
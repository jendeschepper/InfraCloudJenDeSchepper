import xlwt

groups_struc = {
 "groups": [
      { "group": { "group_name": "DEVASC_A" ,    
                   "members": [   
                     {"person_name": "Noel", "email": "noel@student.bxl.be"},
                     {"person_name": "Mary", "email": "mary@student.bxl.be"},
                     {"person_name": "Jens", "email": "jens@student.bxl.be"}
                   ]
                 }
      },
      { "group": { "group_name": "DEVASC_B" ,    
                   "members": [   
                     {"person_name": "Ives", "email": "ives@student.bxl.be"}, 
                     {"person_name": "John", "email": "john@student.bxl.be"}, 
                     {"person_name": "Alec", "email": "alec@student.bxl.be"}
                   ]     
                 }
      } 
   ]
}

people=[]

for group in groups_struc["groups"]:
  groupname = group["group"]["group_name"]
  for member in group["group"]["members"]:
    naam=member["person_name"]
    email=member["email"]
    person=[groupname, naam, email]
    people.append(person.copy())

#print(people)

workbook=xlwt.Workbook()
sheet=workbook.add_sheet('people')

for row in range(len(people)-1):
  rowstr=""
  for column in range(3):
    #sheet.write(row, column, people[row][column])
    rowstr+=people[row][column]
    rowstr+=", "
    #print(people[row][column])
  print(rowstr)

#workbook.save('/home/devasc/labs/GitJenDeSchepper/InfraCloudJenDeSchepper/Challenges/11/output.xlsx')
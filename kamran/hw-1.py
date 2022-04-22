#Healthcare
# Note patient reviews: scored out of 10 

# LocalPhysicians = ["Dr.Barry", "Dr.kawasaki", "Dr.Juan", "Dr.Candy", "Dr.Jacobs"]


 # for i in range(0, len(LocalPhysicians)):            #nameerror: 'Physicanname' isn't defined
    #print(LocalPhysicians[i])         # i refers to itteration variable and ranges from 0 - 5 with a break on 5.  
                                      # looping forward 


# for i in range(len(LocalPhysicians), 0) :    #nameerror: 'Physicanname' isn't defined
    # print(LocalPhysicians[i])  

 # for i in LocalPhysicians[0:2]:
   # print(i)                             # I want to access the first two physician names



# Doctorinfo = [{"Avg.patientreview":"10", "age":"30", "specialty":"Dermatology","practice":"hospital", "hrs worked":"40"},
# {"Avg patientreview":"5.3","age":"45", "specialty": "G.I.", "practice":"hospital"," hrs worked":"35"}, 
# {"Avg. patientreview":"7.6","age":"30", "specialty":"Family med." , "practice":"clinic", "hrs worked":"42"}, 
# {"Avg. patientreview":"8","age":"30", "specialty":"G.I." , "practice":"clinic", "hrs worked":"81"}, 
# {"Avg. patientreview":"5","age":"30", "specialty":"G.I." ," practice":"hospital", "hrs worked":"55"}]


 # for i in range(0, len(Doctorinfo)) :  #syntax error : 
   # print(Doctorinfo[i]) #again is in this context is accessing each dictioanry. 

# for i in range(len(Doctorinfo), 0) :  
  #  print(Doctorinfo[i])

# for i in range(Doctorinfo[0:3]) : # Typeerrorproblem was defining a proper min and max value

# for i in range(0,3) : 
   # print(Doctorinfo[i]['age'])


#School

# Grade8Students = ["John", "joe", "Sally", "Ann", "blake"]

# for i in range(0, len(Grade8Students)) : 
   # print(Grade8Students[i]) # indentation error - due to for-loop being placed on line 56 and i stands for in this context for every iteration it will produce the given dictionary

# for i in range(len(Grade8Students),0) : 
   #  print(Grade8Student[i])

# for i in range(3,5):  # This is wrong don't use splicing
    # print(Grade8Students[3:5])

# for i in range(3,5):
     # print(Grade8Students[i])

   
# studentDemographics = [{"age":"14", "ethnicity":"White", "GPA":"3.5","school-sport":"baseball","Fav.Class":"Math"},
  # {"age":"14", "ethnicity":"Asian", "GPA":"3.2","school-sport":"football","Fav.Class":"science"},
  # {"age":"15","ethnicity":"Black", "GPA":"4.0","school-sport":"golf","Fav.Class":"geography"},
  # {"age":"13", "ethnicity":"Arab", "GPA":"2.7","school-sport":"swimming","Fav.Class":"History"}, 
  # {"age":"13","ethnicity":"Black", "GPA":"3.4","school-sport":"running","Fav.Class":"Math"}
 #  ]

# for i in range(0,len(studentDemographics)) : 
    # print(studentDemographics[i])
  
#for i in range(len(studentDemographics),0) : #indentation error 
      # print(studentDemographics[i]) # come back to this one, it runs, but doesn't display on terminal. 

# for i in range(3,5) : 
   # print(studentDemographics[i]["school-sport"])




# Government 

livingPresidents = ["Obama", "Bush", "Carter", "Biden", "Trump"] #unexpected indent error

#for i in LivingPresidents : 
# print("President's Name is " + i)  # i in this case implicitly states the count behind the scenes, but is printing each dictionary

# for i in range(len(livingPresidents),0):
    # print("Cool I am reversing the list made of" + LivingPresidents[i])

# favorite_President= livingPresidents[1]
# print(favorite_President)

# favorite_President = 50  # changing the value of this variable from a string to integer. 
# print(favorite_President)


presidentDemographics = [
{"Age":"55", "Yrs served":"8", "Weekly_hrs_worked": "60", "Ethnicity":"Black","hobby":"Golf"},
{"Age":"82", "Yrs served":"8", "Weekly_hrs_worked": "54", "Ethnicity":"White","hobby":"Art"}, 
{"Age":"55", "Yrs served":"8", "Weekly_hrs_worked": "72", "Ethnicity":"White","hobby":"Travel"},
{"Age":"55", "Yrs served":"4", "Weekly_hrs_worked": "45", "Ethnicity":"White","hobby":"Cooking"}, 
{"Age":"55", "Yrs served":"8", "Weekly_hrs_worked": "80", "Ethnicity":"White","hobby":"videogames"}
]


#for i in range(0,len(presidentDemographics)):
   # print(presidentDemographics[i])

# for i in range(len(presidentDemographics),0):
   # print(presidentDemographics[i])

print(presidentDemographics[0])

print("My president is" + livingPresidents[0] + "and his demographics are" + presidentDemographics[0])
print(f"My president is {livingPresidents[0]} and his demographics are {presidentDemographics[0]}")


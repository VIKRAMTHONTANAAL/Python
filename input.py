# For given input:
# dict={"names":["abc","def","xyz"],"locations":["mumbai","pune","blore"]}
 
# Convert to output to:
# dict={"names":["ABC","DEF","XYZ"],"locations":["Mumbai","Pune","Blore"]}

dict={"names":["abc","def","xyz"],"locations":["mumbai","pune","blore"]}


for i in range(len(dict["names"])):
    dict["names"][i] = dict["names"][i].upper()

for i in range(len(dict["locations"])):
    dict["locations"][i] = dict["locations"][i].capitalize()

print(dict)
import json

listOfTuples=[]
with open('employee.json','r') as json_file:
    data=json.load(json_file)
    print(data)
    for row in data:
        print(row)
        listOfTuples.append(tuple(row.values()))
    print(listOfTuples)

import json
student={'Name':'SID','Age':'18','Department':'CSE'}
with open('studentfile.json','w+') as f1:
    json.dump(student,f1,indent=4)
    f1.seek(0)
    data=json.load(f1)
    print(data["Name"])
    

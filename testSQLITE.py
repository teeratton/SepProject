from firebase import firebase
import random
firebase = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')

#firebase.put('Students','S4',{'first':'asdsad','last':'sds','age':50})

subjects = {"math":1,"math1":2}
print(subjects.get('math'))



inid = "ton123"
id = firebase.get('/Login/'+inid,None)
if(id.get('password') == "teerast"):
    print("get in")
else:
    print("incorrect password")

teachers = firebase.get('/Teachers',None)
teacher1 = teachers.get('UkritH')
subjects = teacher1.get('subjects')
print(subjects)
print(teacher1)



table = firebase.get('/Students',None)
table = table.get('S4')
t1 = table.get('age')
print(t1)

def createAcount(first, last, username):
    count = 1;
    teacher2 = {'first': first, 'last': last, 'password': 'abc', 'role': 'teacher',
                'subjects': {'sub1': 'java2', 'sub2': 'jaba2'}}
    if(checkUsername(username) == 1):
        firebase.put('Teachers', username, teacher2)
    else:
        count += 1
        username = first + last[0:count]
        print("suggest username : " + username)
        choice = input("Confiirm press c : ")
        if (choice == 'c'):
            firebase.put('Teachers', username, teacher2)

def checkUsername(username):
    if(username in teachers):
        print("username is already exist")
        return 0
    return 1

createAcount('Veera','Boonjing','VeeraB')











import random
"""
s = "math123"
subject = ""
year = ""
for i in range(len(s)):
    if not (s[i].isdigit()):
        subject += s[i]
    else:
        year += s[i]

print(subject)
print(year)
"""
'''
from firebase import firebase


def getSubject(subId):
    subject =""
    for i in range(len(subId)):
        if not (subId[i].isdigit()):
            subject += subId[i]
    return subject

db = firebase.FirebaseApplication('https://test-982ab.firebaseio.com/')

questions = db.get('/PendingQuestions',None)


subject = "Mathematics"
q = []

for x in questions :
    s = (getSubject(questions.get(x).get('subId')))
    if(subject == s):
        q.append(questions.get(x))

print(q)


a = 1
b = 5
x = []
for i in range(4):
    y = (random.randint(a,b))
    if(y not in x):
        i -= 1
    x.append(y)

print(x)

'''


'''
        self.q = []
        for x in self.questions:
            if self.subject == self.getSubject(self.db.get('/PendingQuestions/'+x+'/subId',None)):
                self.q.append(self.questions.get(x))

        self.showSomething()
        print(self.q)
'''
a = 0
b = 4
x = []
for i in range(3):
    y = (random.randint(a,b))
    if(y not in x):
        i -= 1
    x.append(y)

print(x)

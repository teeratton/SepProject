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






'''
        self.q = []
        for x in self.questions:
            if self.subject == self.getSubject(self.db.get('/PendingQuestions/'+x+'/subId',None)):
                self.q.append(self.questions.get(x))

        self.showSomething()
        print(self.q)
'''


class question():
    def __init__(self,subId,question, ansA,ansB,ansC,ansD,correctAns, level , quesID,teacherUsername):
        self.question = question
        self.ansA = ansA
        self.ansB = ansB
        self.ansC = ansC
        self.ansD = ansD
        self.correctAns = correctAns
        self.questionId = quesID
        self.subId = subId
        self.teacherUsername = teacherUsername
        self.level = level



    def getQuestion(self):
        return self.question

    def getansA(self):
        return self.ansA

    def getansB(self):
        return self.ansB

    def getansC(self):
        return self.ansC

    def getansD(self):
        return self.ansD

    def getCorrectAns(self):
        return self.correctAns

    def getQuestionId(self):
        return self.questionId

    def getSubId(self):
        return self.subId

    def getTeacherUsername(self):
        return self.teacherUsername

    def getLevel(self):
        return self.level

    def setQuestion(self,question):
        self.question = question

    def setansA(self, ansA):
        self.ansA = ansA

    def setansB(self,ansB):
        self.ansB = ansB

    def setansC(self,ansC):
        self.ansC = ansC

    def setansD(self,ansD):
        self.ansD = ansD

    def setCorrectAns(self,correctAns):
        self.correctAns = correctAns

    def setQuestionId(self,quesId):
        self.questionId = quesId

    def setSubId(self,subId):
        self.subId = subId

    def setTeacherUsername(self,teacherUsername):
        self.teacherUsername = teacherUsername

    def setLevel(self,level):
        self.level = level

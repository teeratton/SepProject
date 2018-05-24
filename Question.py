class Question():
    def __init__(self,question, ansA,ansB,ansC,ansD,rightAns, quesID, courseID)
        self.question = question
        self.ansA = ansA
        self.ansB = ansB
        self.ansC = ansC
        self.ansD = ansD
        self.rightAns = correctAns
        self.questionId = quesID
        self.courseId = courseID

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

    def getRightAns(self):
        return self.rightAns

    def getQuestionId(self):
        return self.questionId

    def getCourseId(self):
        return self.courseId

    def setQuestion(self,question):
        self.question = question

    def setansA(self, ansA):
        self.ansA = ansA

    def setansB(self,ansB):
        self.ansB = ansB

    def setansC(self):
        self.ansC = ansC

    def setansD(self):
        self.ansD = ansD

    def setRightAns(self,rightAns):
        self.rightAns = rightAns

    def setQuestionId(self,quesId):
        self.questionId = quesId

    def setCourseId(self,courseId):
        self.courseId = courseId

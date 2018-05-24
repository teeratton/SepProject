class teacher:
    def __init__(self,first,last,username,password,subjects):
        self.first = first
        self.last = last
        self.username = username
        self.password = password
        self.subjects = subjects

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getSubjects(self):
        return self.subjects

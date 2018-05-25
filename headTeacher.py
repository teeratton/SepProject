class teacher:
    def __init__(self,first,last,username,password,subject):
        self.first = first
        self.last = last
        self.username = username
        self.password = password
        self.subject = subject

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getSubject(self):
        return self.subject


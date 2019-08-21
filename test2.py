class cat:
    def __init__(self,gender):
        self.gender = gender
    def classification(self):
        print("cat gender is {}".format(self.gender))

mark = cat("female")
mark.classification()
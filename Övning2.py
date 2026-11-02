def InNum():
    while True:
        try:
            return int(input("Ditt val:"))
        except:
            print("ogilltig input")

class Question:
    def __init__(self, question, ansOpt1, ansOpt2, ansOpt3, correctAns):
        self.question = question
        self.ansOpt1 = "1:" + ansOpt1
        self.ansOpt2 = "2:" + ansOpt2
        self.ansOpt3 = "3:" + ansOpt3
        self.correctAns = correctAns

    def compare(self):
        return InNum() == self.correctAns

    def printQuestion(self):
        print(self.question)
        print(self.ansOpt1)
        print(self.ansOpt2)
        print(self.ansOpt3)

    def runQuestion(self):
        self.printQuestion()
        if self.compare():
            print("Rätt")
        else:
            print("Fel")

questions = [
    Question("Vad är sveriges huvudstad?", 
             "Oslo",
             "Stockholm",
             "Köpenhamn",
             2)
]

questions[0].runQuestion()
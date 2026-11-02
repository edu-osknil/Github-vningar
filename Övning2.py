import random as rand

totalQuestions = 0
rightQuesses = 0

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
        global totalQuestions
        totalQuestions += 1
        self.printQuestion()
        if self.compare():
            print("Rätt")
            global rightQuesses
            rightQuesses+=1
        else:
            print(f"Fel rätt svar var alternativ {self.correctAns}")

questions = [
    Question("Vad är sveriges huvudstad?", 
             "Oslo",
             "Stockholm",
             "Köpenhamn",
             2),
    Question("Vilket år började andra världskriget?",
             "1914",
             "1939",
             "1945",
             2),
    Question("Vilken huvudstad har Norge?",
             "Oslo",
             "Bergen",
             "Trondheim",
             1)
]

def runQuiz():
    while True:
        questions[rand.randint(0, len(questions) - 1)].runQuestion()
        print(f"Du har haft {rightQuesses} / {totalQuestions} rätt")
        while (True):
            action = input("Fortsätt? y/n: ")
            if action.lower() == 'y':
                break
            elif action.lower() == 'n':
                return
            else:
                print("ogilltig handling")

runQuiz()
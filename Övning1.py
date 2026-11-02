import random as rand

ansNum = rand.randint(1,10)

print(f"Hej {input("Vad heter du?\n")}.")

def InNum():
    while True:
        try:
            return int(input("Gissa ett tal mellan 1 och 10: "))
        except:
            print("ogilltig input")

guessNum = InNum()
if guessNum == ansNum:
    print("rätt")
else:
    print(f"fel det var {ansNum}")
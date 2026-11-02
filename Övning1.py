import random as rand

ansNum = rand.randint(1,10)
guesses = 3

print(f"Hej {input("Vad heter du?\n")}.")

def InNum():
    while True:
        try:
            return int(input("Gissa ett tal mellan 1 och 10: "))
        except:
            print("ogilltig input")


for i in range(guesses):
    guessNum = InNum()
    if guessNum == ansNum:
        print("rätt.")
        break
    else:
        print(f"fel {guesses - i - 1} gissningar kvar.")
        if i == guesses - 1:
            print(f"Svaret var {ansNum}")
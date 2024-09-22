print("welcome to quiz play game")
playing = input("do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay! lets play :)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect! the correct answer is central processing unit.")
      
answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect! the correct answer is power supply unit.")

answer = input("what does GPU stand for? ")
if answer.lower() == "Graphic processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect! the correct answer is Graphic processing unit.")

answer = input("what does RAM stand for? ")
if answer.lower() == "Random Access Memory":
    print("correct!")
    score += 1
else:
    print("incorrect! the correct answer is Random Access Memory.")

print("you got  " + str(score) + " questions correct!")
print("you got  " + str((score /4 )*100) + "%.")
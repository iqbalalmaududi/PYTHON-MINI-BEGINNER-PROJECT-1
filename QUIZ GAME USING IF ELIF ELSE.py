print("welcome to the game")

quiz1 = input("play the game? ")
score = 0
if quiz1 == "yes":
    print("lets play")

if quiz1 == "no":
    quit()

jawab1 = input("apakah saya ganteng? " )
if jawab1 == "mantab":
    print("jawaaban benar")
    score = score + 1
else:
    print("jawaban salah")
    score = score -1

jawab1 = input("apakah saya orang? " )
if jawab1 == "iya":
    print("jawaaban benar")
    score = score + 1
else:
    print("jawaban salah")
    score = score - 1

jawab1 = input("apakah anda jelek? " )
if jawab1 == "banget":
    print("jawaaban benar")
    score = score + 1
else:
    print("jawaban salah")
    score = score - 1

jawab1 = input("apakah saya kaya? " )
if jawab1 == "betul":
    print("jawaaban benar")
    score = score + 1
else:
    print("jawaban salah")
    score = score - 1

jawab1 = input("apakah kamu bisa? " )
if jawab1 == "bisa":
    print("jawaaban benar")
    score = score + 1
else:
    print("jawaban salah")
    score = score - 1
print("anda mendapatkan nilai " + str(score/5*100) + " persen")

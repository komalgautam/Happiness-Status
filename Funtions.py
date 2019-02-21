def details():
   name = input("Hello! What's your name?")
   age =  input("What's your age?")
   place =("Where do you live?")
   status = input("Are you happy right now? YES/NO")
   if status == "YES" :
        status1 = input("Are you sure? Don't be shy. YES/N0")
        if status1 == "YES" :
            print("Perfect! Keep smiling. :)")
        elif status1 == "NO" :
            print("It's Ok! Be positive , everything will fall in place soon.")
        else :
            print("Wrong input")
   elif status == "NO" :
        status2 = input("Wanna share what's wrong? YES/NO")
        if status2 == "YES" :
            share = input("Great! I'm all ears. Go on..")
            print("I understand! Just have faith and be positive. Everythimg will fall into place soon")
        elif status2 == "NO":
            print("I understand. Just believe in yourself. Everything will fall into place soon.")
        else :
            print(":/")
   else :
        print("wrong input")

details()



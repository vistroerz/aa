print("Give your answer Yes or No")
age = input("Are you a cigarette addict older than 75 years old?")
chronic = input("Do you have a severe chronic disease?")
immune = input("Is your immune system too weak?")

if (age and chronic and immune) == "Yes" :
    results = True
    print("You are in risky group")
else : 
    results = False
    print("You are not in risky group")

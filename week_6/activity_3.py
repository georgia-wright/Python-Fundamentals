# five separate questions, multiple choice

# correct - add 5
#incorrect - minus 2
# counter of points

# display total

score = 0
from colorama import Back, Fore, Style


#Q1
print("What is the capital of Canada?")
answer1 = input("A)Vancouver, B)Ottawa, C)Toronto or D)Quebec City   >  ").capitalize()

if answer1 == "B" or answer1 == "Ottawa":
    print(Fore.GREEN + "Correct!" + Fore.RESET)
    score += 5
else:
    print(Fore.RED + "Unlucky, the correct answer is Ottawa." + Fore.RESET)
    score -= 2

#Q2
print("What is the capital of India?")
answer2 = input("A) New Delhi, B) Mumbai, C) Kolkata or D)Jaipur   >  ").capitalize()

if answer2 == "A" or answer2 == "New delhi":
    print(Fore.GREEN + "Correct!" + Fore.RESET)
    score += 5
else:
    print(Fore.RED + "Unlucky, the correct answer is New Delhi." + Fore.RESET)
    score -= 2

#Q3
print("What is the capital of Afghanistan?")
answer3 = input("A) Herat, B) Ghazni, C) Kandahar or D) Kabul   >   ").capitalize()

if answer3 == "D" or answer3 == "Kabul":
    print(Fore.GREEN + "Correct!" + Fore.RESET)
    score += 5
else:
    print(Fore.RED + "Unlucky, the correct answer is Kabul." + Fore.RESET)
    score -= 2

#Q4
print("What is the capital of South Korea?")
answer4 = input("A) Busan, B) Daegu, C) Incheon or D) Seoul   >   ").capitalize()

if answer4 == "D" or answer3 == "Seoul":
    print(Fore.GREEN + "Correct!" + Fore.RESET)
    score += 5

else:
    print(Fore.RED + "Unlucky, the correct answer is Seoul." + Fore.RESET)
    score -= 2

#Q5 

print("What is the capital of Australia?")
answer4 = input("A) Sydney, B) Canberra, C) Melbourne or D) Perth   >   ").capitalize()

if answer4 == "B" or answer4 == "Canberra":
    print(Fore.GREEN + "Correct!" + Fore.RESET)
    score += 5

else:
    print(Fore.RED + "Unlucky, the correct answer is Canberra." + Fore.RESET)
    score -= 2

print(Fore.CYAN + Back.LIGHTYELLOW_EX + Style.BRIGHT + f"Your total score is {score}.")














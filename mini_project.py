from random import randint as ri
print("******************\nTo exit anytime press enter or give input 'e'\n******************")
user_score = 0
tries = 0
while True:
    user_input = input("Enter a number in 1 to 6: ")
    if user_input == '' or user_input=='e':
        break
    number = int(user_input)
    random_number = ri(1,6)
    if number == random_number:
        user_score += 1
        print("You won the dice. score: ", user_score)
    else:
        print("Better luck next time!")
    tries += 1

print(f"Your total score is {user_score} for {tries} trials")
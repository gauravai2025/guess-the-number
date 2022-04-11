actual_number = 165
attempts = 0
score = 100
# user will get maximum score when he guessesd the number in first attempts.
# maximum score: 99
#ans=input('do you want to play')
while ans==yes:
    attempts += 1        # attempts increment by one
    score -= 1           # score gets decrement by one  after each   attempts.
    guess = int(input("guess the number between 100 and 200:\n"))

    if guess < actual_number:
        print('your number was small')

    elif guess > actual_number:
        print(' your number was high')

    else:
        print(f'you guessed the number in {attempts} attempts') # count the number of attempts in which user will guess the number.
        print(f' your score:{score} ') # calculae the score

        break

print('thanks for playing\nhave a good day!')

input("press any key to exit")
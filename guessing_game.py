import random


number_guess=random.randint(1,100)
attempts=10
def guess_game(attempt):
    
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty=input("Choose,difficulty.Type 'easy' or 'hard':")

    if difficulty == "easy":
        
        print(f"You have {attempt} attempts remaining to guess the number.")
        # is_true=True
        is_running=True
        while is_running:
            guess_answer=int(input("Make a guess: "))
            
            if guess_answer != number_guess:
            # while guess_answer != number_guess:
                attempt-=1
                if guess_answer>number_guess:
                    print(f"You have {attempt} attempts remaining to guess the number.")
                    print('Too high')
                
                if guess_answer < number_guess:
                    print(f"You have {attempt} attempts remaining to guess the number.")
                    print("Too low")
                if attempt==0:
                    is_running =False
                    print("Unfortunately you lost")
            if guess_answer==number_guess :
                print(f"You have {attempt} attempts remaining to guess the number.")
                is_running=False
                print(f"That's correct the number is {number_guess}")
                
        
        return attempt
    if difficulty == "hard":
        
        print(f"You have {attempt-5} attempts remaining to guess the number.")
        # is_true=True
        is_hard=True
        while is_hard:
            guess_answer=int(input("Make a guess: "))
            
            if guess_answer != number_guess:
            # while guess_answer != number_guess:
                attempt=attempt-1
                if guess_answer>number_guess:
                    print(f"You have {attempt-5} attempts remaining to guess the number.")
                    print('Too high')
                
                if guess_answer < number_guess:
                    print(f"You have {attempt-5} attempts remaining to guess the number.")
                    print("Too low")
                if attempt-5==0:
                    is_hard =False
                    print("Unfortunately you lost")
                    print("Reload to play again")
            if guess_answer==number_guess :
                print(f"You have {attempt-5} attempts remaining to guess the number.")
                is_running=False
                print(f"That's correct the number is {number_guess}")
                print("Reload to play again")
        
       

        return attempt
        
            
            
        

                

attempts=guess_game(attempts)
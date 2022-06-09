import random

R = "Rock"
P = "Paper"
S = "Scissors"

choices = [R, P, S ]

computer = random.choice(choices)


user = False
 
while user == False: 
    user = input('pick an option between "R", "P" or "S" ').upper()
    
    # function that prints the player and cpu value
    def printer(playerValue):
      print(f"\nPlayer ({playerValue}): \n CPU ({computer}) ")  
        
       
    if user == "R":
        user = "Rock"
        printer(user) 
    elif user == "P":
        user = "Paper" 
        printer(user)
    elif user == "S":
        user = "Scissors"
        printer(user)
    else:
        print("\nOh No! That's an invalid input. Check your spelling")
        # this is to make sure that the user is asked again to input a value after putting a wrong value
        user = False
        computer = random.choice(choices) 
        
           
            
    

    if user == computer:
        print("It's a tie!")
        
        #setting player back to false so the loop continues
        user = False
        computer = random.choice(choices)
    elif user == "Rock":
        if computer == S:
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! CPU wins!") 
    elif user == "Paper":
        if computer == R:
            print("Paper covers Rock! You win!") 
        else: 
            print("Scissors cuts Paper! CPU wins!")
    elif user == "Scissors":
        if computer == P:
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! CPU wins!")
            
            
            
    

          
    
          
                    
    
    
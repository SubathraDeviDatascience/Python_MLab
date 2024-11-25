import random
def play_game():
  choices = ["rock", "paper", "scissors"]
  #Get user input for their choice
  user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
  # Validate user input
  if user_choice not in choices: 
   print("Invalid choice. Please choose rock, paper, or scissors.")
   return 
  # Computer randomly selects its choice
  computer_choice = random.choice(choices)
  # Display choices
  print(f"\nYou chose: {user_choice}")
  print(f"Computer chose: {computer_choice}\n")
  #Determine the winner
  if user_choice == computer_choice:
   print("It's a tie!")
  elif (
    (user_choice =="rock" and computer_choice == "scissors") or
    (user_choice=="paper" and computer_choice =="rock") or
    (user_choice =="scissors" and computer_choice== "paper")
  ):
   print("You win!")
  else:
   print("Computer wins!")
if __name__=="__main__": 
  play_game()
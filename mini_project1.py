# GUESSING GAME
import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
       user_num = int(input("Guess the number :"))
       if user_num == lucky_num:
          print("YAYY!!\nYOU WON THE GAME\nTHANKS FOR PLAYING")
          break
       elif user_num < lucky_num:
           print("Too Low")
       else :
           print("Too High")
play_game()   



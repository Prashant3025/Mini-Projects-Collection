# Lucky draw program

lucky_num = 353

while True:

  guess_num = int(input("Enter your number: "))

  if guess_num>0:

    if guess_num == lucky_num:

      print("Congratulations! you have won a prize.")

      break

    else:

      print("Better luck next time.") 

  else:

    print("Enter a positive number.")



# Text based game for python by litten1up
# forest adventer
# credit to
#  https://thecodingpie.com/post/make-your-own-text-based-adventure-game-in-python3
# thank you

s=0
def play_again(reason):
  print(reason)
  # convert the player's input to lower_case
  answer = input("play again y, n>").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  elif answer == "test":
    test()
    linux()
  elif "ssh" in answer:
      answer = input("password for stipton7960>").lower()
      if answer == "px21a":
          print("welcome stipton7960")
          answer = input("1, 2, 3, 4>").lower()
          if "1" in answer:
              bear_room()
          elif "2" in answer:
              diamond_room()
          elif "3" in answer:
              monster_room()
          else:
              room()
      else:
        # if user types anything besides "yes" or "y", exit() the program

        print("play the tutral")
        test()        
# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print(reason)
  if "linux" in reason:
      linux()

  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again("\nDo you want to play again? (y or n)")

def room():
   print("you are in a cold room you see a computer to your right")
   answer = input("lit's dev envirment>").lower()
   if "r" in answer:
      print("you log on to the linux computer")
      linux()
   else:
      room()
def echo(text):
    print(text)
def linux():
    answer = input("lit's dev envirment $").lower()
    if answer == "ls":
      print("litten_1up.txt")
      print("env.txt")
      print("passwd")
      print("groups")
      linux()
    elif answer == "cat litten_1up.txt":
        print("35 33 20 36 35 20 36 31 20 36 65 20 32 30 20 35 34 20 36 39 20 37 30 20 37 34 20 36 66 20 36 65")
        linux()
    elif answer == "cat env.txt":
        print("/etc/env")
        linux()
    elif answer == "cat":
      print("must enter file")
      linux()
    elif "ls" in answer:
        print("folder not found")
        linux()
    elif answer == "score":
      print(s)
      linux()
    elif answer == "exit":
      room()
    elif answer == "touch":
      answer = input("make what file $").lower()
      for i in range(100):
            answer = input("line %d\r\n" % (i+1)).lower()
            if answer == "exit":
                linux()
            custom[i]=answer
      linux()

    else:
        print("command not found")
        linux()
# diamond room
def diamond_room():
  # some prompts
  print("\nYou are now in a room filled with diamonds!")
  print("And there is a door too!")
  print("What would you do? (1 or 2)")
  print("1). Take some diamonds and go through the door.")
  print("2). Just go through the door.")

  # take input()
  answer = input(">")

  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die!")
  elif answer == "2":
    # the player won the game
    print("\nNice, you're are an honest man! Congrats you win the game!")
    # activate play_again() function
    play_again("\nTutral done enter *ssh litten1up@ubuntu* password *px21a*")
    s= s+100
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")

# monster room
def monster_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the room of a monster!")
  print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
  print("1). Go through the door silently.")
  print("2). Kill the monster and show your courage!")

  # take input()
  answer = input(">")

  if answer == "1":
    # lead him to the diamond_room()
    diamond_room()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("The monster was hungry, he/it ate you.")
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")


def bear_room():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nThere is a bear here.")
  print("Behind the bear is another door.")
  print("The bear is eating tasty honey!")
  print("What would you do? (1 or 2)")
  print("1). Take the honey.")
  print("2). Taunt the bear.")

  # take input()
  answer = input(">")

  if answer == "1":
    # the player is dead!
    game_over("The bear killed you.")
  elif answer == "2":
    # lead him to the diamond_room()
    print("\nYour Good time, the bear moved from the door. You can go through it now!")
    diamond_room()

  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")
def start():
  # give some prompts.
  print("\nYou are standing in a dark room.")
  print("There is a door to your left and right, which one do you take? (l or r)")

  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to bear_room()
    bear_room()
  elif answer == "credits":
      game_over("litten 1up")
  elif answer == "nix":
      linux()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
    monster_room()

  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")


# start the game
start()

from random import choice

def get_bot_response(user_response):
    happyList = ["That's wonderful!", "Go you! Keep it up!", "These are good vibes"]
    sadList = ["Maybe you should go for a walk!", "A smoothie might cheer you up!", "Sending you positve and happy energy!"]
    mehList = ["*swings bangs over forehead* Yeah I feel that", "sending good vibes"]
    tiredList = ["im right there with you", "does coffee even work anymore?", "make sure you get the attendance code..."]
    excitedList = ["YES SO AM I", "*happy screaming noises*", "EXPLOSIONS AND BACKFLIPS"]

    if user_response == "happy":
        return choice(happyList)
    elif user_response == "sad":
        return choice(sadList)
    elif user_response == "meh":
        return choice(mehList)
    elif user_response == "tired":
        return choice(tiredList)
    elif user_response == "excited":
        return choice(excitedList)
    else:
      print("I know you're feeling something but I cant tell what that is! Try again please :)")

print ("Hi! I am Chat Bot! I am a program designed to see how you are feeling.")
print("Please answer with one of the following! happy, meh, sad, tired, or excited!")

user_response = ""

while True:
  user_response = input("So, how are you feeling?: ")
  if user_response == 'done':
    break
  bot_response = get_bot_response(user_response)
  print(bot_response)

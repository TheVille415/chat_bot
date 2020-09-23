from random import choice

def get_bot_response(user_response):
    happyList = ["That's wonderful!", "Go you! Keep it up!", "These are good vibes"]
    sadList = ["Maybe you should go for a walk!", "A smoothie might cheer you up!", "Sending you positve and happy energy!"]

    if user_response == "happy":
        return choice(happyList)
    elif user_response == "sad":
        return choice(sadList)
    else:
      print("I know you're feeling something but I cant tell what that is!")

print ("Hi! I am Chat Bot! I am a program designed to see how you are feeling.")
print("Are you feeling happy or sad? ")

user_response = ""

while True:
  user_response = input("How are you feeling today?: ")
  if user_response == 'done':
    break
  bot_response = get_bot_response(user_response)
  print(bot_response)

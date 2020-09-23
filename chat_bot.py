import random
print ("Hi! I am Chat Bot! I am a program designed to see how you are feeling.")
user_response = input("Now tell me, are you feeling happy or sad? ")

def get_bot_response(user_response):
    happyList = ["That's wonderful!", "Go you! Keep it up!", "These are good vibes"]
    sadList = ["Maybe you should go for a walk!", "A smoothie might cheer you up!", "Sending you positve and happy energy!"]

    if user_response == "happy" or "Happy":
        print(random.choice(happyList))
    elif user_response == "sad" or "Sad":
        print(random.choice(sadList))

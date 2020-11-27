#question 1.
import random
responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes – definitely", "You may rely on it",
             " As I see it, yes" "Most likely", " Outlook good", "Yes", " Signs point to yes"
             " Reply hazy, try again", " Ask again late", " Better not tell you now", "Cannot predict now",
             "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no",
             "Outlook not so good", "Very doubtful"]
def gamer():
    while "?" not in input("Please ask me any Yes/No question: "):
        print("Please enter a valid question")
    print(random.choice(responses))

def main_gamer():
    gamer()
main_gamer()













import random

def cardchoice():
    input("Woukd you like another card? Type Y for yes, type N for no.")
    if ("Y"):
        return getcard()
    else:
        return "N"

def getcard():
    x = random.randint(1, 10)
    print("You drew",x)
    return x
def usertotal():
    usertotal = getcard()

def who_wins(user, dealer):

    if dealer >= 21 and user >= 21:
        return "Both lose."
    elif dealer == user:
        return "Tie."
    elif dealer >= 21:
        return "You win!"
    elif user >= 21:
        return "Dealer wins."
    elif dealer >= user:
        return "Dealer wins."
    elif user >= dealer:
        return"You win!"


'''
This function will tell us who
if wins:
:param User: The user's card total
:param Dealer: The dealer's card total
'''

def main():
    print ("Welcome to the casino, let's play BlackJack!")
    user = cardchoice()
    user = user + cardchoice()
    print ("You currently have a total of", (user))

if __name__ == '__main__':
    main()
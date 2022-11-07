import random



def getcard():
    x = random.randint(1, 10)
    print("You drew",x)
    return x
def usertotal(current):
    return current + getcard()

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
    current = 0
    current = getcard(current)
    choice = input("Woukd you like another card? Type Y for yes, type N for no.")
    if choice == "y":
        current = getcard(current)
    else:
        return "N"
    def
    user = cardchoice()
    user = user + cardchoice()
    print ("User currently have a total of", (user))
    user = user + cardchoice()
    print ("User currently have a total of", (user))
    user = user + cardchoice()
    print("User currently have a total of", (user))
    dealer = cardchoice()
    dealer = dealer + cardchoice()
    print("Dealer currently have a total of", (dealer))
    dealer = dealer + cardchoice()
    print("Dealer currently have a total of", (dealer))


if __name__ == '__main__':
    main()


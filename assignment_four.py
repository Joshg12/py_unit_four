import random



def getcard(current):
    x = random.randint(1, 10)
    print(x,"Has been drawn")
    current = current + x
    return current
def usertotal(current):
    return current + getcard()

"""
This code generates a random number for the user and the dealer.
"""

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

def dealertotal(decurrent):
    dealercard = getcard(decurrent)
    print(dealercard)
    return dealercard
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
        print (current)
    else:
        return "N"
    choice = input("Woukd you like another card? Type Y for yes, type N for no.")
    if choice == "y":
        current = getcard(current)
        print(current)
    else:
        return "N"
    choice = input("Woukd you like another card? Type Y for yes, type N for no.")
    if choice == "y":
        current = getcard(current)
        print(current)
    else:
        return "N"
    choice = input("Woukd you like another card? Type Y for yes, type N for no.")
    if choice == "y":
        current = getcard(current)
        print(current)
    else:
        return "N"

    decurrent = 0
    decurrent2 = dealertotal(decurrent)
    print ("The dealer currently has", decurrent2)
    decurrent3 = dealertotal(decurrent2)
    print("The dealer currently has", decurrent3)

    """
    This code manages the dealer's total.
    """
    who_wins()

"""
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
"""

if __name__ == '__main__':
    main()


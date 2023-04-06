import random

Total_money = 1000

A = 1
J = 10
K = 10
Q = 10

def hit(my_cards, deck):
    random_card = random.choice(deck)
    my_cards.append(random_card)
    return my_cards


 
deck = [2,3,4,5,6,7,8,9,10,A,J,K,Q,2,3,4,5,6,7,8,9,10,A,J,K,Q,2,3,4,5,6,7,8,9,10,A,J,K,Q,2,3,4,5,6,7,8,9,10,A,J,K,Q]

my_cards = random.sample(deck, 2)
dealer_cards = random.sample(deck, 2)

for i in dealer_cards:
    if ((dealer_cards[i] + dealer_cards[i + 1]) < 17): # if the first and second card do not add upto 17, we will append another card,
        random_card = random.choice(deck)              # we then check if all three of them add upto 17 or more and then append another if they dont
        dealer_cards.append(random_card)

print(my_cards)
print(dealer_cards) # only print the first card as this is the dealer

if input() == 'hit':
    print(hit(my_cards, deck))






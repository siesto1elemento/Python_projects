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

while sum(dealer_cards) < 17:# until the sum of the dealer cards is less than 17
    random_card = random.choice(deck)# we will keep appending cards to the list
    dealer_cards.append(random_card)

print(my_cards)
print(dealer_cards[0]) # only print the first card as this is the dealer

if input() == 'hit':
    print(hit(my_cards, deck))

print(dealer_cards) # we finally print the dealer cards to see we win or not

if (sum(my_cards) > sum(dealer_cards)) and sum(my_cards) <= 21:
    print('You Win, congratulation')

else:
    print('Dealer wins')







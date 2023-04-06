import random

Total_money = 1000

def hit(my_cards, deck):
    random_card = random.choice(deck)
    my_cards.append(random_card)
    return my_cards


 
deck = [2,3,4,5,6,7,8,9,10,'A','J','K','Q',2,3,4,5,6,7,8,9,10,'A','J','K','Q',2,3,4,5,6,7,8,9,10,'A','J','K','Q',2,3,4,5,6,7,8,9,10,'A','J','K','Q']

my_cards = random.sample(deck, 2)

print(my_cards)
print(hit(my_cards, deck))

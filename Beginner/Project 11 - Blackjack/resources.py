blackjack_logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      `------'                           |__/           
'''

from enum import Enum

class SpecialCards(Enum):
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11

card_stack = [2, 3, 4, 5, 6, 7, 8, 9, 10, SpecialCards.JACK, SpecialCards.QUEEN, SpecialCards.KING, SpecialCards.ACE]

def update_score(cards):
    count_aces = 0
    sum = 0

    for card in cards:
        sum += card.value if type(card) == SpecialCards else card
        if card == SpecialCards.ACE:
            count_aces += 1
            
    while(sum > 21 and count_aces > 0):
        sum -= 10
        count_aces -= 1
    
    return sum

def card_to_str(card):
    if card == SpecialCards.JACK:
        return "JACK"
    elif card == SpecialCards.QUEEN:
        return "QUEEN"
    elif card == SpecialCards.KING:
        return "KING"
    elif card == SpecialCards.ACE:
        return "ACE"
    else:
        return str(card)

def cards_to_str(cards):
    retstr = "["

    for i in range(len(cards)):
        retstr += card_to_str(cards[i])
        if i != len(cards) - 1:
            retstr += ", "
        
    return retstr + "]"
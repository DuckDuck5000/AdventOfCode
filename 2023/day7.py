import collections
def calculate_hand_score(hand, game_part=True):
    if game_part == True: 
        hand = hand.replace('J', 'X')

    card_values = ['J23456789TXQKA'.index(card) for card in hand]
    max_hand_type = 0

    
    for rank_char in 'J23456789TQKA':
      
        counter = collections.Counter(hand.replace('J', rank_char))
        pattern = tuple(sorted(counter.values()))


        ## adding (5,) for 5 of a kind due to joker
        hand_types = [(1,1,1,1,1), (1,1,1,2), (1,2,2), (1,1,3), (2,3), (1,4), (5,)]
        hand_type = hand_types.index(pattern)
        max_hand_type = max(max_hand_type, hand_type)
      
    return (max_hand_type, card_values)

def calculate_total_winnings(lines, game_part):
    hands = sorted((calculate_hand_score(hand, game_part), int(bid)) for hand, bid in (line.split() for line in lines))
    total = sum((index + 1) * bid for index, (_, bid) in enumerate(hands))
    return total


with open("input.txt") as file:
    lines = [line.strip() for line in file if line.strip()]

total_part1 = calculate_total_winnings(lines, True)
total_part2 = calculate_total_winnings(lines, False)

print(total_part1, total_part2)

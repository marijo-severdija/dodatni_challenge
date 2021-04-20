import random

cards_special = {
    "ace": [1, 11],
    "jack": 12,
    "queen": 13,
    "king": 14,
}

cards_list = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]

player_list = []
comp_list = []
player_sum = 0
comp_sum = 0
hand = ""

def random_card():
    card = random.choice(cards_list)
    return card

def card_value(card):
    if isinstance(card, str):
        if card == "ace":
            card = int(cards_special["ace"][1])
        else:
            card = int(cards_special[card])
    return card


game = input("Do you want to start blackjack play? (y/n): ")
while game.lower() == "y":
    p1 = random_card()
    p2 = random_card()
    player_list.append(p1)
    player_list.append(p2)
    print(f"player hand: {player_list}")

    p1 = card_value(p1)
    p2 = card_value(p2)
    player_sum = p1 + p2
    if player_sum > 22 and p1 == 11:
        p1 = 1
        player_sum = p1 + p2
    elif player_sum > 22 and p2 == 11:
        p2 = 1
        player_sum = p1 + p2
    print(f"player sum: {player_sum}")

    c1 = random_card()
    c2 = random_card()
    comp_list.append(c1)
    comp_list.append(c2)
    print(f"\ncomp hand: [{c1}, ?]")

    if player_sum == 21:
        print("player won!!!")
    elif player_sum > 21:
        print("player lost...")
    else:
        while hand != "n":
            hand = input("do you want another card? (y/n): ")
            if hand.lower() == "y":
                new_card = random_card()
                player_list.append(new_card)
                print(f"player hand: {player_list}")

                new_card = card_value(new_card)
                player_sum += new_card
                if player_sum > 22 and "ace" in player_list:
                    new_card = 1
                    player_sum = player_sum - 11 + new_card

                print(f"player sum: {player_sum}")
                if player_sum > 21:
                    print("player lost...")
                    break
                elif player_sum == 21:
                    print("player has 21!")
            if hand.lower() == "n":
                print(f"comp hand: {comp_list}")
                c1 = card_value(c1)
                c2 = card_value(c2)
                comp_sum = c1 + c2
                print(f"comp sum: {comp_sum}")
                if comp_sum > 21:
                    print("comp lost...")
                    break
                elif comp_sum == 21:
                    print("comp won!!!")
                    break
                elif comp_sum > player_sum:
                    print("comp won!!!")
                    break
                else:
                    while comp_sum < 21 or comp_sum < player_sum:
                        new_card = random_card()
                        comp_list.append(new_card)
                        print(f"comp hand: {comp_list}")

                        new_card = card_value(new_card)
                        comp_sum += new_card
                        if comp_sum > 22 and "ace" in comp_list:
                            new_card = 1
                            comp_sum = comp_sum - 11 + new_card

                        print(f"comp sum: {comp_sum}")
                        if comp_sum > 21:
                            print("comp lost...")
                            break
                        elif comp_sum == 21:
                            print("comp won!!!")
                            break
                        elif comp_sum < 22 and comp_sum > player_sum:
                            print("comp won!!!")
                            break

    game = input("do you want to play again? (y/n): ")
    if game.lower() == "n":
        break
    if game.lower() == "y":
        comp_list.clear()
        player_list.clear()
        hand = ""

import src.art as art
import random

# start the game
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game():
    # more_card = False
    print("Welcome to blackjack game")
    print("\n")
    print(art.logo)
    print("\n\n\n")

    black_jack = False
    end_game = False
    user_cards_list = []
    computer_cards_list = []

    user_current_score = 0
    computer_current_score = 0

        # choose a 2 random cards from the card list for user
    user_card = int(random.choice(card_list))
    user_current_score += user_card
    user_cards_list.append(user_card)
    user_card = int(random.choice(card_list))
    user_current_score += user_card
    user_cards_list.append(user_card)

        # choose a 2 random cards from the card list for computer
    computer_card = int(random.choice(card_list))
    computer_current_score += computer_card
    computer_cards_list.append(computer_card)
    computer_card = int(random.choice(card_list))
    computer_current_score += computer_card
    computer_cards_list.append(computer_card)

    while end_game == False:
        # if more_card == True :
        #     user_card = int(random.choice(card_list))
        #     user_current_score += user_card
        #     user_cards_list.append(user_card)

        # use for loop to shorten the line of code

        # display to the user their card list, their score and computer's first card
        print(f"Your cards: {user_cards_list} current score: {user_current_score}")

        print(f"Computer's first card: {computer_cards_list[0]}")

        # Another way
        # print(f"Computer's first card: {computer_cards_list[0]}")

        # check if the user or computer get blackjack without the need to get another card
        if user_current_score == 21 and len(user_cards_list) == 2:
            print("You got a blackjack, you win!")
            print(f"computer's final hand: {computer_cards_list}, final score: {computer_current_score}")
            black_jack = True
            break
           

        if computer_current_score == 21 and len(computer_cards_list) == 2:
            print(f"computer's final hand: {computer_cards_list}, final score: {computer_current_score}")
            print("Computer got a blackjack, you lose!")
            black_jack = True
            break
            

        # check if the user score is greater than 21 -> the user loses immediately
        if user_current_score > 21 and computer_current_score <= 21:
            print(f"computer's final hand: {computer_cards_list}, final score: {computer_current_score}")
            print("A bust. You lose!")
            break
            
            

        if black_jack == False :
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            # usder don't get more cards
            if user_choice == "n":
                print(f"your final hand: {user_cards_list}, final score: {user_current_score}")

                # if the computer current score < user current score, the computer get a card
                while computer_current_score < user_current_score:
                    computer_card = int(random.choice(card_list))
                    computer_cards_list.append(computer_card)
                    computer_current_score += computer_card

                print(f"computer's final hand: {computer_cards_list}, final score: {computer_current_score}")

                # check if the user score and computer score are both greater than 21 ||  equal -> it's a draw
                if (user_current_score > 21 and computer_current_score > 21) :
                    print("It's a draw")
                    
                    
                # check if the computer score is greater than 21 -> the computer loses immediately
                elif user_current_score <= 21 and computer_current_score > 21 :
                    print("You win!")
                    
                elif user_current_score < computer_current_score :
                    print("Your score is lower than computer's. You lose!")                
                # check if the computer score is equal to user score -> it's a draw
                elif user_current_score == computer_current_score :
                    print("It's a draw")
                else : #user score < 21 and computer score < user score
                    print("You win")

                    

                # print(f"computer's final hand: {computer_cards_list}, final score: {computer_current_score}")
                break

            if user_choice == 'y':
                # more_card = True 
                new_card = int(random.choice(card_list))
                user_cards_list.append(new_card)
                user_current_score += new_card
                print(f"your new card: {new_card}, your new hand: {user_cards_list}, new score: {user_current_score}")

        # Ask the user to replay the game
    user_replay = input("\n\nType 'y' to play again, type 'n' to quit: ")
    if user_replay == 'n':
        end_game = True
        print("Thanks for playing!")
    else :
        print("\n\nNew Round\n\n")
        game()

game()

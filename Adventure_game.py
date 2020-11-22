#Developer: Melinda Eades
#Date: Oct 21, 2020
#Program: Adventure Project

#Imports used:
import time
import sys
import random
from random import choice

#Functions used:
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and purple wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
    print_pause("You hear that she likes games of chance and if you beat her she will give you a magical sword.")
    print_pause("If not, well it won't end well.")
    print_pause("You are a little nervous because you are from the coast and all you have is a shrimp fork to defend yourself.")
    print_pause("You notice a runned down cottage in the middle of the field surrounded by an overgrown garden.")
    print_pause("You can either check out the cottage or the overgrown garden.")

def game_over():  
    print("Game Over!")

def path():
    path = input("If you want to explore the cottage select '1'. If you want to explore the overgrown garden select '2'.")
    if path == '1':
        print_pause("Well grab that shrimp fork and let us check out the cottage!")
        cottage()
    elif path == '2':
        print_pause("Well grab that shrimp fork and let us check out the overgrown garden!")
        garden()   
    else:
        valid_path = input("If you want to explore the cottage select '1'. If you want to explore the overgrown garden select '2'.")
        while True:
            if '1' in valid_path:
                cottage()
            elif '2' in valid_path:
                garden()
            else:
                print_pause('Please select a valid option:')
            return valid_path

def cottage():
    cottage = input("You walk towards the cottage. To go up the stairs select '1'. Otherside run away by entering anything else.")
    if cottage == '1':
        print_pause("You slowly ascend the rickety stairs to the cottage.")
        print_pause("You knock on the door very lightly.")
        print_pause("The fairie opens the door and scowls. 'How dare you disturb me during my Netflix binge?'")
        coin_flip_cottage()
    else:
        print_pause("After brief consideration, you realize the risks outweigh the rewards.")
        print_pause("Better safe than sorry. You decide to 'nope' it on out of there.")
        print_pause("You take your shrimp fork and escape this place before you are caught and it costs you your life.")
        play_again()

def coin_flip_cottage():
    print_pause("'Are you here to flip a coin for a chance to win a magical sword with a game of chance?'")
    print_pause("'She says in a menacing tone before you answer...'")
    print_pause("'You need to know before you decide that once you peer at the result there is no escaping your fate.'")
    print_pause("'If it is 'Heads' you win. If it is 'Tails' you lose. Otherwise, you can run away.'")
    coin_flip = input("'So what's your decision? Will you flip the coin? 'Yes' or 'No'? Otherside run away by entering anything else.'")
    if coin_flip.lower().startswith('y'):
        print_pause("'Well it is your funeral.'")
        print_pause("You flip the coin and wait for what seems like an eternity for it to land.")
        time.sleep(2.75)
        print_pause("You sense you are trembling with fear as you look at the coin.")
        cottage_coin = random.choice(['Heads', 'Tails'])
        if cottage_coin == 'Heads':
            print_pause("It is Heads! Congratulations! You won!")
            print_pause("The fairie says 'take your magical sword and leave me to my Netflix before I cast a spell on you'.")
            print_pause("The fairie tosses you the sword and slams the door in your face.")
            print_pause("Stunned, you look down and in your grasp is a gleaming magical sword with a bright shiny jewel on top.") 
            print_pause("Now that you have won you are no longer dependent on a shrimp fork for your safety!")
            play_again()
        else:
            print_pause("It is Tails. Oh no! You lost!")
            print_pause("The wicked fairie says you are a loser and casts an evil spell on you for disturbing her Netflix binge.")
            print_pause("You are doomed for all eternity to binge watch the Tiger King and Cheer shackled in her cottage")
            play_again()
    else:
        print_pause("Well since she put it that way, you decide you will pass.")
        print_pause("Over your shoulder you say 'have a nice day fairie!', you decide to 'nope' it on out of there quickly.")
        print_pause("You take your shrimp fork and escape this place before she decides to cast an evil spell on you.")
        play_again()

def garden():
    garden = input("You head towards the overgrown garden. To go into the garden select '2'. Otherside run away by entering anything else.")
    if garden == '2':
        print_pause("You decide to search the overgrown garden for any weapons.")
        print_pause("You find a rusty sword tangled in a vine that contains a dull jewel.")
        print_pause("Next to it there is a coin and a scroll.")
        print_pause("You read the scroll and it says that the sword will become magical if the coin is flipped and lands on heads...")
        print_pause("However, it warns that if the coin lands on tails the fairie will hear you and cast an evil spell on you.")
        coin_flip_garden()
    else:
        print_pause("After brief consideration, you realize the risks outweigh the rewards.")
        print_pause("Better safe than sorry. You decide to 'nope' it on out of there.")
        print_pause("You take your shrimp fork and escape this place before you are caught and it costs you your life.")
        play_again()

def coin_flip_garden():
    print_pause("You need to know before you decide that once you peer at the result there is no escaping your fate.")
    print_pause("If it is 'Heads' you win. If it is 'Tails' you lose. Otherside run away by entering anything else.")
    coin_flip = input("So what is your decision? Will you flip the coin? 'Yes' or 'No'? Otherside run away by entering anything else.")
    if coin_flip.lower().startswith('y'):
        print_pause("Well it is your funeral.")
        print_pause("You flip the coin and wait for what seems like an eternity for it to land.")
        time.sleep(2.75)
        print_pause("You notice you are trembling as you look at the coin.")
        garden_coin = random.choice(['Heads', 'Tails'])
        if garden_coin == 'Heads':
            print_pause("It is Heads! The vine releases the sword.")
            print_pause("The rust falls away revealing a gleaming magical sword with a bright shiny jewel on top.")
            print_pause("Congratulations! You won!") 
            print_pause("Take the magical sword you won and leave without disturbing the fairie and her Netflix binge.")
            print_pause("Now that you have won you are no longer dependent on a shrimp fork for your safety!")
            play_again()
        else:
            print_pause("It's Tails! Oh no! You lost. The wicked fairie hears you rustling in the garden.")
            print_pause("She casts an evil spell on you for disturbing her Netflix binge.")
            print_pause("You are now doomed for all eternity to binge watch the Tiger King and Cheer shackled in her cottage")
            play_again()
    else:
        print_pause("Better safe than sorry.")
        print_pause("You take your shrimp fork and escape this place before you are caught and it costs you your life.")
        play_again()

def play_again():
    play_again = input("Would you like to play again? 'Yes' or 'No'.")
    if play_again.lower().startswith('y'):
        print_pause("Ok! Let's do it.") 
        play_game()
    elif play_again.lower().startswith('n'):   
        print_pause("Ok. Good idea. Better to take your shrimp fork and live to fight another day. Goodby!")
        sys.exit()
    else:
        print_pause("Indecision is not your friend. Goodby!")
        play_again()

def play_game():
    intro()
    path()
    cottage()
    coin_flip_cottage
    garden()
    coin_flip_garden
    play_again()
    game_over()

play_game()
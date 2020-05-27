import time
import random

gold = 0
gear = []
location = ''
locations_visited = []
state_of_mind = 'normal'


def print_pause(to_print):  # delay printing of text by one second
    print(to_print)
    time.sleep(1)


def welcome_message():  # welcome players to the game
    print_pause('Welcome to Adventureland!')
    print_pause('Currently, Adventureland is terrorized by an awful demon '
                'that you must defeat')
    print_pause('You stare across a vast wilderness')
    print_pause('At the end of the clearing are a spooky hut '
                'and a decrepit old townhouse')


def restart_game():  # at completion, give player a choice to restart the game
    choice = input('Would you like to play again? Enter yes or no\n')
    if choice.lower() == 'yes':
        welcome_message()
    elif choice.lower() == 'no':
        print_pause('Thanks for playing!')
        exit()
    else:
        print("I don't understand your response. You must enter yes or no.\n")
        restart_game()


def be_brave():
    global state_of_mind
    brave = input('Are you brave enough to carry on? Enter yes or no.\n')
    if brave.lower() == 'yes':
        print_pause('The gods applaud your bravery')
        state_of_mind = 'normal'
        opening_decision()
    elif brave.lower() == 'no':
        print_pause('Thanks for playing!')
        exit()
    else:
        print_pause("The fear may have paralyzed you "
                    "but that is not a valid choice.")
        be_brave()


def hut_perimeter():
    print_pause('As you scope things out, you catch a shimmer of light '
                'off something on the ground')
    print_pause('Do you?')  # may need glimmer_choice function too
    glimmer_choice = input("1. Pick it up\n"
                           "2. Ignore it\n")
    if glimmer_choice == '1':
        print_pause('You dust off the object and find a gleaming dagger!')
        gear.append('dagger')
        print_pause('You resume your inspection and '
                    'come back to the front of hut')
        hut_choice()
    elif glimmer_choice == '2':
        print_pause('You continue to scope out the exterior, '
                    'eventually returning to the front of the hut')
        hut_choice()
    else:
        print_pause('Sorry, you have to take some kind of action.\n')
        hut_perimeter()


def hut_choice():
    global location
    global gear
    global state_of_mind
    global location
    global locations_visited
    location = 'hut'
    locations_visited.append('hut')
    print_pause('What do you want to do next?')
    choice = input("1. Knock on the door\n"
                   "2. Scout the perimeter\n"
                   "3. Return to the clearing\n")
    if choice == '1':
        witch_doctor_knock()
    elif choice == '2':
        print_pause('You walk around the exterior of the hut')
        hut_perimeter()
    elif choice == '3':
        field_free()
    else:
        print_pause('Please make a valid choice\n')
        hut_choice()


def witch_doctor_knock():
    global location
    global gear
    global state_of_mind
    global gold
    print_pause('You knock on the door')
    print_pause('The witch doctor opens it and invites you in!')
    print_pause('What do you do?')
    enter_choice = input("1. Follow him into the house\n"
                         "2. Bid him farewell\n")
    if enter_choice == '1':
        print_pause('The witch doctor brews you a '
                    'steaming mug of chamomile tea')
        print_pause('You strike up a conversation and '
                    'he offers you a protection charm')
        print_pause('You humbly accept and thank him for the generosity, '
                    'then walk out of the hut')
        field_free()
    elif enter_choice == '2':
        witch_doctor_state = random.choice(['happy', 'mad'])
        if witch_doctor_state == 'happy':
            print_pause('The witch doctor waves you off with a smile')
            field_free()
        elif witch_doctor_state == 'mad' and 'dagger' in gear:
            print_pause('The witch doctor raises a ghoul '
                        'that chases you out of the house!')
            print_pause('Luckily, you have your dagger!')
            print_pause('You stab the ghoul and it dissipates into the ether')
            print_pause('The witch doctor is impressed by your bravery '
                        'and hands you 500 gold pieces')
            gold += 500
            print_pause('You bid farewell to the witch doctor and '
                        'head back out to the clearing')
            opening_decision()
        elif witch_doctor_state == 'mad' and 'dagger' not in gear:
            lucky_draw = random.choice(['lucky', 'unlucky'])
            if lucky_draw == 'lucky':
                print_pause('The witch doctor raises a ghoul that '
                            'chases you out of the hut!')
                state_of_mind = 'scared'
                field_free()
            else:
                print_pause('The witch doctor raises a ghoul that chases you '
                            'out of the hut and consumes you!')
                dead_game()
        else:
            print_pause('The witch doctor looks at you puzzled. '
                        'Make a valid choice.\n')
            hut_choice()
    else:
        print_pause('The witch doctor looks at you puzzled. '
                    'Make a valid choice.\n')
        witch_doctor_knock()


def house_choice():
    global location
    global gear
    global state_of_mind
    global gold
    global locations_visited
    location = 'house'
    locations_visited.append('house')
    print_pause('What do you want to do next?')
    choice = input("1. Go through the door\n"
                   "2. Scout the perimeter\n"
                   "3. Return to the clearing\n")
    if choice == '1':
        print_pause('You open the creaky door slowly')
        print_pause('You see stairs leading up to the attic '
                    'and down to the basement')
        demon_door()
    elif choice == '2':
        print_pause('You walk around the exterior of the house')
        house_perimeter()
    elif choice == '3':
        field_free()
    else:
        print_pause('Please make a valid choice\n')
        house_choice()


def demon_door():
    global gear
    global state_of_mind
    global gold
    global locations_visited
    print_pause('Where do you go?')
    enter_choice = input("1. Head upstairs\n"
                         "2. Head downstairs\n"
                         "3. Head back to the clearing\n")
    if enter_choice == '1':
        locations_visited.append('upstairs')
        print_pause('You ascend the stairs into the attic bravely')
        print_pause('At the top, a gnome stands guard over '
                    'a large treasure chest')
        gnome_choice()
    elif enter_choice == '1' and 'upstairs' in locations_visited:
        print_pause('You climb the stairs and find an empty chest')
        print_pause('You return to the main floor')
        demon_door()
    elif enter_choice == '2':
        locations_visited.append('downstairs')
        print_pause('You creep down the creaky stairs to the basement')
        print_pause('There, in the corner, stands the awful Demon!')
        demon_fight()
    elif enter_choice == '2' and 'downstairs' in locations_visited:
        print_pause('All you find is the corpse of the demon')
        demon_door()
    elif enter_choice == '3':
        field_free()
    else:
        print_pause('Please make a valid choice.\n')
        demon_door()


def gnome_choice():
    global gear
    global state_of_mind
    global gold
    global locations_visited
    print_pause('Do you?')
    gnome_action = input("1. Offer it a bribe\n"
                         "2. Attack it!\n")
    gnome_luck = random.choice(['strong', 'weak'])
    if gnome_action == '1' and gold >= 100:
        print_pause('The gnome takes your bribe of 100 gold '
                    'and hands you the chest')
        gold -= 100
        print_pause('You open the chest and find the Crossbow of Olivantium!')
        gear.append('Crossbow')
        print_pause('You toast the gnome and return to the main floor')
        demon_door()
    elif gnome_action == '1' and gold < 100:
        print_pause('You do not have enough gold to bribe the gnome!')
        print_pause('Enraged, the gnome charges you and pushes '
                    'you down the stairs to your death!')
        dead_game()
    elif gnome_action == '2' and gnome_luck == 'strong' and 'dagger' in gear:
        print_pause('You produce your dagger and stab at the gnome')
        print_pause('Unfortunately, he is too crafty for you '
                    'and turns the dagger on you!')
        dead_game()
    elif gnome_action == '2' and gnome_luck == 'weak' and 'dagger' in gear:
        print_pause('You produce your dagger and stab at the gnome')
        print_pause('You fell the gnome with a swift strike from your dagger')
        print_pause('You kick his corpse to the side and open the chest '
                    'to find the Crossbow of Olivantium!')
        gear.append('Crossbow')
        print_pause('Stepping over the body, you return to the main floor')
        demon_door()
    elif gnome_action == '2' and gnome_luck == 'strong':
        print_pause('You grapple with the gnome')
        print_pause('He overpowers you and throws you out the window!')
        dead_game()
    elif gnome_action == '2' and gnome_luck == 'weak':
        print_pause('You grapple with the gnome')
        print_pause('You gain the upper hand and toss him '
                    'down the stairs to his doom')
        print_pause('You open the chest and find the Crossbow of Olivantium!')
        gear.append('Crossbow')
        print_pause('Stepping over the body, you return to the main floor')
        demon_door()
    else:
        print_pause('The gnome looks at you puzzled. '
                    'You must make a valid choice')
        gnome_choice()


def demon_fight():
    global state_of_mind
    print_pause('What do you do?!')
    demon_choice = input("1. Attack!\n"
                         "2. Bribe Him to leave this land\n"
                         "3. Run away!\n")
    demon_strength = random.choice(['strong', 'weak'])
    if demon_choice == '1' and 'Crossbow' in gear:
        print_pause('The demon charges it at you while you '
                    'ready the Crossbow of Olivantium!')
        print_pause('You put a bolt straight between its eyes')
        print_pause('The demon is dead!')
        won_game()
    elif demon_choice == '1' and demon_strength == 'strong' \
            and 'dagger' in gear:
        print_pause('The demon charges at you!')
        print_pause('You ready your small dagger!')
        print_pause('The demon overpowers you and '
                    'crushes you to death')
        dead_game()
    elif demon_choice == '1' and demon_strength == 'weak' and 'dagger' in gear:
        print_pause('The demon charges at you!')
        print_pause('You ready your small dagger!')
        print_pause('The battle is fierce, sapping all of your energy')
        print_pause('At last, you stab the demon with your small dagger '
                    'and it falls to the ground')
        print_pause('The demon is dead!')
        won_game()
    elif demon_choice == '1' and demon_strength == 'strong':
        print_pause('The demon charges at you!')
        print_pause('You are no match for this overpowering demon!')
        print_pause('The demon overpowers you and crushes you to death')
        dead_game()
    elif demon_choice == '1' and demon_strength == 'weak':
        print_pause('The demon charges at you!')
        print_pause('The battle is fierce, sapping all of your energy')
        print_pause('At last, you are able to throttle the demon '
                    'and it falls dead to the floor')
        print_pause('The demon is dead!')
        won_game()
    elif demon_choice == '2' and gold >= 500:
        print_pause(f"You offer the demon a reward of {gold} "
                    f"gold pieces to leave this land")
        print_pause('The demon pauses to consider your generous offer')
        print_pause('He accepts! Taking the bag of gold, '
                    'he vanishes from sight')
        won_game()
    elif demon_choice == '2' and gold < 500:
        print_pause(f"You offer the demon a reward of {gold} gold "
                    f"pieces to leave this land")
        print_pause('The demon pauses to consider your generous offer')
        print_pause('He laughs at your paultry offering! '
                    'With a swing of his hand, he takes off your head!')
        dead_game()
    elif demon_choice == '3' and demon_strength == 'strong':
        print_pause('You turn to run from the demon')
        print_pause('Before you can climb the stairs, he grabs you!')
        print_pause('In one feel swoop, the demon tears you in two!')
        dead_game()
    elif demon_choice == '3' and demon_strength == 'weak':
        state_of_mind = 'scared'
        print_pause('You turn to run from the demon')
        print_pause('Barely evading his grasp, you escape from the house!')
        field_free()
    else:
        print_pause('The demon is enraged! Make a valid choice.\n')
        demon_fight()


def house_perimeter():
    global gold
    print_pause('As you scope things out, you catch a shimmer of '
                'light off something on the ground')
    print_pause('Do you?')  # may need glimmer_choice function too
    glimmer_choice = input("1. Pick it up\n"
                           "2. Ignore it\n")
    if glimmer_choice == '1':
        print_pause('You dust off the object and find a loose bag of gold!')
        if gold < 600:
            gold += 200
        else:
            gold = 600
            print_pause('You cannot hold any more gold')
        print_pause('You resume your inspection and come back '
                    'to the front of the house')
        house_choice()
    elif glimmer_choice == '2':
        print_pause('You continue to scope out the exterior, eventually '
                    'returning to the front of the house')
        house_choice()
    else:
        print_pause('Sorry, you have to take some kind of action.\n')
        house_perimeter()


def won_game():
    print_pause('You won!')
    print_pause('Do you want to play again?')
    go_again = input("Yes or No?\n")
    if go_again.lower() == 'yes':
        opening_decision()
    elif go_again.lower() == 'no':
        print_pause('Thanks for playing!')
        exit()
    else:
        print_pause('You need to make a valid choice')
        won_game()


def dead_game():
    print_pause('You died!')
    print_pause('Do you want to play again?')
    go_again = input("Yes or No?\n")
    if go_again.lower() == 'yes':
        opening_decision()
    elif go_again.lower() == 'no':
        print_pause('Thanks for playing!')
        exit()
    else:
        print_pause('You need to make a valid choice')
        dead_game()


def field_free():
    global gear
    if state_of_mind == 'normal':
        print_pause('You head back out to the clearing')
        opening_decision()
    else:
        print_pause('You flee to the clearing to avoid danger!')
        be_brave()


def opening_decision():
    print_pause('Where would you like to adventure?')
    first_choice = input("1. Spooky Hut\n"
                         "2. Decrepit Townhouse\n")
    if first_choice == '1':
        print_pause("You approach the hut and see a sign: "
                    "'Here lives the witch doctor'")
        hut_choice()
    elif first_choice == '2':
        print_pause('You approach the house and find the door slightly ajar')
        house_choice()
    else:
        print('No magic wands here; please make a valid choice')
        opening_decision()


welcome_message()

opening_decision()

#Introduction to the Adventure Story Game
import time
import random
import sys

#Slowly print out the text
def type_text(text, delay):
    for char in text:
        print(char, end = "", flush = True) #Print the character without moving to the next line    
        time.sleep(delay) #Parameter is the delay for characters popping up 
    print()  # Move to the next line after the text is printed

#Introduction to the Adventure Story Game
type_text("Welcome to the Fantasy Life!", 0.07)
type_text("Let your name be known: \n", 0.07) 
name = input("Enter your name: ")
#If Name is Blank, ask for the name again
while name == "":
    type_text("Invalid input. Please enter your name: \n", 0.07)
    name = input("Enter your name: ")
#Dialogue for the name
name_dialogue = name + ": "
type_text("\n" + "When you see the text 'What do you want to do?', you will be given a choice to choose from.\n" + "You will be given a number to choose from.\n" + "Please type the number to choose your path.\n" + "Please do not spam or click 'enter' multiple times as it will answer the next question.\n" + "Enjoy the game!\n", 0.07)
type_text("\n" + "\n", 0.07)

#Play again
def play_again():
    type_text("Do you want to play again? (For the King ending, you must run the program again) ", 0.05)
    choice = input("Yes (1)/ No (2): ")
    #Restart the game
    if choice == "1":
        type_text("\n" + "Restarting the game ...\n" + "\n", 0.07)
        start_adventure()
    #Exit the game (the system will exit)
    elif choice == "2":
        type_text("Thank you for playing the Fantasy Life!\n", 0.07)
        sys.exit()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            type_text("Do you want to play again? (For the King ending, you must run the program again) ", 0.05)
            choice = input("Yes (1)/ No (2): ")
            if choice == "1":
                type_text("\n" + "Restarting the game ...\n" + "\n", 0.07)
                start_adventure()
                break
            elif choice == "2":
                type_text("Thank you for playing the Fantasy Life!\n", 0.07)
                sys.exit()

#Secret Ending
def custom_play_again():
    type_text("Do you want to play again? (For the King ending, you must run the program again) ", 0.05)
    choice = input("Yes (1)/ No (2): ")
    #Restart the game
    if choice == "1":
        type_text("\n" + "Restarting the game ...\n" + "\n", 0.07)
        start_adventure()
    #Exit the game (the system will exit)
    elif choice == "2":
        type_text("Thank you for playing the Fantasy Life!\n", 0.07)
        sys.exit()
    elif choice in ["Darkness", "darkness"]:
        type_text("\n" + "You have unlocked the secret ending!\n", 0.07)
        type_text("\n" + "\n" + ". . .\n" + "\n", 0.04)
        darkness_ending()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            type_text("Do you want to play again? (For the King ending, you must run the program again) ", 0.05)
            choice = input("Yes (1)/ No (2): ")
            if choice == "1":
                type_text("\n" + "Restarting the game ...\n" + "\n", 0.07)
                start_adventure()
                break
            elif choice == "2":
                type_text("Thank you for playing the Fantasy Life!\n", 0.07)
                sys.exit()
            elif choice in ["Darkness", "darkness"]:
                type_text("\n" + "You have unlocked the secret ending!\n", 0.07)
                type_text("\n" + "\n" + ". . .\n" + "\n", 0.04)
                darkness_ending()

#Start the adventure (Normal game)
def start_adventure():
    type_text(". . .\n", 0.04)
    type_text("You had a peaceful life in the village of Everpeace, until this one day.\n" + "Unknown: Run! The village is under attack!\n" + "Your friend, John, runs towards you.\n" + name_dialogue + "What's happening?\n" + "John: The village is under attack by the Dark Lord's minions!\n" + "John: We need to protect the village. Grab your sword and follow me!\n", 0.04)
    type_text("What do you want to do?: ", 0.05)
    #Choose to follow John or run away
    choice = input("Grab sword and follow John? (1)/ Run away? (2): ")
    if choice == "1":
        fight_path_1()
    elif choice == "2":
        run_path_1()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            type_text("What do you want to do?: ", 0.05)
            choice = input("Grab sword and follow John? (1)/ Run away? (2): ")
            if choice == "1":
                fight_path_1()
            elif choice == "2":
                run_path_1()

#Fight the Dark Lord's minions            
def fight_path_1():
    type_text("\n" + "You grab your sword and looked at John\n" + name_dialogue + "Let's go!\n" + "You and John see the Dark Lord's minions destroying the village.\n" + "John: We need to fight them off!\n" + "You and John fight the minions bravely.\n" + "You see the Dark Lord in the distance, watching the battle.\n" + "John: We need to defeat the Dark Lord!\n" + "Dark Lord's Commander: Not so fast. You will have to go through me first.\n" + "You and John charge towards the Dark Lord's Commander.\n" + "Dark Lord's Commander: You dare challenge me?\n" + "You and John fight the Dark Lord's Commander.\n" + "After a long battle, you and John gets defeated by the Commander.\n" + "The Dark Lord's Commander: You are no match for me!\n" + "You and John are against the wall, unable to move. The blade of the Commander's sword is pointed at your nose.\n" + "The Dark Lord's Commander: You have talent in swordfighting. I might spare your life if you serve our King.\n" + "John: Don't listen to him!\n", 0.04)
    type_text("What do you want to do? ", 0.05)
    choice = input("Serve the Dark Lord's King? (1)/ Fight the Commander? (2): ")
    #Choose to serve the King or fight the Commander
    if choice == "1":
        serve_king()
    elif choice == "2":
        fight_commander()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            type_text("What do you want to do? ", 0.05)
            choice = input("Serve the Dark Lord's King? (1)/ Fight the Commander? (2): ")
            if choice == "1":
                serve_king()
            elif choice == "2":
                fight_commander()

#Run away from the village                
def run_path_1():
    type_text("\n" + name_dialogue + " I can't do this!\n" + "You run away from the village and never look back.\n" + "You hear John's voice yelling your name, but you never return.\n" + "There are 2 ways where you can escape safely. The Ocean and the Forest.\n", 0.04)
    type_text("What do you want to do? ", 0.05)
    choice = input("Escape to the Ocean? (1)/ Escape to the Forest? (2): ")  
    #Choose to escape to the Ocean or the Forest
    if choice == "1":
        escape_ocean()
    elif choice == "2":
        escape_forest()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            type_text("What do you want to do? ", 0.05)
            choice = input("Escape to the Ocean? (1)/ Escape to the Forest? (2): ")
            if choice == "1":
                escape_ocean()
            elif choice == "2":
                escape_forest()

#Serve the Dark Lord's King
def serve_king():
    type_text("\n" + name_dialogue + "I'm sorry, John but I want to live.\n" + "John: " + name + ", please don't do this.\n" + name_dialogue + "It's not personal.\n" + "Dark Lord's Commander: Good choice newcomer, but I hate to say this ... you're first task is to kill your friend.\n", 0.04)
    type_text("What do you want to do? ", 0.05)
    choice = input("Kill John? (1)/ Refuse? (2): ")
    #Choose to kill or refuse the order
    if choice == "1":
        kill_john()
    elif choice == "2":
        refuse_order()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            type_text("What do you want to do? ", 0.05)
            choice = input("Kill John? (1)/ Refuse? (2): ")
            if choice == "1":
                kill_john()
            elif choice == "2":
                refuse_order()

#Fight the Dark Lord's Commander
def fight_commander():
    type_text("\n" + name_dialogue + "I won't serve your kind!\n" + "You grab your sword and hit the Commander's sword.\n" + "Dark Lord's Commander: You will regret this!\n" + "You and John fight the Commander.\n", 0.04)
    type_text("Type the written letter to defeat the Commander: ", 0.05)
    #Sword Fightting Game
    for i in range(7):
        #Choose a random letter
        letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        print(letter)
        guess = input("Enter the letter: ")
        #If the letter is correct
        if guess == letter:
            type_text("Ting! Your sword hits the Commander's sword.\n", 0.04)
        #If the letter is wrong
        else:
            type_text("The Commander's sword hits your sword.\n" + "The Commander strikes again and stabs you in the chest.\n" + "Dark Lord Commander: I told you not to. Hahahaha!\n", 0.04)
            type_text("You have been defeated by the Dark Lord's Commander.\n", 0.04)
            commander_die()
            return
    type_text("You almost defeated the Commander.\n" + "However, a minion comes behind you and stabs you in the back.\n" + "You have been defeated by the Dark Lord's minions.\n", 0.04)
    minion_die()
    return

#Escape to the Ocean
def escape_ocean():
    type_text("\n" + name_dialogue + "I will escape to the Ocean!\n" + "You run towards the Ocean and never look back.\n" + "You reached the cool waters.\n" + "The water tickles your feet.\n" + "You start swimming and swimming.\n" + "You swam for hours but found no nearby islands.\n" + "You start to become tired.\n" + "You stopped swimming due to fatigue.\n", 0.04)
    type_text("You have drowned in the Ocean.\n", 0.04)
    drown_die()
    return

#Escape to the Forest
def escape_forest():
    type_text("\n" + name_dialogue + "I will escape to the Forest!\n" + "You run towards the Forest and never turned back.\n" + "You ran and ran until the village was miles away.\n" + "It started to become dark so you decided to take a break.\n" + "You happened to have a metal key in your pocket.\n" + "You looked around and found some flint.\n" + "You wondered if you should start a fire.\n", 0.04)
    type_text("What do you want to do? ", 0.05)
    choice = input("Start a fire? (1)/ Sleep? (2): ")
    #Choose to start a fire or sleep
    if choice == "1":
        start_fire()
    elif choice == "2":
        sleep_forest()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" or "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            type_text("What do you want to do? ", 0.05)
            choice = input("Start a fire? (1)/ Sleep? (2): ")
            if choice == "1":
                start_fire()
            elif choice == "2":
                sleep_forest()
              
#Kill John
def kill_john():
    type_text("\n" + name_dialogue + "I'm sorry John.\n" + "John: Please don't do this.\n" + "John pleads for his life but you stab him in the chest.\n" + "John falls to the ground, unable to move.\n" + "John: Why?\n" + "Dark Lord's Commander: Good job. You have passed your first task.\n" + "Dark Lord's Commander: Your next task is to kill the village elder.\n" + "You make quick work of the village, leaving no Everpeacian unkilled.\n" + "Dark Lord's Commander: Well done, newcomer. Now tell me your name.\n" + name_dialogue + name + " ... It's " + name + " the Dark Lord's servant.\n" + "Dark Lord Commander: Well said, " + name + ".\n"+ "Dark Lord Commander: Let's head back to the palace.\n" + "...", 0.04)
    type_text("You entered the Dark Lord's palace\n" + "Dark Lord's Commander: We are to meet the Dark Lord and give a brief summary of our kills.\n" + "The Dark Lord's Commander takes off his helmet.\n" + name_dialogue + "What is your name?\n" + "Dark Lord's Commander: Andrew\n", 0.04)
    type_text("Andrew: We need to go now.\n" + "You entered the King's room.\n" + "The room was filled with luxurious jewelry that any man would kill for.\n" + "Dark Lord: Andrew ...\n" + "Andrew bows down\n" + "Andrew: Yes, my lord...\n" + "Dark Lord: Who is this here ... \n" + "Andrew: " + name + ", my lord", 0.04)
    type_text("...\n"+ "Dark Lord: ... How many have you killed?\n" + "Andrew: 50, my lord\n" + "Dark Lord: ... And\n" + "Andrew: " + name + " has killed 100, my lord\n" + "Dark Lord: ... Impressive\n" + "Dark Lord: You have done well, " + name + ".\n" + "You feel regrets and happiness at the same time.\n" + "You started to think whether you should continue to serve the king.\n", 0.04)
    type_text("What do you want to do? ", 0.05)
    choice = input("Continue serving the Dark Lord? (1)/ Refuse? (2): ")
    #Choose to continue serving the King or refuse the order
    if choice == "1":
        continue_serving()
    elif choice == "2":
        refuse_order2()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            type_text("What do you want to do? ", 0.05)
            choice = input("Continue serving the Dark Lord? (1)/ Refuse? (2): ")
            if choice == "1":
                continue_serving()
            elif choice == "2":
                refuse_order2()

#Refuse the order
def refuse_order():
    type_text("\n" + "You throw your sword to the ground.\n" + "Dark Lord's Commander: You fool!\n" + "The Commander stabs you in the chest.\n" + "Dark Lord's Commander: You should have listened.\n" + "You have been defeated by the Dark Lord's Commander.\n", 0.04)    
    commander_die()

#Die from Commander's attack
def commander_die():
    type_text("\n" + "Maybe you should have chosen a more passive path.\n" + "In the end, you knew that you couldn't beat an entire army.\n" + "You just wanted to fight for fun, right?\n" + "\n" + "\n", 0.04)
    play_again()

#Die from minion's attack
def minion_die():
    type_text("\n" + "You thought you were good because the Dark Lord's Commander said so, right?\n" + "You were probably delusional to think that you could beat the Dark Lord's army.\n" + "You were just a mere mortal or maybe ...\n", 0.04)
    play_again()

#Die from drowning
def drown_die():
    type_text("\n" + "You thought you could escape the Dark Lord's army by swimming?\n" + "Who said you can swim for hours without getting tired?\n" + "You are human too you know?\n" + "You should have thought about that before you decided to swim.\n", 0.04)
    play_again()

#Start a fire
def start_fire():
    type_text("\n" + "You decided to start a fire.\n" + "You just have to know how to start one.\n" + "You used the flint to start a fire.\n", 0.04)
    #Randomly choose if the fire is successful or not
    number = random.choice("12")
    if number == "1":
        type_text("You successfully started a fire.\n", 0.04)
        type_text("You decided to sleep for the night after the long day.\n", 0.04)
        forest_fire()
    else:
        type_text("You failed to start a fire.\n", 0.04)
        type_text("You gave up after many attempts.\n" + "You decided to sleep for the night in the cold.\n", 0.04)
        sleep_coldness()

#Sleep in the forest
def sleep_forest():
    type_text("\n" + "You decided to sleep for the night in the cold.\n", 0.04)
    sleep_coldness()

#Continue serving the Dark Lord
def continue_serving():
    type_text("\n" + "You decided to continue serving the Dark Lord.\n" + "You have become a loyal servant to the Dark Lord.\n" + "You have become a feared warrior in the land.\n" + "\n" + "75 years later ...\n" + "You lay on the bed, old and frail.\n" + "You have served the Dark Lord for many years.\n" + "You have killed many innocents.\n" + "You weakening body can't take it anymore.\n" + "You close your eyes and take your last breath.\n" + "You have died a loyal servant to the Dark Lord.\n" + "However, you never learnt the lesson of how to love someone.\n" + "Killing is your biggest regret.", 0.04)
    die_regrets()

#Refuse the order
def refuse_order2():
    type_text("\n" + "You can't take it anymore.\n" + "The regrets is filling you up.\n" + name_dialogue + "I can't do this\n" + "Dark Lord: Do you resign as a servant?\n" + name_dialogue + "I do\n" + "Dark Lord: So be it\n" + "The Dark Lord's minions come and kill you.\n" + "You make a worthwhile battle.\n" + "However, you couldn't handle all of the minions.\n", 0.04)
    die_refuse()

#Forest Fire
def forest_fire():
    #Random chance to die from fire
    burn = random.choice("12")
    if burn == "1":
        type_text("\n" + "Remember the fire you made?\n" + "Well, you won't see it anymore.\n" + "Why? You died from the fire.\n" + "The fire spread when you were sleeping, causing a forest fire.\n" + "And unfortunately, you got caught in it.\n", 0.04)
        die_burn()
    else:
        type_text("\n" + "You wake up to the smell of smoke.\n" + "The forest was burning.\n" + name_dialogue + "How did this happen?\n" + "You ran as fast as you could.\n" + "You ran and ran until the fire was no where to be seen.\n" + "You see a small hut nearby.\n" + "You are also very hungry.\n", 0.04)
        type_text("What do you want to do? ", 0.05)
        choice = input("Go to the hut? (1) / Keep walking? (2): ")
        #Choose to go to the hut or keep walking
        if choice == "1":
            hut()
        elif choice == "2":
            keep_walking()
        else:
            #If the input is invalid, ask for the input again
            while choice != "1" and choice != "2":
                type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
                choice = input("Go to the hut? (1) / Keep walking? (2): ")
                if choice == "1":
                    hut()
                elif choice == "2":
                    keep_walking()

#Sleep in the coldness
def sleep_coldness():
    type_text("\n" + "You slept in the coldness.\n" + "You shivered and shivered until you couldn't take it anymore.\n" + "You started to walk again.\n" + "You walked and walked until you couldn't walk anymore.\n" + "You found a small hut.\n", 0.04)
    type_text("What do you want to do? ", 0.05)
    choice = input("Go to the hut? (1) / Keep walking? (2): ")
    #Choose to go to the hut or keep walking
    if choice == "1":
        hut()
    elif choice == "2":
        keep_walking()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            choice = input("Go to the hut? (1) / Keep walking? (2): ")
            if choice == "1":
                hut()
            elif choice == "2":
                keep_walking()

#Die with regrets
def die_regrets():
    type_text("\n" + "Maybe you should be a nicer person next time.\n" + "Clearly, you didn't learn the lesson of how to love someone.\n" + "You were too focused on killing.\n" + "You should have thought about that before you decided to kill innocents.\n", 0.04)
    play_again()

#Die from resigning
def die_refuse():
    type_text("\n" + "You thought you could resign from the Dark Lord's army after killing your friend, John?\n" + "You thought you could just walk away?\n" + "You were wrong.\n" + "You monsters don't just get to walk away.\n" + "You should have thought about that before you decided to resign.\n", 0.04)
    play_again()

#Hut
def hut():
    type_text("\n" + "You entered the hut.\n" + "You see an old man staring out the window with his back towards you.\n" + name_dialogue + "Hel... \n" + "The old man interrupts you.\n" + "Old Man: I have been expecting you.\n" + name_dialogue + "What do you mean?\n" + "Old Man: You have been chosen to wield the power of the elements.\n" + "Old Man: You have the power to control the elements of fire, water, earth, and air.\n" + name_dialogue + "I don't understand.\n" + "Old Man: You will.\n" + "You started to feel suspicious of him.", 0.04)
    type_text("What do you want to do? ", 0.05)
    choice = input("Believe him? (1) / Run away? (2): ")
    if choice == "1":
        believe_him()
    elif choice == "2":
        run_away()
    else:
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            choice = input("Believe him? (1) / Run away? (2): ")
            if choice == "1":
                believe_him()
            elif choice == "2":
                run_away()

#Keep walking
def keep_walking():
    type_text("\n" + "You decided to keep walking.\n" + "You thought that the small hut was too suspicious.\n" + "You walked and walked for hours.\n" + "You found another forest ... \n" + "A forest different from all the ones you have seen.\n" + "The trees are miniature and the flowers are glowing.\n" + "The leaves are all kinds of colors.\n" + "You see a small creature with wings.\n" + "Could that be a ... fairy?\n", 0.04)
    fairy()

#Die from the forest fire
def die_burn():
    type_text("\n" + "Did your parents ever tell you not to play with fire?\n" + "You should have listened to them.\n" + "Well, you can't listen to them now.\n" + "You should have thought about that before you decided to play with fire.\n" + "However, if you were lucky enough, you must have survived.\n", 0.04)
    play_again()

#Believe the old man
def believe_him():
    type_text("\n" + name_dialogue + "Tell me more.\n" + "The old man turns around and you see his eyes glowing.\n" + "Old Man: You are born with the blood of the elements.\n" + "Old Man: Your parents were one of the most famous element wielders.\n" + name_dialogue + "No, I was told that I never had any parents.\n" + "Old Man: You were lied to.\n", 0.04)
    type_text("What do you want to do? ", 0.05)
    choice = input("Believe him? (1) / Run away? (2): ")
    #Choose to believe or run away
    if choice == "1":
        believe_him2()
    elif choice == "2":
        run_away()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            choice = input("Believe him? (1) / Run away? (2): ")
            if choice == "1":
                believe_him2()
            elif choice == "2":
                run_away()
              
#Run away
def run_away():
    type_text("\n" + "You decided to run away from the hut.\n" + "You thought the old man was suspicious.\n" + "You ran and ran until to notice something differen.\n" + "You found another forest ... \n" + "A forest different from all the ones you have seen.\n" + "The trees are miniature and the flowers are glowing.\n" + "The leaves are all kinds of colors.\n" + "You see a small creature with wings.\n" + "Could that be a ... fairy?\n", 0.04)
    fairy()

#Fairy
def fairy():
    type_text("\n" + "...\n" + "You rubbed your eyes.\n" + name_dialogue + "Is this real?\n" + "The fairy hears your voice and gets startled.\n" + "The fairy flies behind a tree to take cover.\n" + "Fairy: Who are you?\n" + name_dialogue + "I'm " + name + ".\n" + "Fairy: You are not from around here.\n" + "Fairy: How are you able to see me?\n" + name_dialogue + "I don't know?\n" + "There is a long pause.\n" + "You go to check up on the fairy.\n" + "However, it was not there.\n" + "Did you imagine it?\n" + "You see a small light in the distance.\n", 0.04)
    fairy_land()

#Believe the old man
def believe_him2():
    type_text("\n" + name_dialogue + "What happened to my parents.\n" + "Old Man: It's a story not to be told.\n" + name_dialogue + "I want to know.\n" + "Old Man: You will know in time.\n" + name_dialogue + "I want to know now.\n" + "Old Man: Your parents were killed by the Dark Lord.\n" + name_dialogue + "What?\n" + name_dialogue + "How?\n" + "Old Man: The Dark Lord was after their power.\n" + name_dialogue + "But, isn't the Dark Lord a mortal like us?\n" + "Old Man: The Dark Lord is not a mortal.\n" + "Old Man: He is a demon.\n" + name_dialogue + "A demon?\n" + "Old Man: Yes.\n" + "Old Man: He has powers that no mortal can have.\n" + "Old Man: He has the power to control the elements.\n" + name_dialogue + "What do you mean?\n" + "Old Man: The same power that you have.\n" + name_dialogue + "I don't understand.\n" + "Old Man: You will.\n", 0.04)
    secret_room()

#Fairy Land
def fairy_land():
    type_text("\n" + "You followed the light.\n" + "It's becoming brighter and brighter ...\n" + "Suddenly, you couldn't move.\n" + "You were in cobwebs.\n" + "Fairy 1: Good thing we collected some spider webs.\n" + "Fairy 2: Yes, it came in handy for this human.\n" + "Fairy 1: We should take him to the Queen.\n" + "Fairy 2: Yes, we should.\n" + "You were carried by the fairies.\n" + "You were taken to a beautiful land.\n" + "The land was filled with glowing flowers and miniature trees with what looks like fairy houses.\n" + "You see a palace decorated in the most beautiful way.\n" + "With flowers and leaves of all kinds.\n" + "Fairy 1: This human is too big.\n" + "Fairy 2: Yes, we should call the queen.\n" + "The fairy left and came back with the fairy you saw and what looks like the queen.\n" + "Fairy Queen: Who are you?\n" + name_dialogue + "I'm " + name + ".\n" + "Fairy Queen: You are not from around here.\n" + "Fairy Queen: How are you able to see us?\n" + name_dialogue + "I don't know?\n" + "Fairy Queen: You are not a normal human.\n" + "Fairy Queen: I have never encountered this in so long ...\n" + "Fairy Queen: Not since Shawn and Alice.\n" + name_dialogue + "Who are they?\n" + "Fairy Queen: They were the last humans to come here.\n" + "Fairy Queen: They were humans who carried the power of the elements.\n" + name_dialogue + "I don't understand.\n" + "Fairy Queen: You won't have to.\n", 0.04)
    waterfall()

#Secret Room
def secret_room():
    type_text("\n" + "Old Man: Follow me.\n" + "You followed the old man to a secret room.\n" + "The room was filled with books and scrolls.\n" + "Old Man: This is where you will learn about your power.\n" + name_dialogue + "What power?\n" + "Old Man: The power of the elements.\n" + "Old Man: Hold this.\n" + "He hands you a scroll.\n" + "You held it and felt a surge of heat, calmness, and power.\n" + "Old Man: Do you feel it?\n" + name_dialogue + "What is this?\n" + "Old Man: This is the elements calling to you.\n" + "Old Man: You won't be able to control it at first.\n" + "Old Man: But, you will learn.\n" + name_dialogue + "I don't understand\n" + "Old Man: You will.\n" + "Old Man: Come back tomorrow and we will start your training.\n" + name_dialogue + "I don't have anywhere to stay\n" + "Old Man: You can stay here.\n" + "The old man showed you to a room.\n" + "It was filled with books and looked ancient.\n" + "Old Man: This will be your room for now on.\n" + name_dialogue + "Thank you.\n" + "The old man leaves and closes the the door behind him.\n" + "You are tired from all the walking and the events of the day.\n" + "You decided to sleep for the night.\n", 0.04)
    next_day()

#Fairy Land 2
def waterfall():
    type_text("\n" + "Fairy Queen: Take him to the place.\n" + "Fairy 2: Yes, my queen.\n" + "You were taken to another place.\n" + "There was a waterfall and a singular boulder poking out of the waterfall.\n" + "Fairy Queen: Bring this human there.\n" + "Fairies: Yes, my queen.\n" + "The fairies carried you to the boulder you saw.\n" + "The water fell on you.\n" + "You felt pain from the water.\n" + "You felt like you were burning.\n" + "You screamed in pain.\n" + "The cobweb kept you in place.\n" + "You couldn't move.\n" + "You felt like you were going to die.\n" + "Fairy Queen: Answer our questions, you human.\n" + "You tried to talk but the water was just too much.\n" + "The water kept gushing down on you in full force.\n" + "Fairy Queen: Answer or die.\n", 0.04)
    #Answer the questions
    #Question 1
    type_text("Fairy Queen: Are you a demon? ", 0.05)
    #Randomly choose a letter
    letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    print(letter)
    guess = input("Enter the letter to keep living: ")
    #If the letter is correct
    if guess == letter:
        type_text("The water hurted you but you were able to answer the question.\n", 0.04)
        type_text(name_dialogue + "I'm not a demon.\n" + name_dialogue + "Demons are not even real.\n", 0.04)
    else: 
        #If the letter is wrong
        type_text("The water hurted you and you were unable to answer the question.\n", 0.04)
        type_text("You have fainted from the pain.\n", 0.04)
        die_waterfall()
        return
    #Question 2
    type_text("Fairy Queen: Do you know the Dark Lord? ", 0.05)
    letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    print(letter)
    guess = input("Enter the letter to keep living: ")
    #If the letter is correct
    if guess == letter:
        type_text("The water hurted you but you were able to answer the question.\n", 0.04)
        type_text(name_dialogue + "Yes ... they destroy my hometown\n" + name_dialogue + "I ran away to survive.\n", 0.04)
    else:
        #If the letter is wrong
        type_text("The water hurted you and you were unable to answer the question.\n", 0.04)
        type_text("You have fainted from the pain.\n", 0.04)
        die_waterfall()
        return
    #Question 3
    type_text("Fairy Queen: How are you able to see us? ", 0.05)
    letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    print(letter)
    guess = input("Enter the letter to keep living: ")
    #If the letter is correct
    if guess == letter:
        type_text("The water hurted you but you were able to answer the question.\n", 0.04)
        type_text(name_dialogue + "I don't know.\n" + name_dialogue + "I just kept walking and saw something with wings.\n", 0.04)
    else:
        #If the letter is wrong
        type_text("The water hurted you and you were unable to answer the question.\n", 0.04)
        type_text("You have fainted from the pain.\n", 0.04)
        die_waterfall()
        return
    end_questioning()

#Next Day
def next_day():
    type_text("\n" + "You wake up to the sun shining through the window.\n" + "You remember the events of yesterday.\n" + "You get up and go to the secret room.\n" + "The old man was waiting for you.\n" + name_dialogue + "I'm here.\n" + "Old Man: Let's start your first lesson.\n" + "You listened to his lecture about elements.\n" + "Old Man: Let's start with the element of fire.\n" + "Old Man: To release this power, you need to apply anger.\n" + "Old Man: Like this.\n" + "The old man shoots out a fireball and hits the fireplace, igniting the firewood.\n" + "Old Man: Now try it.\n", 0.04)
    words = ["annkjssadaknjsd" , "sadaisbasdvccdua", "asasdnjdasdsad", "asdahdfzxcnsfsd", "eriuoznxkcjxcvasd", "njjzxcczxcxciojia", "aoioibcvbcsdudn", "vkbdjdissfsdfvbasd", "husahdujjnsdjidsa", "bhbjcbjcxkjzhxbcj", "wquoidofxxcjoiob", "zxxbzcibcjbjkasd", "knjkjskdshoasdjbkasd"]
    word = random.choice(words)
    print(word)
    guess = input("Enter the word to release the fireball: ")
    #If the word is correct, release the fireball
    if guess == word:
        type_text("You successfully released the fireball.\n", 0.04)
        elements()
    else:
        #If the word is wrong, try again
        while guess != word:
            type_text("You couldn't release it", 0.05)
            type_text("\n" + "Old Man: It's okay. Try again.\n", 0.04)
            word = random.choice(words)
            print(word)
            guess = input("Enter the word to release the fireball: ")
            if guess == word:
                type_text("You successfully released the fireball.\n", 0.04)
    elements()

#Die from the waterfall
def die_waterfall():
    type_text("\n" + "You couldn't handle the pain from the water.\n" + "The water fell on you at incredible speeds.\n" + "If only you answered the questions.\n", 0.04)
    play_again()

#End of questioning
def end_questioning():
    type_text("\n" + "Fairy Queen: You have answered our questions.\n" + "Fairy Queen: You are not a demon.\n" + "Fairy Queen: Nor the Dark Lord's minion.\n" + "Fairy Queen: Bring this human back.\n" + "The fairies carried you back to the boulder.\n" + "The pain from the water stopped.\n" + "You were able to move again.\n" + "You were able to breathe again.\n" + "You were able to talk normally again.\n" + "Fairy Queen: If you are not either of those, you might have the powers of the elements.\n" + "Fairy Queen: You are free to go.\n" + "Fairy Queen: Bring him out of the land.\n" + "Fairy Queen: Forget what happened here.\n" + name_dialogue + "Wait, what is the power of the elements?\n" + "Fairy Queen: You won't have to know.\n" + name_dialogue + "Please, I want to know.\n" + "The Fairy Queen turns around, her back to you.\n" + "Fairy Queen: The power of elements is something I used for many decades.\n" + "Fairy Queen: It's a power that can destroy or save the world.\n" + "Fairy Queen: It's a power that can bring peace or chaos.\n" + "Fairy Queen: It's a power that can bring life or death.\n" + "Fairy Queen: We should never have given it to humans.\n" + "Fairy Queen: However, you are an exception.\n" + "Fairy Queen: You remind me of Shawn and Alice.\n" + "Fairy Queen: Prehaps, you are what the rumors say.\n" + name_dialogue + "What rumors.\n" + "The fairy you encountered spoke.\n" + "Fairy: Shawn and Alice had a kid who was lost during the battle with the Dark Lord.\n" + "Fairy: They say that the kid will come back to save us all.\n" + "Fairy: They say that the kid will have the power of the elements.\n" + "Fairy: They say that the kid will be the one to defeat the Dark Lord.\n" + "The Fairy Queen faces you again.\n" "Fairy Queen: Yes, Olivia.\n" + "I believe you might be the one.\n" + name_dialogue + "I don't understand.\n" + name_dialogue + "I never had any parents.\n" + "Fairy Queen: You were lied to.\n" + "Fairy Queen: Fairies, bring this human back.\n" + "Fairy Queen: This human is the one.\n" + "The fairies takes you back to the fairyland.\n" + name_dialogue + "Please, I want to know more.\n" + "Fairy Queen: You will know tomorrow.\n" + "Fairy Queen: You will know everything.\n" + "Fairy Queen: Go rest until tomorrow.\n" + "You were shown to an human-sized room.\n" + "You were given food and water.\n" + "You were tired from the events of the day.\n" + "You decided to sleep for the night.\n", 0.04)
    next_day2()

#Release the elements
def elements():
    type_text("\n" + "Old Man: Well done, " + name + ".\n" + "Old Man: You have released the element of fire.\n" + "Let's move on to the next element.\n" + "After hours of training, you learned all the elements.\n" + "Old Man: You have learned all the elements.\n" + "Old Man: You are now ready to wield the power of the elements and use them.\n" + name_dialogue + "Thank you.\n" + "Old Man: You are excepted to use this power for good.\n" + "Old Man: You are excepted to use this power to defeat the Dark Lord.\n" + name_dialogue + "The Dark Lord?\n" + name_dialogue + "How am I supposed to defeat the Dark Lord?\n" + name_dialogue + "I'm just one person.\n" + "Old Man: You are not just one person.\n" + "Old Man: You have the power of the elements and nature on your side.\n" + name_dialogue + "I don't think I can do it.\n" + "Old Man: You can.\n" + "Old Man: The elements will guide you.\n" + "Old Man: Just like they guided your parents.\n" + "Old Man: Just like they guided Shawn and Alice\n" + "Old Man: Now go rest and tomorrow set out to defeat the Dark Lord.\n" + name_dialogue + "Shawn and Alice?\n" + "Old Man: You will know one day.\n" + "The old man left the room.\n" + "You got on the bed and laid down.\n" + "You wondered who Shawn and Alice were.\n" + "You wondered who your parents were.\n" + "You wondered if you could defeat the Dark Lord.\n" + "You closed your eyes and went to sleep.\n", 0.04)
    next_day3()
    return

#Next Day 2
def next_day2():
    type_text("\n" + "You woke up to the touch of a tiny hand.\n" + "Olivia: It's time to wake up " + name + ".\n" + "You woke up and saw Olivia's face.\n" + "Olivia: The Fairy Queen is about to teach you about the elements.\n" + "Olivia: You better get ready.\n" + "You got up and followed Olivia to the Fairy Queen.\n" + "Fairy Queen: Today, I will teach you the powers of the elements.\n" + "Fairy Queen: You will learn how to control them.\n" + "Fairy Queen: You will learn how to use them.\n" + "Fairy Queen: It will not be easy.\n" + "Fairy Queen: But, you will learn.\n" + "Fairy Queen: There are multiple elements.\n" + "Many elements that you can control.\n" + "Fairy Queen: However, no creature can learn them all.\n" + "Fairy Queen: Such elements are Fire, Air, Earth, Water, Light, Ice, Lightning, and ... Darkness.\n" + "Fairy Queen: I will teach you the element of Light.\n" + "Fairy Queen: To release this power, you need to apply happiness.\n" + "Fairy Queen: Like this.\n" + "The Fairy Queen shoots out a light beam and hits the wall, illuminating the room.\n" + "Fairy Queen: You can hurt or heal with this power.\n" + "Fairy Queen: Now try it.\n", 0.04)
    words = ["annkjssadaknjsd" , "sadaisbasdvccdua", "asasdnjdasdsad", "asdahdfzxcnsfsd", "eriuoznxkcjxcvasd", "njjzxcczxcxciojia", "aoioibcvbcsdudn", "vkbdjdissfsdfvbasd", "husahdujjnsdjidsa", "bhbjcbjcxkjzhxbcj", "wquoidofxxcjoiob", "zxxbzcibcjbjkasd", "knjkjskdshoasdjbkasd"]
    word = random.choice(words)
    print(word)
    guess = input("Enter the word to release the light beam: ")
    #If the word is correct, release the light beam
    if guess == word:
        type_text("You successfully released the light beam.\n", 0.04)
        elements2()
    else:
        #If the word is wrong, try again
        while guess != word:
            type_text("You couldn't release it", 0.05)
            type_text("\n" + "Fairy Queen: It's okay. Try again.\n", 0.04)
            word = random.choice(words)
            print(word)
            guess = input("Enter the word to release the light beam: ")
            if guess == word:
                type_text("You successfully released the light beam.\n", 0.04) 
    elements2()

#Next Day 3
def next_day3():
    type_text("\n" + "You woke up to the bright sun shining through the window.\n" + "You have a duty to do.\n" + "You have to defeat the Dark Lord.\n" + "You got up and went to the secret room.\n" + "The old man was longer there.\n" + "There was a note on the table.\n" + "The note read: " + name + ", you have the power to defeat the Dark Lord.\n" + "The note read: It is time for you to defeat the Dark Lord once and for all.\n" + "The note read: I have a duty to do as well.\n" + "The note read: I have to protect the land from the Dark Lord's minions.\n" + "The note read: You are the only one who can defeat him.\n" + "The note read: You are the only one who can save us all.\n" + "The note read: Go and bring peace back to our lands.\n" + "From: William Solace\n" + "You were shocked to see the name.\n" + "You never knew the old man's name until now.\n" + "You felt determined to defeat the Dark Lord.\n" + "You set out to find the Dark Lord.\n", 0.04)
    dark_lord()
    return

#Release the elements 2
def elements2():
    type_text("\n" + "Fairy Queen: You have successfully learned how to release the element of Light.\n" + "Fairy Queen: You have learned how to control it now.\n" + "Fairy Queen: You need to use it to help others.\n" + "Fairy Queen: Come here.\n" + "You came up to the Fairy Queen.\n" + "The Fairy Queen flew up on top of your head.\n" + "You felt a wierd sensation.\n" + "You felt like you were glowing.\n" + "You felt like you were floating.\n" + "Fairy Queen: Your pain from the water should be gone now.\n" + "Fairy Queen: This will be another of your lesson.\n" + "Fairy Queen: You will learn how to heal others.\n" + "The Fairy Queen flew back down to face you.\n" + "Fairy Queen: Olivia, bring me a thorn.\n" + "Olivia: Yes, my queen.\n" + "After some time, Olivia came back with a thorn.\n" + "Fairy Queen: " + name + ", cut yourself with it.\n" + name_dialogue + "What?\n" + "Fairy Queen: Trust me.\n" + "You cut yourself with the thorn.\n" + "You felt pain.\n" + "You felt a wierd tingle in your veins.\n" + "Fairy Queen: There is some little poison in it.\n" + "Fairy Queen: You must learn the power to heal on you own.\n" + "Fairy Queen: You have 3 days before the poison kills you.\n" + "Fairy Queen: Let's go fairies.\n" + "The fairies left the room.\n" + "You were left alone in the room.\n", 0.04)
    type_text("What do you want to do? ", 0.05)
    choice = input("Learn to heal yourself? (1) / Try to escape (2): ")
    #Choose to heal or escape
    if choice == "1":
        heal_poison()
    elif choice == "2":
        escape_fairyland()
    else:
        #If the input is invalid, ask for the input again
        while choice != "1" and choice != "2":
            type_text("Invalid choice. Please choose '1' or '2'.\n", 0.07)
            choice = input("Heal yourself? (1) / Wait for the poison to kill you? (2): ")            
            if choice == "1":
                heal_poison()
            elif choice == "2":
                escape_fairyland()

#Dark Lord
def dark_lord():
    type_text("\n" + "You found a map that the old man left for you.\n" + "It showed the Dark Lord's hideout.\n" + "You decided to follow the path.\n" + "After hours of walking.\n" + "You see a person with armor that you recognize.\n" + "Dark Lord's minions: Hehe, who do we have here?\n" + name_dialogue + "I am " + name + " and I am here to destory the Dark Lord!\n" + "Dark Lord's minion: Hahaha, this human thinks it can beat us.\n" + "Dark Lord's minion: How ridiculous.\n" + "You shoot a fireball at the minion.\n" + "Dark Lord's minion: Ahhhh, that's it.\n" + "Dark Lord's minion: Get that person.\n", 0.04)
    words = ["annkjssadaknjsd" , "sadaisbasdvccdua", "asasdnjdasdsad", "asdahdfzxcnsfsd", "eriuoznxkcjxcvasd", "njjzxcczxcxciojia", "aoioibcvbcsdudn", "vkbdjdissfsdfvbasd", "husahdujjnsdjidsa", "bhbjcbjcxkjzhxbcj", "wquoidofxxcjoiob", "zxxbzcibcjbjkasd", "knjkjskdshoasdjbkasd"]
    word = random.choice(words)
    print(word)
    guess = input("Enter the word to fight back: ")
    #If the word is correct
    if guess == word:
        type_text("You successfully released a spike from the ground.\n", 0.04)
        type_text("Dark Lord's minions: Oww, that hurt.\n", 0.04)
    else:
        #If the word is wrong
        while guess != word:
            type_text("You couldn't release your elements", 0.05)
            type_text("\n" + "Dark Lord's minion: You moron, you thought your good?\n", 0.04)
            die_dark_lord_minion()
            return
    word = random.choice(words)
    print(word)
    guess = input("Enter the word to fight back: ")
    #If the word is correct
    if guess == word:
        type_text("You successfully released a strong wind that blew the minions back.\n" + "The minion hit the trees behind with incredible forece.", 0.04)
        type_text("\n" + "Dark Lord's minions: Oww, please stop.\n", 0.04)
    else:
        #If the word is wrong
        while guess != word:
            type_text("You couldn't release your elements", 0.05)
            type_text("\n" + "Dark Lord's minion: You got us once, but never the second time.\n", 0.04)
            die_dark_lord_minion()
            return
    word = random.choice(words)
    print(word)
    guess = input("Enter the word to fight back: ")
    #If the word is correct
    if guess == word:
        type_text("You successfully released a flow of water trapped the minions in place.\n", 0.04)
        type_text("\n" + "Dark Lord's minions: Gulp, gulp, gulp, please st... Gulp.\n", 0.04)
    else:
        #If the word is wrong
        while guess != word:
            type_text("You couldn't release your elements", 0.05)
            type_text("\n" + "Dark Lord's minion: Sucks to be you.\n", 0.04)
            die_dark_lord_minion()
            return
    dark_lord_battle()
    return

#Heal poison
def heal_poison():
    type_text("\n" + name_dialogue + "Hey ... how do I heal myself?\n" + "You tried to remember what the Fairy Queen said.\n" + "However, she never taught how to heal.\n" + "You tried to remember to apply happiness to heal your wound.\n" + "But, it didn't work.\n" + name_dialogue + "Please teach me how to heal!\n" + "There was no answer ...\n" + "You tried to heal yourself again.\n" + "But, it did not work.\n" + "AFter hours or maybe days, you still couldn't release the power of healing.\n" + "You felt the poison taking over your body.\n" + "You felt the poison taking over your mind.\n" + "You sat on the ground hopeless without any sleep.\n" + "Suddenly, you heard a tiny knock somewhere.\n" + "You looked around and saw a fairy on the other side of the window.\n" + "It was Olivia.\n" + "Olivia: I'm breaking the rules to help you.\n" + "Olivia: I saw you struggling without any progress.\n" + "Olivia: I didn't want you to die.\n" + "Olivia: I will teach you how to heal.\n" + "Olivia: But, I have to be quick or else another fairy might see me.\n" + "Olivia: You have to apply joy to heal.\n" + "Olivia: Like this.\n" + "Olivia shot a light beam at the ground below.\n" + "Flowers bloomed from the ground.\n" + "It made a garden unlike any you have seen.\n" + "Olivia: That is all you need to know.\n" + "Olivia: I have to go now.\n" + "Olivia: Good luck, " + name + ".\n" + "Olivia flew away.\n", 0.04)
    type_text("\n" + "You tried to heal yourself.\n" + "You applied joy to your wound.\n" + "You felt a surge of happiness.\n" + "You felt a surge of power.\n" + "You felt a surge of light.\n" + "You felt the poison leaving your body.\n" + "But, you still felt pain.\n" + "Did it work?\n" + "You looked at your arm, it still had the wound.\n" + "You looked sad.\n" + "However, you remembered that not everything comes out perfect.\n" + "You remembered that you have to keep trying.\n" + "You tried again.\n", 0.04)
    words = ["annkjssadaknjsd" , "sadaisbasdvccdua", "asasdnjdasdsad", "asdahdfzxcnsfsd", "eriuoznxkcjxcvasd", "njjzxcczxcxciojia", "aoioibcvbcsdudn", "vkbdjdissfsdfvbasd", "husahdujjnsdjidsa", "bhbjcbjcxkjzhxbcj", "wquoidofxxcjoiob", "zxxbzcibcjbjkasd", "knjkjskdshoasdjbkasd"]
    word = random.choice(words)
    print(word)
    guess = input("Enter the word to heal yourself: ")
    #If the word is correct, heal yourself
    if guess == word:
        type_text("You have successfully learned to heal yourself\n" + "You felt the wound closing up.\n" + "You felt the pain leaving your body.\n" + "You felt the joy of healing yourself.\n", 0.04)
        healed_yourself()
    else:
        #If the word is wrong, try again
        while guess != word:
            type_text("You couldn't heal yourself\n" + "You remember that things take time.\n" + "You tried again.\n", 0.05)
            word = random.choice(words)
            print(word)
            guess = input("Enter the word to heal yourself: ")
            if guess == word:
                type_text("You have successfully learned to heal yourself\n" + "You felt the wound closing up.\n" + "You felt the pain leaving your body.\n" + "You felt the joy of healing yourself.\n", 0.04)
                healed_yourself()

#Escape Fairyland
def escape_fairyland():
    type_text("\n" + "You tried escaping.\n" + name_dialogue + "What the heck did I get myself into?\n" + "You tried breaking the window but it didn't work.\n" + "You tried everything but your still stuck here.\n" + "You kept wasting your time trying to escape that the poison was taking over your body.\n" + "Soon, you died of the poison.\n", 0.04)
    die_escaping_fairyland()

#Die from the Dark Lord's minion
def die_dark_lord_minion():
    type_text("\n" + "You were held by the minion.\n" + "Their hands on your throat.\n" + "You couldn't breathe.\n" + "Soon, you died of lack of oxygen.\n" + "Dark Lord's minions: Stupid human.\n" + "Dark Lord's minions: Hahahaha.\n" + "\n" + "You are not as good as you think.\n" + "Clearly you don't know your capabilities.\n", 0.04)
    play_again()

#Dark Lord Battle
def dark_lord_battle():
    type_text("\n" + "You kept going on your journey to battle the Dark Lord.\n" + "Soon, you see a palace in the distance.\n" + "You see the Dark Lord standing in front of the palace.\n" + "Dark Lord: So, you are the one who has been causing trouble.\n" + name_dialogue + "I'm here to defeat you.\n" + "Dark Lord: Hahaha, you think you can defeat me?\n" + "Dark Lord: You are just a human.\n" + "Dark Lord: You are nothing compared to me.\n" + "You shoot a fireball at the Dark Lord.\n" + "Dark Lord: Hahaha, that's all you got?\n" + "Dark Lord: You are weak.\n" + "Dark Lord: You are nothing.\n" + "You shoot a tornado at the Dark Lord.\n" + "Dark Lord: Oww, that hurts.\n" + "Dark Lord: Hahahahahah.\n" + "The Dark Lord shoots a beam of darkness at you.\n", 0.04)
    words = ["annk2jssa45daknjsda6sgas214gddasfa" , "sa3daisbas47dasagh5hjaksfv5ccdua", "asasd46njdfgdfg5hdf6uhgi34dasdsad", "asdahdf234zxcigig56bsduf67usdnsfsd", "eriuoz123nsdgihdu51gsgdxkcjx5cvasd", "njjzxdsg21dsfsdif4hcc812zxcxc5iojia", "aoioi1bcsd4fisd6fosv7bsdgs8sdgcs2dudn", "vkb1djdiss23fssdf7hsu5odfd5fvbasd", "hus123ahdujj4nsd6sdgo5hdsogd7sgjids8a", "bhbj123cbjcs4dgui4hod54sgxkj6zhxbcj", "wqu23osdgohd43oigsdi45dofxx7cjoi8ob", "zxxb23zcibcj34sdgo4ihs5do6gisbjka7sd", "knjk123jsksdgo54sdigdshoa68sdj8bkasd"]
    word = random.choice(words)
    print(word)
    guess = input("Enter the word to dodge the attack: ")
    #If the word is correct, dodge the attack
    if guess == word:
        type_text("You successfully dodged the attack.\n", 0.04)
        type_text("Dark Lord: You got skills.\n" + "Dark Lord: Let's see if you can dodge this.\n" + "The Dark Lord turn the sky into pitch black.\n" + "He shot hundreds of dark arrows at you.\n", 0.04)
    else:
        #If the word is wrong, die from the attack
        while guess != word:
            type_text("You couldn't dodge the attack", 0.05)
            type_text("\n" + "Dark Lord: Weakling.\n" + "Dark Lord: Hahahahahaha\n", 0.04)
            die_dark_lord()
            return
    word = random.choice(words)
    print(word)
    guess = input("Enter the word to block the attack: ")
    #If the word is correct, block the attack
    if guess == word:
        type_text("You successfully released the power of Wind to block the arrows.\n", 0.04)
        type_text("\n" + "Dark Lord: You are good.\n" + "Dark Lord: But, how strong are you.\n" + "Dark Lord: Hit me with all you've got.\n" + "Dark Lord: Hahahaha.\n", 0.04)
    else:
        #If the word is wrong, die
        while guess != word:
            type_text("You couldn't block the attack", 0.05)
            type_text("\n" + "Dark Lord: Weakling.\n" + "Dark Lord: Hahahahahaha\n", 0.04)
            die_dark_lord()
            return
    word = random.choice(words)
    print(word)
    guess = input("Enter the word to attack the Dark Lord: ")
    #If the word is correct, attack the Dark Lord
    if guess == word:
        type_text("\n" + "You successfully released a beam of all the 4 elements at the Dark Lord.\n", 0.04)
        type_text("Dark Lord: Ahhhh, now you have done it.\n" + "Dark Lord: You have made me mad.\n" + "Dark Lord: You will pay for this.\n" + "The Dark Lord shot a beam of darkness at you so fast that it hit you.\n", 0.04)
    else:
        #If the word is wrong, die
        while guess != word:
            type_text("You couldn't release the attack", 0.05)
            type_text("\n" + "Dark Lord: Weakling.\n" + "The Dark Lord shot a super fast dark beam at you.\n" + "You couldn't dodge it.\n", 0.04)
            die_dark_lord()
            return
    type_text("You felt a burn on your shoulders.\n" + "You felt like you were about to die.\n" + "However, you remember the promise you made to the old man.\n" + "The terror that happened to your village.\n" + name_dialogue + "I will not let you live another day.\n", 0.04)
    power = input("Enter as much letters as you can to release the power of the elements (You want to type a lot): ")
    #If the input is more than 100 characters, win
    if len(power) > 100:  
        type_text("You successfully released the power of the elements.\n" + "You hit the Dark Lord with incredible power.\n" + "Dark Lord: AHHHHHHHHHhhhh...\n" + "The Dark Lord fell to the ground.\n" + "Dark Lord: I never knew it would come to this...\n" + "Dark Lord: Kid, who are you.\n" + name_dialogue + " " + name + ".\n" + "Dark Lord: You were a worthy opponent.\n" + "Dark Lord: You better use that power not like how I used mine.\n" + "Dark Lord: Use it for the good of people.\n" + "The Dark Lord's body started to fade away.\n" + "Even the palace and the minions around started to disappear.\n" + "You wondered what happened.\n" + "You wondered if you did the right thing.\n" + "You wondered if you could ever go back to your village.\n" + "Suddenly, you felt a hand on your shoulder.\n" + "You turned around and saw William Solace.\n" + "\n" + "William Solace: Good job, " + name + ".\n" + "William Solace: You have brought peace to our lands.\n" + "William Solace: Let's go back to the village.\n" + "You were teleported back to the village.\n", 0.04)
        win()
    else:
        #If the input is less than 100 characters, die
        while len(power) < 100:
            type_text("You didn't release enough power", 0.05)
            type_text("\n" + "Dark Lord: Weakling.\n" + "The Dark Lord shot a super fast dark beam at you.\n" + "You couldn't dodge it.\n", 0.04)
            die_dark_lord()
            return
    
#Healed yourself
def healed_yourself():
    type_text("\n" + "The doors opened.\n" + "You saw the fairies.\n" + "Fairy Queen: Congratulations.\n" + "Fairy Queen: You have learned to heal.\n" + "Fairy Queen: Tomorrow, you will set out for the Dark Lord.\n" + "Fairy Queen: But, today, you rest and relax.\n" + "The Fairy Queen was about to leave.\n" + "Then ...\n" + name_dialogue + "But, I haven't learned everything about the Light element yet.\n" + "Fairy Queen: You have.\n" + "Fairy Queen: You will be able to do anything with the skills you learned.\n" + "The fairies left the room, leaving you alone.\n" + "You went to bed and slept.\n", 0.04)
    next_day4()

#Die from escaping Fairyland
def die_escaping_fairyland():
    type_text("The Fairy Queen comes into your room.\n" + "Fairy Queen: Selfish human.\n" + "Fairy Queen: This human was definitely not the one.\n" + "Fairy Queen: This human was useless.\n" + "Fairy Queen: Throw this thing out.\n" + "The fairies took your body and threw it out of the fairyland.\n" + "You were left in the forest to rot.\n", 0.04)
    type_text("\n" + "Maybe you should have followed the instructions.\n" + "You came pretty far to die like this.\n" + "You need to think logically.\n" + "You need to think before you act.\n", 0.04)
    play_again()

#Win
def win():
    type_text("\n" + "You saw John and all of the villagers.\n" + name_dialogue + "How?\n" + "John: We fought the Dark Lord and somehow survived!\n" + "John: But, you, my friend ...\n" + "John: The runner ...\n" + "John: WILL BE REMEMBERED AS A HERO.\n" + "The villagers applauded for your heroic deed.\n" + "You and the villagers had a feast that day.\n" + "You were happy to be back.\n" + "You were happy to be alive.\n" + "You brought peace back to Everpeace.\n" + "Everpeace remained peaceful for the years to come.\n" + "But, will it be peaceful forever?\n" + "Only time will tell.\n" + "The End.\n", 0.04)
    custom_play_again()

#Die from the Dark Lord
def die_dark_lord():
    type_text("\n" + "You thought that by having acquired the four elements you could beat anyone?\n" + "Well you were wrong.\n" + "You just wasted your life just to die.\n")
    play_again()

#Next Day 4
def next_day4():
    type_text("\n" + "You woke up to the bright sun shining through the window.\n" + "You have a duty to do.\n" + "You have to defeat the Dark Lord.\n" + "You got up and saw the fairies outside your room.\n" + "Fairy Queen: It is time ...\n" + "Fairy Queen: Bring peace back to our lands, " + name + ".\n" + "Fairy Queen: Also, take this.\n" + "She handed you a shining light.\n" + "Fairy Queen: This light will guide you to the Dark Lord's palace.\n" + name_dialogue + "Thank you!\n" + name_dialogue + "I will defeat the Dark Lord and bring peace back to our lands!\n" + "You set out to find the Dark Lord.\n" + "After hours of walking with guidance of the light.\n" + "You see a palace in the distance.\n" + "Dark Lord: You human.\n" + "Dark Lord: You have come to face me.\n" + "Dark Lord: Do you not know of me?\n" + "The Dark Lord turns the sky into pitch darkness.\n" + "Dark Lord: I am the Dark Lord.\n" + "Dark Lord: I am the ruler of this land.\n" + "Dark Lord: I am the one who will destroy you.\n" + "Dark Lord: Let's see what you've got.\n", 0.04)    
    #Fight
    player_health = 100
    dark_lord_health = 120

    #While the player and the Dark Lord are alive
    while player_health > 0 and dark_lord_health > 0:
        print("Player Health: " + str(player_health))
        print("Dark Lord Health: " + str(dark_lord_health))
        print("1. Light Beam")
        print("2. Light Shower")
        print("3. Light Blast")
        print("4. Heal")
        action = input("Enter your action: ")

        #Action
        while action not in ["1", "2","3","4"]:
                type_text("Invalid choice. Please choose '1' or '2' or '3' or '4'.\n", 0.07)
                action = input("Enter your action: ")
        
        #Action Choice
        if action == "1":
            type_text("You released a light beam at the Dark Lord.\n", 0.04)
            dark_lord_health -= 10
        elif action == "2":
            type_text("You released a light shower at the Dark Lord.\n", 0.04)
            dark_lord_health -= 15
        elif action == "3":
            type_text("You released a light blast at the Dark Lord.\n", 0.04)
            dark_lord_health -= 20
        elif action == "4":
            type_text("You healed yourself.\n", 0.04)
            if player_health < 100:
                player_health += 10
            elif player_health > 100:
                player_health = 100

        #Dark Lord's Attack 
        if dark_lord_health > 0:
            words = ["The Dark Lord shot a beam of darkness at you so fast.\n", "The Dark Lord shot thousands of dark arrows at you.\n", "The Dark Lord shot a swords of darkness at you.\n"]
            word = random.choice(words)
            print(word)
            dodge_words = ["saduhusahdiu124jnjsda", "928ehiuaisdbjabsdasd", "1293uiuasdbsadw012uesad", "8219ue9hadbasbdbjbhsad", "213iuaisudbjsabdknsad", "021ehusadbsdjas192euabif", "9182ehabdiahsbdiifasf", "213hasdh0adjsabfhjasd"]
            dodge_word = random.choice(dodge_words)
            print(dodge_word)
            guess = input("Enter the word to dodge the attack: ")
            #If the word is correct, dodge the attack
            if guess == dodge_word:
                type_text("You successfully dodged the attack.\n", 0.04)
            else:
                #If the word is wrong, lose health
                type_text("You couldn't dodge the attack", 0.05)
                player_health -= 10

    #Player Died
    if player_health <= 0:
        type_text("The Dark Lord killed you.\n" + "Dark Lord: I told you were just a weakling.\n" + "Dark Lord: Don't deny it.\n" + "Dark Lord: HAHAHAHAHHA\n", 0.04)
        play_again()
    
    #Win
    if dark_lord_health <= 0:
        type_text("You defeated the Dark Lord.\n" + "The Dark Lord fell to the ground.\n" + "You could the darkness and its ominous feeling disappear.\n" + "You could feel the darkness and evilness of the Dark Lord fading.\n" + "Dark Lord: My darkness is gone.\n" + "Dark Lord: Thank you!\n" + "Dark Lord: Please tell me your name.\n" + name_dialogue + "It's " + name + ".\n" + "Dark Lord: Your a worthy opponent.\n" + "Dark Lord: Don't lose yourself the side of darkness like I did.\n" + "The Dark Lord's body faded away.\n" + "Suddenly, you saw a fairy.\n" + "Fairy Queen: Good job, " + name + ".\n" + "Fairy Queen: You have done well.\n" + "Fairy Queen: Let's go back to the village.\n" + "You were teleported back to the village.\n", 0.04)
        win()
        return

#King name secret lore
def king_name():
    type_text("\n" + "..." + "\n" + "You are the King.\n" + "...\n" + "You are 10 years old...\n" + "You have no friends...\n" + "You are alone in this world.\n" + "You don't even have parents.\n" + "Even if you do, you don't know them.\n" + "...\n" + "You are sitting next to a store in the city of Karelore.\n" + "Random Guy: Move it you thing!\n" + "You were homeless.\n" + "You sat next to the store as a beggar.\n" + "Random Guy: If you don't move, I kill you.\n" + "You didn't move.\n" + "...\n" + "Boom.\n" + "The guy kicked you so hard that you fell to the floor.\n" + "Random Guy: I told you, didn't I?\n" + "Random Guy: Hahahahahaha.\n" + "The guy grabbed you and tossed into near the trash.\n" + "Your vision started to become worse.\n" + "Suddenly, the world went blank.\n" + "...\n" + "Voice: Don't you feel like you don't belong in this world?\n" + "...\n" + "Voice: Don't you feel like your powerless?\n" + "...\n" + "Voice: Don't you ask yourself why life is so unfair?\n" + "...\n" + "Voice: If you join me, I will give you everything that you ever wanted.\n" + "Voice: All you need to do is to join me.\n" + "Voice: You can get revenge on the ones who hurt you.\n" + "Voice: Join me and you will feel invincible.\n" + "Voice: So, what do you say.\n" + "Matthew: Giv... e ... me ... th... at. po. wer...\n" + "Voice: Good choice, my friend.\n" + "You started to feel a surge of power around you.\n" + "Your vision was becoming better.\n" + "Your pain was disappearing.\n" + "You feel strong.\n" + "Voice: I will teach you the power of this element.\n" + "You were back at the place where you were kicked.\n" + "You quickly found the person who hurt you.\n" + "Voice: Use your power and KILL HIM.\n" + "You unleashed a power that no human can comprehend.\n" + "The world turned into darkness...\n", 0.04)
    type_text("Thank you for playing the secret ending of the King.\n" + "If you want to play the main game, run this program again and write your name that is neither 'king' or 'King'.\n", 0.04)
    sys.exit()

def darkness_ending():
    type_text("\n" + "One day, in the village of Everpeace...\n" + "You went to the place where you fought the Dark Lord.\n" + name_dialogue + "This brings back memories...\n" + name_dialogue + "Here is where I fought the almighty Dark Lord.\n" + "Kids: Woahhhh\n" + "One kid: This just looks like a forest.\n" + name_dialogue + "When I defeated the Dark Lord, the palace and everything disappeared.\n" + "The kids were fascinated by your stories.\n" + "Soon, it was dark.\n" + "The kids went back to their homes.\n" + "You wanted to stay there a little longer.\n" + "Suddenly, you heard a sound near the bushes.\n" + name_dialogue + "Who's there?\n" + "Voice: Hahahahaha\n" + "Voice: Your story might have sounded better if you have killed me.\n" + "You see a dark figure coming out of the bushes.\n" + "There was no face.\n" + "It was just a shadow-like corpse walking towards you.\n" + name_dialogue + "Who are you?\n" + "Voice: You might have killed that weakling who goes by the name, Dark Lord.\n" + "Voice: But, I am his power.\n" + "Voice: I will destory everything in this world.\n" + name_dialogue + "Not unless I stop you first.\n" + "You blasted elements that you learned from years ago.\n" + "Shadow Figure: Hahahaha.\n" + "Shadow Figure: You think that is going to work?\n" + "Shadow Figure: Take this.\n" + "The shadow figure blinded you and binded you to the ground.\n" + "Shadow Figure: Hahahaha.\n" + "Slowly you felt your limbs getting cut off.\n" + "You screamed in pain.\n" + "Soon, you only had a head and your heart.\n" + "Shadow Figure: Say goodbye!\n" + "The shadow figure cut off your head...\n" + "\n" + "\n" + "..." + "\n" + "\n" + "You woke up sweating...\n" + "You started to wonder if your dead.\n" + "You looked around and saw that your still in your house.\n" + "So, it was a dream you thought to yourself.\n" + "You went back to sleep.\n" + "\n" + "\n" + "Was it a dream?\n" + "Its for you to decide.\n", 0.04)
    play_again()

#If name is king
if name in ["King", "king"]:
    king_name()
else:
    start_adventure()


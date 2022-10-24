import os, sys, time

def type(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n") 

def typeslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n") 

def intro():
    type("A group of goblins try to kill you, what do you do?")
    type("A. Accept your fate     B. Run     3. Fight them off")
    ans = input("> ")
    if ans.lower().startswith("a"):
        end_die()
    elif ans.lower().startswith("b"):
        run()
    elif ans.lower().startswith("c"):
        fight()

def run():
    type("You run and meet a group of mercenaries who ask what you're running from, you tell them the story. They offer to help when the goblins come back. ")
    type("Do you accept? (Y/N)")
    ans = input("> ")
    if ans.lower().startswith("y"):
        accept()
    else:
        end_home()

def accept():
    type("As you arrive at their home, you find out they have a lot of a familiar substance, you decide to stay with them for a bit, taking the substance as you talk.")
    time.sleep(1)
    type("After a while you tell them that you need to leave, they protest and ask you to stay a bit longer.")
    type("What will you do? leave or stay?")
    ans = input("> ")
    if ans.lower().startswith("l"):
        end_junk_leave()
    else:
        end_junk_stay()

def fight():
    type("You punch one of the goblins so hard the others flee out of fear")
    type("go after them? (Y/N)")
    ans = input("> ")
    if ans.lower().startswith("y"):
        chase()
    else:
        end_home()

def chase():
    type("You walk in the direction the goblins went to, you end up hearing sounds of civilization ")
    type("Do you go towards it? (Y/N)")
    ans = input("> ")
    if ans.lower().startswith("y"):
        civgo()
    else:
        end_lost()

def civgo():
    type("You see an entire goblin civilization, the leader spots you and sends a group of higher-ranking goblins to capture you.")
    type("A. Fight Them Off     B. Run Away     C. Let Yourself Be Captured")
    ans = input("> ")
    if ans.lower().startswith("a"):
        fightcapture()
    elif ans.lower().startswith("b"):
        runcapture()
    else:
        capture()

def fightcapture():
    type("You attempt to fight them off, but eventually you are overpowered and taken away.")
    end_locked_up()

def runcapture():
        type("You run until you cannot see the group following you.")
        type("A. Keep Running     B. Hide In Bushes And Wait")
        ans = input("> ")
        if ans.lower().startswith("a"):
            end_lost()
        else:
            hide()


def hide():
    type("You see them running past, but with 1 member less than you first saw. Without having time to process this, you hear something behind you, turn around and get knocked out by the (previously) missing member. ")
    end_locked_up()

def capture():
    type("while they take you away you pass out")
    end_locked_up()

def end_die():
    type("you fucking die")
    typeslow("The End.")
    time.sleep(1)
    type("Do you want to restart?")
    restart = input("> ")
    if restart.lower().startswith("y"):
        os.system("cls")
        intro()

def end_home():
    type("You go home after a long day, waiting for the hallucinations to end. ")
    typeslow("The End.")
    time.sleep(1)
    type("Do you want to restart?")
    restart = input("> ")
    if restart.lower().startswith("y"):
        os.system("cls")
        intro()

def end_junk_leave():
    type("You leave to return home, before you can enter your house, one of your neighbors asks you where you have been for the past 15 days. ")
    typeslow("The End.")
    time.sleep(1)
    type("Do you want to restart?")
    restart = input("> ")
    if restart.lower().startswith("y"):
        os.system("cls")
        intro()

def end_junk_stay():
    type("You decide to sleep there. You eventually wake up in a dumpster with a crudely stitched up 	wound on the left side of your chest, below your ribcage. They stole your fucking kidney ")
    typeslow("The End.")
    time.sleep(1)
    type("Do you want to restart?")
    restart = input("> ")
    if restart.lower().startswith("y"):
        os.system("cls")
        intro()

def end_locked_up():
    type("you wake up a few hours later in a jail cell, an officer tells you that you fought with another officer when they were investigating a disturbance about someone punching a kid.")
    type("He also 	informs you that you're being charged for assault and resisting arrest")
    typeslow("The End.")
    time.sleep(1)
    type("Do you want to restart?")
    restart = input("> ")
    if restart.lower().startswith("y"):
        os.system("cls")
        intro()

def end_lost():
    type("After walking for what seems like hours in the dark you collapse from exhaustion")
    type("Upon waking up you find yourself in a ditch next to a field, not knowing what had happened the day prior. You decide never to do drugs again ")
    typeslow("The End.")
    time.sleep(1)
    type("Do you want to restart?")
    restart = input("> ")
    if restart.lower().startswith("y"):
        os.system("cls")
        intro()

# if this seems like a very half-arsed story, it is. I'm about as good of a creative writer as a slightly overdate bowl of chicken noodle soup

intro()
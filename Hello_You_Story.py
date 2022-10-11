import time


def intro():
    print("A group of goblins try to murder you, what do you do?")
    print("A. Accept your fate     B. Run     3. Fight them off")
    ans = input("> ")
    if ans.lower().startswith("a"):
        end_die()
    elif ans.lower().startswith("b"):
        run()
    elif ans.lower().startswith("c"):
        fight()

def run():
    print("You run and meet a group of mercenaries who ask what you're running from, you tell them the story. They offer to help when the goblins come back. ")
    print("Do you accept? (Y/N)")
    ans = input("> ")
    if ans.lower().startswith("y"):
        accept()
    else:
        end_home()

def accept():
    print("As you arrive at their home, you find out they have a lot of a familiar substance, you decide to stay with them for a bit, taking the substance as you talk.")
    time.sleep(1)
    print("After a while you tell them that you need to leave, they protest and ask you to stay a bit longer.")
    print("What will you do? leave or stay?")
    ans = input("> ")
    if ans.lower().startswith("l"):
        end_junk_leave()
    else:
        end_junk_stay()

def fight():
    print("You punch one of the goblins so hard the others flee out of fear")
    print("go after them? (Y/N)")
    ans = input("> ")
    if ans.lower().startswith("y"):
        chase()
    else:
        end_home()

def chase():
    print("You walk in the direction the goblins went to, you end up hearing sounds of civilization ")
    print("Do you go towards it? (Y/N)")
    ans = input("> ")
    if ans.lower().startswith():
        civgo()
    else:
        end_lost()

def civgo():
    print("You see an entire goblin civilization, the leader spots you and sends a group of higher-ranking goblins to capture you.")
    print("A. Fight Them Off     B. Run Away     C. Let Yourself Be Captured")
    ans = input("> ")
    if ans.lower().startswith("a"):
        fightcapture()
    elif ans.lower().startswith("b"):
        runcapture()
    else:
        capture()

def fightcapture():
    print("You attempt to fight them off, but eventually you are overpowered and taken away.")
    end_locked_up()

def runcapture():
        print("You run until you cannot see the group following you.")
        print("A. Keep Running     B. Hide In Bushes And Wait")
        ans = input("> ")
        if ans.lower().startswith("a"):
            end_lost()
        else:
            hide()


def hide():
    print("You see them running past, but with 1 member less than you first saw. Without having time to process this, you hear something behind you, turn around and get knocked out by the (previously) missing member. ")
    end_locked_up()

def capture():
    print("while they take you away you pass out")
    end_locked_up()

def end_die():
    print("you fucking die")
    print("The End.")

def end_home():
    print("You go home after a long day, waiting for the hallucinations to end. ")
    print("The End.")

def end_junk_leave():
    print("You leave to return home, before you can enter your house, one of your neighbors asks you where you have been for the past 15 days. ")
    print("The End.")

def end_junk_stay():
    print("You decide to sleep there. You eventually wake up in a dumpster with a crudely stitched up 	wound on the left side of your chest, below your ribcage. They stole your fucking kidney ")
    print("The End.")

def end_locked_up():
    print("you wake up a few hours later in a jail cell, an officer tells you that you fought with another officer when they were investigating a disturbance about someone punching a kid.")
    print("He also 	informs you that you're being charged for assault and resisting arrest")
    print("The End.")

def end_lost():
    print("After walking for what seems like hours in the dark you collapse from exhaustion")
    print("Upon waking up you find yourself in a ditch next to a field, not knowing what had happened the day prior. You decide never to do drugs again ")
    print("The End.")

# if this seems like a very half-arsed story, it is. I'm about as good of a creative writer as a slightly overdate bowl of chicken noodle soup

intro()
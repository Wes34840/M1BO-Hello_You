from re import L
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
    elif ans.lower().startswith("a"):


intro()
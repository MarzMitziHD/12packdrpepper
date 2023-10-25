import os
import time

global consolas
consolas = ""

'''
And now, a wall of stupid idiots (affectionate) that have did the done that:
I’m gonna eat your balls. And all of your croutons. Mine now, bitch. - TEMPT8N



'''


def tengine(string="Sample Text", delay=0.05, sleepafter=0, noconsolasnewline=False):
    global consolas
    stringlist = [*string]
    i = 0
    print(f"DEBUGINFO\nI {i}\nSTRINGLIST {stringlist}\nSTRING {string}\nTIME {time}")
    yo = ""
    string_length = len(stringlist) - 1
    while i <= string_length:
        yo = yo + stringlist[i]
        i += 1
        os.system("clear")
        print(consolas + yo + "█")
        time.sleep(delay)
    if noconsolasnewline:
        consolas = consolas + yo
    else:
        consolas = consolas + yo + "\n"
    time.sleep(sleepafter)


def clearconsole():
    global consolas
    consolas = ""
    os.system("clear")


def load_list_from_txt(filename):
    try:
        file = open(filename, "r")
    except Exception as err:
        print('\n                                   +-+'
              '\n +----  +---+ +---+ +---+ +---+   ++#++'
              '\n |      |   | |   | |   | |   |  ++# #++'
              '\n +----  +--++ +--++ |   | +--++ ++## ##++'
              '\n |      |  |  |  |  |   | |  | -+#######++'
              '\n +----  |  +- |  +- +---+ |  +- #### ####|'
              '\n                                ----------+'
              f'\n{filename} could not be opened.'
              f'\n{err}'
              f'\nTHIS IS FATAL AS FUCK. YOU **NEED** THIS FILE OR YOU WILL **DIE**.'
              '\nEXITING.'
              )
        exit(1)
    output2 = file.readlines()
    # for i in range(len(output)):
    #     output2[i] = output2[i].removesuffix('\n')

    output = ''.join(output2)

    file.close()
    return output


tengine("Hello, player, to the \"Grab a 12-pack of Dr Pepper for your friend simulator\". Type your name.", 0.01)
name = input("--> ")
consolas = consolas + f"--> {name}\n"
tengine(f"Welcome, {name}. You are on a mission to grab Pop (or soda, if you're dumb) for your friend.", 0.01, 2)
tengine(f"Your friend asked you to grab a drink called \'Doctor Pepper\'. You have never tried this Pop before,", 0.01,
        0)
tengine(f"but, you might as well try it, since your friend has claimed it tasted good.", 0.01, 2)
tengine(f"Exploring around what seems to be a labyrinth of isles bring you nothing but crying children and", 0.01, 0)
tengine(f"the abhorrent screaming of old women yelling \"I WANT TO SPEAK TO YOUR MANAGER!\"", 0.01, 2)
tengine(f"Finally, after what seemed like an eternity but was really only a few minutes, you find the \"Pop\"", 0.01, 0)
tengine(f"isle. You walk to it and find a 12-pack of Doctor Pepper.", 0.01, 2)


def choiceno1():
    global consolas
    tengine(f"Will you grab it? (Choices: Y or N)", 0.01, 0)
    answer = input("--> ")
    consolas = consolas + f"--> {answer}\n"
    if answer == "Y":
        tengine(f"You grab the 12-pack of Doctor Pepper.", 0.01, 2)
    elif answer == "N":
        tengine(f"You don't grab the Doctor Pepper and instead just buy yourself a plain Monster Energy.", 0.01, 2)
        tengine(f"You have achieved the BAD ENDING. There is only 1 other ending.", 0.01, 2)
        exit()
    else:
        tengine("unknown answer, try again", 0.01)
        choiceno1()


choiceno1()

tengine(f"With the 12-pack of Doctor Pepper in one hand, and your Debit Card in the other, you go over to the", 0.01, 0)
tengine(f"cashier. You slot your Debit Card through the part of the card reader that wants you to swipe.", 0.01, 2)
tengine(f"Miraculously, the debit card actually gets read. Rarely, the store doesn't like to read debit cards,", 0.01,
        0)
tengine(f"so you had to swipe your backup Credit Card instead, but this time the Debit Card worked.", 0.01, 2)
tengine(f"The cashier says \"Have a nice day!\" when you walk out of the door. The cashier is kinda cute, albeit", 0.01,
        0)
tengine(f"he is a dude, but you blush a little as he says that.", 0.01, 2)
tengine(f"\nYou get in your car and drive home, the 12-pack of Doctor Pepper in the passenger's seat.", 0.01, 2)
tengine(f"You have achieved the GOOD ENDING. There is only 1 other ending.", 0.01, 2)

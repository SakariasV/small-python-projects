import random

def main():

    colors = ["Y","G","R","B"]
    codecolors = []
    makecode(colors, codecolors)


    while True:
        guess = get_guess()
        
        good_pos = check_color_position(codecolors, guess)
        if good_pos == len(codecolors):
            print(" You Win ")
        else:
            how_close(codecolors, guess, good_pos)


def check_color_position(codecolors, guess):
    count = 0
    loopcount = 0
    for x in guess:
        if codecolors[loopcount] == guess[loopcount]:
            count += 1
        loopcount += 1

    return count


def how_close(codecolors, guess, goodpos):
    realcount = 0
    for x in codecolors:
        count = 0
        for y in guess:
            if x == y:
                count += 1
            else:
                pass
        if count > 0:
            realcount += 1
    getback(realcount, goodpos)


def getback(count, goodpos):
    print(f"You got {goodpos} colors in the right spot")
    print(f"Youre guess has {count} matching colors")

def get_guess():
    guess = input("What do you want to guess?\n")
    guess.split(" ")
    return guess

def makecode(colors, codecolors):
    colorslen = len(colors)
    for i in range(0,colorslen):
        codecolors.append(colors[random.randint(0, colorslen - 1)])

    print(codecolors)
    


if __name__ == "__main__":
    main()
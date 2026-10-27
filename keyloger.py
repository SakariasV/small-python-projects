import keyboard


def main():

    count = 0

    while True:
        if keyboard.is_pressed('space'):
            count += 1
            print(count)



if __name__ == '__main__':
    main()
import keyboard
import time

def main():
    key = ''
    newkey = ''
    while True:
        newkey = keyboard.read_key()


        try:
            relese = keyboard.is_pressed(key)
            if relese == False:
                key = ''

        except:
            if key != newkey:
                print(newkey)
                key = newkey
        



if __name__ == '__main__':
    main()
import keyboard
import time

def main():
    key = ''
    newkey = ''
    wordlist = []
    
    while True:
        newkey = keyboard.read_key()


        try:
            relese = keyboard.is_pressed(key)
            if relese == False:
                key = ''

        except:
            
            try:
                if  newkey == 'backspace':
                    time.sleep(0.1)
                    wordlist.pop(1)
       
                elif newkey == 'enter':
                    print(wordlist)
                    wordlist = []

                elif  newkey == 'backspace':
                    pass

                elif newkey == 'space':
                    wordlist.append(" ")

                elif key != newkey:
                    wordlist.append(newkey)
                    key = newkey
            except:
                            pass
        



if __name__ == '__main__':
    main()
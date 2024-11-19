import pygame, time

pygame.mixer.init()
short_beep = pygame.mixer.Sound("morseshort.mp3")
long_beep = pygame.mixer.Sound("morselong.mp3")

MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'}

def play_morse(message):
    for x in message.upper():        # It loops through each uppercase letter in message
        if x in MORSE_CODE:     # checks to see if it exists in morse code
            for y in MORSE_CODE[x]:       # This loops through each symbol in the Morse code showing of x
                (short_beep if y == '.' else long_beep).play() # if its not short beep play long beep
                time.sleep(1)
            time.sleep(1) # time beetween

play_morse(input("What you wanna beep: "))

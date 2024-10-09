import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Uh oh, I'm falling in love", 0.098),
        ("Oh no," , 0.1),
        ("I'm falling in love again", 0.1),
        ("Oh", 0.2),
        ("I'm falling in love", 0.1),
        ("I thought the plane was going down", 0.08),
        ("How'd you turn it right around?", 0.1),
    ]

    delays = [1, 0.3, 0.5, 1, 0.2, 0.01, 0.1]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
    
print_lyrics()

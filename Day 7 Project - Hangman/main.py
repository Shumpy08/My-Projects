import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

name = ['abruptly',
        'absurd',
        'abyss',
        'affix',
        'askew',
        'avenue',
        'awkward',
        'axiom',
        'azure',
        'bagpipes',
        'bandwagon',
        'banjo',
        'bayou',
        'beekeeper',
        'bikini',
        'blitz',
        'blizzard',
        'boggle',
        'bookworm',
        'boxcar',
        'boxful',
        'buckaroo',
        'buffalo',
        'buffoon',
        'buxom',
        'buzzard',
        'buzzing',
        'buzzwords',
        'caliph',
        'cobweb',
        'cockiness',
        'croquet',
        'crypt',
        'curacao',
        'cycle',
        'daiquiri',
        'dirndl',
        'disavow',
        'dizzying',
        'duplex',
        'dwarves',
        'embezzle',
        'equip',
        'espionage',
        'euouae',
        'exodus',
        'faking',
        'fishhook',
        'fixable',
        'fjord',
        'flapjack',
        'flopping',
        'fluffiness',
        'flyby',
        'foxglove',
        'frazzled',
        'frizzled',
        'fuchsia',
        'funny',
        'gabby',
        'galaxy',
        'galvanize',
        'gazebo',
        'giaour',
        'gizmo',
        'glowworm',
        'glyph',
        'gnarly',
        'gnostic',
        'gossip',
        'grogginess',
        'haiku',
        'haphazard',
        'hyphen',
        'iatrogenic',
        'icebox',
        'injury',
        'ivory',
        'ivy',
        'jackpot',
        'jaundice',
        'jawbreaker',
        'jaywalk',
        'jazziest',
        'jazzy',
        'jelly',
        'jigsaw',
        'jinx',
        'jiujitsu',
        'jockey',
        'jogging',
        'joking',
        'jovial',
        'joyful',
        'juicy',
        'jukebox',
        'jumbo',
        'kayak',
        'kazoo',
        'keyhole',
        'khaki',
        'kilobyte',
        'kiosk',
        'kitsch',
        'kiwifruit',
        'klutz',
        'knapsack',
        'larynx',
        'lengths',
        'lucky',
        'luxury',
        'lymph',
        'marquis',
        'matrix',
        'megahertz',
        'microwave',
        'mnemonic',
        'mystify',
        'naphtha',
        'nightclub',
        'nowadays',
        'numbskull',
        'nymph',
        'onyx',
        'ovary',
        'oxidize',
        'oxygen',
        'pajama',
        'peekaboo',
        'phlegm',
        'pixel',
        'pizazz',
        'pneumonia',
        'polka',
        'pshaw',
        'psyche',
        'puppy',
        'puzzling',
        'quartz',
        'queue',
        'quips',
        'quixotic',
        'quiz',
        'quizzes',
        'quorum',
        'razzmatazz',
        'rhubarb',
        'rhythm',
        'rickshaw',
        'schnapps',
        'scratch',
        'shiv',
        'snazzy',
        'sphinx',
        'spritz',
        'squawk',
        'staff',
        'strength',
        'strengths',
        'stretch',
        'stronghold',
        'stymied',
        'subway',
        'swivel',
        'syndrome',
        'thriftless',
        'thumbscrew',
        'topaz',
        'transcript',
        'transgress',
        'transplant',
        'triphthong',
        'twelfth',
        'twelfths',
        'unknown',
        'unworthy',
        'unzip',
        'uptown',
        'vaporize',
        'vixen',
        'vodka',
        'voodoo',
        'vortex',
        'voyeurism',
        'walkway',
        'waltz',
        'wave',
        'wavy',
        'waxy',
        'wellspring',
        'wheezy',
        'whiskey',
        'whizzing',
        'whomever',
        'wimpy',
        'witchcraft',
        'wizard',
        'woozy',
        'wristwatch',
        'wyvern',
        'xylophone',
        'yachtsman',
        'yippee',
        'yoked',
        'youthful',
        'yummy',
        'zephyr',
        'zigzag',
        'zigzagging',
        'zilch',
        'zipper',
        'zodiac']

word = random.choice(name)
print(f"FOR TESTING PURPOSE \n The answer is: {word}\n")
lives = 6
word_len = len(word)

display = []
for blank in range(word_len):
    display += "_"

end = False

while not end:

    guess = input("Enter your guess: ")

    if guess in display:
        print(f"You have already guessed the letter {guess}. Choose another letter!")
    for position in range(word_len):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word:
        lives -= 1
        print("You guessed a wrong word, you lose 1 life.")
        if lives == 0:
            end = True
            print("You lose")

    if "_" not in display:
        end = True
        print("You win")
    print(display)

    print(stages[lives])

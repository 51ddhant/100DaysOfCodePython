welcome_message = '''
 _  _  ____  __     ___  __   _  _  ____    ____  __     _  _   __   __ _   ___  _  _   __   __ _  _  _  _   
/ )( \(  __)(  )   / __)/  \ ( \/ )(  __)  (_  _)/  \   / )( \ / _\ (  ( \ / __)( \/ ) / _\ (  ( \/ \/ \/ \  
\ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _)     )( (  O )  ) __ (/    \/    /( (_ \/ \/ \/    \/    /\_/\_/\_/  
(_/\_)(____)\____/ \___)\__/ \_)(_/(____)   (__) \__/   \_)(_/\_/\_/\_)__) \___/\_)(_/\_/\_/\_)__)(_)(_)(_)  '''

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

win_message = '''
 __   __  _______  __   __    _     _  _______  __    _  __   __   __  
|  | |  ||       ||  | |  |  | | _ | ||       ||  |  | ||  | |  | |  | 
|  |_|  ||   _   ||  | |  |  | || || ||   _   ||   |_| ||  | |  | |  | 
|       ||  | |  ||  |_|  |  |       ||  | |  ||       ||  | |  | |  | 
|_     _||  |_|  ||       |  |       ||  |_|  ||  _    ||__| |__| |__| 
  |   |  |       ||       |  |   _   ||       || | |   | __   __   __  
  |___|  |_______||_______|  |__| |__||_______||_|  |__||__| |__| |__| '''

lose_message = '''
 __   __  _______  __   __    ___      _______  _______  _______  __   __   __  
|  | |  ||       ||  | |  |  |   |    |       ||       ||       ||  | |  | |  | 
|  |_|  ||   _   ||  | |  |  |   |    |   _   ||  _____||_     _||  | |  | |  | 
|       ||  | |  ||  |_|  |  |   |    |  | |  || |_____   |   |  |  | |  | |  | 
|_     _||  |_|  ||       |  |   |___ |  |_|  ||_____  |  |   |  |__| |__| |__| 
  |   |  |       ||       |  |       ||       | _____| |  |   |   __   __   __  
  |___|  |_______||_______|  |_______||_______||_______|  |___|  |__| |__| |__| '''
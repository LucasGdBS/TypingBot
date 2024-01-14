'''Main file of the project. Run this file to start the program.'''
import os
from typing_bot import TypingBot

typeBot = TypingBot()

# https://typethealphabet.app
tempo1 = typeBot.write_alfabet()

# https://monkeytype.com
tempo2 = typeBot.monkey_type()

os.system('cls' if os.name == 'nt' else 'clear')
print(tempo1)
print(tempo2)

import sys

text = open('Text.txt')
print(len([i for i in text.split('. ', '! ', '? ')]))



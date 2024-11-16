class abc():
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning 

    def __str__(self):
        return self.word+'( '+self.meaning+' )'    
    
flash = []
print("welcomne to flashcard application")  

while True:
    word = input("enter the name you want to add to flashcard")
    meaning = input("enter the meaning of the word: ")

    flash.append(abc(word, meaning))
    option = int(input("enter 0 if you want another flashcard else 1"))

    if option:
        break 

print("\Your flashcards")
for i in flash:
     print(">", i)    
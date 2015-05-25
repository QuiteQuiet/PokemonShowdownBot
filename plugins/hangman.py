class Hangman:
    def __init__(self, phrase):
        self.solution = phrase
        self.guessed = ['/']
    def guessLetter(self, letter):
        if letter in self.guessed:
            return '{l} have already been tried'.format(l = letter)
        else:
            self.guessed.append(letter)
            if letter in self.solution.lower():
                return '**{l}** was a letter in the phrase!\n{redrawn}'.format(l = letter, redrawn = self.printCurGame())
            return '**{l}** is not in the phrase'.format(l = letter)
    def guessPhrase(self, phrase):
        if phrase.lower() == self.solution.lower():
            return True
        else:
            return False
    def getSolution(self):
        return self.solution
    def getFormatedPhrase(self):
        return ' '.join([l for l in self.solution.replace(' ','/')])
    def allLettersGuessed(self):
        for l in self.solution.replace(' ',''):
            if l not in self.guessed:
                return False
        return True
    def printCurGame(self):
        phrase = []
        for l in self.solution.replace(' ', '/'):
            phrase.append('_ '  if l.lower() not in self.guessed else l+' ')
        return ''.join(phrase)
        

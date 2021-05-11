'''Just guess a number and that number shuold be equal
to your preset number'''
class GuessNumber:
    ''' Main class'''
    def __init__(self,number,mn=0,mx=100):
        self.number = number
        self.guesses = 0
        self.mn = mn
        self.mx = mx
    
    def get_guess(self):
        ''' Getting input User Guess'''
        guess = input(f"Please guess the number from {self.mn} to {self.mx}")

        if self.isValidNumber(guess):
            return int(guess)
        else:
            print("Invalid Number, Please try again")
            return self.get_guess()
    def isValidNumber(self,str_number):
        '''Checking If Number is valid'''
        try:
            tmp = int(str_number)
        except:
            return False

        return self.mn<=tmp<=self.mx
    def play(self):
        ''' Running Function '''
        while True:
            self.guesses+=1

            guess = self.get_guess()

            if guess < self.number:
                print("Your Guess was under")
            elif guess > self.number:
                print("Your Guess was over")
            else:
                break
        print(f"YOOOOOOOOOOOOOOOO Nicee!,You guess it in {self.guesses} guesses!")

game = GuessNumber(50,0,100)
game.play()

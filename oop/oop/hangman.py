"""Hangman game class

This class needs to be able to:
    done - ask the user for a letter
    done - check that the input is a valid letter
    done - test if the input is actually a phrase or a letter
    done - allow the user to guess the phrase
    done - convert the phrase to a hidden string composed of "_ " per letter
    done - test the inputted letter against the phrase and return the position in the string
    done - test the inputted letter and add it to the list of guessed letters that are correct


    seems to work apart from inputting the whole phrase
    and the scoring is 'wrong'


    done - regenerate the hidden phrase with guessed letters visible
    done - output the phrase with guessed letters visible and non-guessed letters hidden by a -
    iffy - count the number of errors and give the user a running score against the maximum allowed errors
    iffy - end the game if the number of errors is greater than the maximum
    fail - end the game if the user guesses the phrase
"""

from oop.base import Base


class Hangman(Base):
    def __init__(self, phrase):
        try:
            self.phrase = phrase
            self.hiddenphrase = self.hidePhrase()
            self.score = 0
            self.maxtries = 10
            self.guessedletters = []
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            print(msg)
            raise

    def hidePhrase(self):
        try:
            tmp = self.phrase.split()
            xtmp = []
            for w in tmp:
                xtmp.append("_ " * len(w))
            return "   ".join(xtmp)
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            print(msg)
            raise

    def askQ(self, prompt):
        try:
            didwewin = False
            xin = input(prompt + " > ")
            if self.testInputIsPhrase(xin):
                # print(f"input {xin} is detected as a phrase")
                if self.testInputIsThePhrase(xin):
                    # print(f"input {xin} is detected as THE phrase")
                    return True
            # print(f"Testing input to check it is a single letter {xin}")
            if self.testInputIsLetter(xin):
                # print(f"input {xin} is a single letter")
                didwewin = self.evaluateGame(xin)
                # pos = self.phrase(xin)
                # if pos > -1:
                #     tmp = list(self.phrase)

                #     pass
            return didwewin
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            print(msg)
            raise

    def testInputIsLetter(self, xin):
        try:
            llist = [chr(x) for x in range(ord("a"), ord("z") + 1)]
            # print(f"is {xin} in {llist}")
            tin = xin.lower()
            # print(f"len input: {len(tin)}")
            if len(tin) == 1 and tin in llist:
                return True
            return False
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            print(msg)
            raise

    def testInputIsPhrase(self, xin):
        try:
            if len(xin) == 1 or len(xin) == 0:
                return False
            return True
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            print(msg)
            raise

    def testInputIsThePhrase(self, xin):
        try:
            if xin.lower().strip() == self.phrase.lower().strip():
                return True
            return False
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            print(msg)
            raise

    def evaluateGame(self, iletter):
        try:
            if iletter in self.guessedletters:
                # print(f"iletter is already guessed {iletter}")
                return False
            if iletter.lower() in self.phrase.lower():
                self.guessedletters.append(iletter)
            else:
                self.score += 1
            check = self.testGuesses()
            opch = " ".join(check)
            print(f"\n{opch}\n")
            return False if "_" in check else True
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            print(msg)
            raise

    def testGuesses(self):
        try:
            check = []
            for letter in self.phrase.lower():
                if letter in self.guessedletters:
                    check.append(letter)
                elif letter == " ":
                    check.append(" ")
                else:
                    check.append("_")
            return check
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            print(msg)
            raise

"""Hangman game class

This class needs to be able to:
    done - ask the user for a letter
    done - check that the input is a valid letter
    done - test if the input is actually a phrase or a letter
    done - allow the user to guess the phrase
    test the inputted letter against the phrase
    output the phrase with guessed letters visible and non-guessed letters hidden by a -
    count the number of errors and give the user a running score against the maximum allowed errors
    end the game if the number of errors is greater than the maximum
    end the gaim if the user guesses the phrase
"""

from oop import Base


class Hangman(Base):
    def __init__(self, phrase):
        try:
            self.phrase = phrase
            self.score = 0
            self.maxtries = 10
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
            xin = input(prompt + " > ")
            if self.testInputIsPhrase(xin):
                if self.testInputIsThePhrase(xin):
                    return True
            if self.testInputIsLetter(xin):
            return True
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
            llist = [x for x in range(ord("a"), ord("z") + 1)]
            tin = xin.lower()
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

    def testLetterInPhrase(self, xin):
        try:
            tphrase = list(self.phrase)
            if xin in tphrase:
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
            if xin == self.phrase:
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

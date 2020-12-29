# Countdown Word Solver

## Lesson 1

* Reading parameters to programs using sys.argv.
* Reading files with a context manager.
* Error checking with exception handling.

## Lesson 2

* Read the whole file as one long string.
* Split the file at line endings using list comprehension.
* Note the empty string at the end of the list.
* Note the use of a negative list slice parameter.

## Lesson 3

* Show how to sort words by length, store the result in a dictionary.
* How to only use a subset of all word lengths (in this case words between 4
  and 9 characters long).
* toptail function to show the 1st and last word for each length.
* Number formatting rules.

## Lesson 4

* anagram solver `testWord`.
* How to copy a string to a list, each char. being one member of the list.
* How to remove members from a list.

## Lesson 5

* Create a possible optimisation for later use by sorting the words not only
  by length but by starting letter.
* Introduce the `chr()` and `ord()` functions.
* Tidy up the `sortWordsByLength` function.

## Lesson 6

* Show how 'tricky' outputs are documented in function doc-strings.
* A further optimisation is to remove all words in the dictionary that don't
  begin with a letter that is in the input set.
* New file `countdown.py` - this will be our application file.
* Create a random letter generating function that can differentiate between
  vowels and consonents.
* Create a generic keyboard input function that outputs a message and reads
  the users keyboard.
* Make the file executable by setting the `x` flag and inserting a
  'hash-bang' at the top of the file.
* Test the `rndLetter()` function in the file execution section.

## Lesson 7

* Place holder function `outputCheck()` that displays the input set.
* Start the `countdown()` function by setting up the dictionary of words.
* Obtain input from the user - give the choice of number of
  vowels/consonents, vowel or consonent one by one, or inputting the actual
  letter required.

## Lesson 8

* show how to generate a list of numbers as strings.
* Show fuller function doc-strings.
* `generateCheck()` function to make a random list of consonents and vowels.
* Show how to convert between list and string and back again.
* How to raise an error.
* Generate random input for the game.

## Lesson 9

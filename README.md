# Wordle-Solver
Retrieve all the words that are possible with the data you already have in wordle\

If you have a letter that has to be excluded then you need to add it like this:\
```python
addLetter("the letter", 0)
```
\
If you have a letter that is in the right spot is should be like this:\
```python
addLetter("the letter", the position, False, True)
```
\
If you have a letter that is in the final word but not in the right spot it should be like this:\
```python
addLetter("the letter", the position, False, False)
```
\
the first parameter is the letter you want to add,\
the second parameter is the position the letter is at,\
the third parameter is if the letter should be excluded, this means that the letter is not in the final word,\
the fourth paramter is if the letter is in the correct place\

# Example

```python
addLetter("g", 0)
addLetter("r", 1, False, True)
addLetter("i", 2, False, True)
addLetter("p", 3)
addLetter("s", 4, False, False)
```

This is means:\
"g" isn't in the final word,\
"r" is in the right spot,\
"i" is in the right spot,\
"p" isn't in the final word,\
"s" isn't in the right spot, but is somewhere in the final word

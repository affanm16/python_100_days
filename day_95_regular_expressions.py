"""
***Regular Expressions in Python***
=>Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python.
 They allow you to match and manipulate strings based on patterns, making it easy to perform complex string
  operations with just a few lines of code.

***Metacharacters in regular expressions***
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE
    to match.
()  Enclose a group of REs

=>Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

***Importing re Package****
=>In Python, regular expressions are supported by the re module.
 The basic syntax for working with regular expressions in Python is as follows:
import re

***Searching for a pattern in re using re.search() Method***
re.search() method either returns None (if the pattern doesn’t match),
 or a re.MatchObject that contains information about the matching part of the string.
  This method stops after the first match, so this is best suited for testing a regular expression more than
   extracting data.
   We can use re.search method like this to search for a pattern in regular expression:

# Define a regular expression pattern
pattern = r"expression"
# Match the pattern against a string
text = "Hello, world!"
match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")

Searching for a pattern in re using re.findall() Method
You can also use the re.findall function to find all occurrences of the pattern in a string:

import re
pattern = r"expression"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)
# Output: ['cat', 'hat']

Replacing a pattern
The following example shows how to replace a pattern in a string:

import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)
# Output: ['cat', 'hat']
new_text = re.sub(pattern, "dog", text)
print(new_text)
# Output: "The dog is in the dog."

Extracting information from a string
The following example shows how to extract information from a string using regular expressions:

import re
text = "The email address is example@example.com."
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    email = match.group()
    print(email)
# Output: example@example.com

Conclusion
Regular expressions are a powerful tool for working with strings and text data in Python.
Whether you're matching patterns, replacing text, or extracting information, regular expressions make it easy
to perform complex string operations with just a few lines of code.
With a little bit of practice, you'll be able to use regular expressions to solve all sorts of
 string-related problems in Python.
"""
import re
# pattern="was"
text='''India's Population, as on 1 March 2011 stood at 1,210.9 million (623.2 million males and 587.6 million females) in
compared to a total of 1, 028, 737, 436 in the year 2001. In absolute term, the population of India has 
increased by more than 181 million during the decade 2001-2011.

The Population at the turn of the twentieth century was around 238.4 million.
It has grown steadily at each decennial census from 1901, except for a decrease during 1911-21.

Uttar Pradesh is the most Populous state in the country with almost 200 million people. 
Sikkim is the least populous state with 6,07,688 people.'''
pattern=r"[A-Z]+opulation"#+searches for all
# match=re.search(pattern,text)#check wether patter exists or not here 'was'
# print(match)
matches=re.finditer(pattern,text)
for match in matches:
    print(match)
    print(type(match.span))

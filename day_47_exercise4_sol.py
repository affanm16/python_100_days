# st=input("input the message")
# words=st.split(" ")#splits into single tokens
# coding=True
# if(coding):
#     new_words=[]#empty string
#     for word in woArds:
#         if(len(word)==3):
#             r1="fhj"#three random letters
#             print(type(r1))
#             r2="uil"#three random words
#             new_st=r1+word[1:]+word[0]+r2
#             new_words.append(new_st)
#         if(len(word)==4):
#             r1="rly"
#             r2="aln"
#             new_st=r1+word[1:]+word[0]+r2
#             new_words.append(new_st)
#
#         else:
#             new_words.append(word[::-1])#reversing
#
#     print(" ".join(new_words))
#
#
#
#
import random
import string

letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(3))

print(random_string)
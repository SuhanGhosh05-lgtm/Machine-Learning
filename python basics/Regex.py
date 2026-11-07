#Regex (Regular Expression) is used to search, match, validate, and manipulate patterns in text/ large datas.
#it checks the input given by user and matches with the expectation of whaat it should be
import re

#re functions:-
#1---> re.search('pattern','string')
print(re.search('flo','flower'))
print(re.search('glo','flower'))

#2---> re.match('pattern','string')
print(re.match('su','suhan'))

#3---> re.findall('pattern','string')
print(re.findall('suh','abcde'))
print(re.findall('cde','abcde'))

#4---> re.sub('string present in string','string u want to replace with','string')
print(re.sub('abc','suhan','abcshrayasi'))

#5---> to find digits from an entire texts
text="my name is 123 and ph is 432"
digits=re.findall(r"\d+",text) #\d+=digits
print(digits)

#6---> to remove spaces from texts
hehe="suhan shrayasi"
space=re.sub(r"\s","+",hehe) #\s=space, 
print(space)

fuck=" hehe is a fucking impossible thing"
fuck_replace=re.sub(r"fucking","f*cking",fuck)
print(fuck_replace)

#extracting email id
mail="contact me at suhanghosh92@gmail.com"
email=re.findall(r"[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,}",mail)
print(email)

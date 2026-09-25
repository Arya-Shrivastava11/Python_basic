str1='today is a good day'
vowels=[]
consonants=[]
for c in str1:
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        vowels.append(c)
    else:
        consonants.append(c)
print(len(vowels))
print(len(consonants))
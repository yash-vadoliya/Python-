# 15. Create an empty dictionary, Insert some Roll:Name into it. i). Retrieve 5th value using key, ii). Retrieve all the roll numbers, iii). Retrieve all the names, iv). Change the name of the student having roll no. 7, v). Remove roll no 9, vi). Display the dictionary.

sdict = {}

sdict = {
    1: 'Yash',
    2: 'Dhaval', 
    3: 'Mahaveer', 
    4: 'Mukesh', 
    5: 'Jay', 
    6: 'Abhi',
    7: 'Keval',
    8: 'Rahul',
    9: 'Raj',
    10: 'Kevin'
}

# i). Retrieve 5th value using key
print(sdict.get(5))

# ii). Retrieve all roll numbers
rno = list(sdict.keys())
print(rno)

# iii). Retrieve all names
nm = list(sdict.values())
print(nm)

# iv). Change the name of the student with roll no. 7
sdict[7] = 'Ram'

# v). Remove roll no. 9
sdict.pop(9)

# vi). Display the dictionary
print(sdict)
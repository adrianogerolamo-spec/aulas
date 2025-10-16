import re
#https://www.w3schools.com/python/python_regex.asp
'''
with open("Python_07_nobody.txt", "r") as file:
    result = re.search(r'Nobody', file)
    print(result)
'''
email = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_.-]+$'
e1 = "aaaaa@agemail.com"
print(re.search(email, e1))

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

x = 1
def change_x(x):
    x = 3
    
    return x
print(x)
print(change_x(x))
print(x)

def change_new(n):
    n=n-1
    return n
n=20
print(n)
print(change_new(n))
print(n)

dic_dic = []
data = input("type the file name: ")
with open(data, "r")as file:
    m = 1
    for line in file:
        dic_dic.append([m, line])
        m += 1
print(dic_dic)

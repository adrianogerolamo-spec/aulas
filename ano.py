import sys
ano = int(sys.argv[1])
if ano%400 == 0:
    print("o ano é bissexto!")
elif ano%4 == 0 and ano%100 != 0:
    print("o ano é bissexto!")
else:
    print("o ano não é bissexto")

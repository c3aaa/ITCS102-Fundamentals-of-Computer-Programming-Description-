cash = eval(input("Enter total deposit amount..."))

onethousand = 1000
fivehundred = 500
twohundred = 200
onehundred = 100
fifty = 50
twenty = 20
ten = 10
five = 5
one = 1

onethousand1 = cash // onethousand
cash = cash % onethousand

fivehundred5 = cash // fivehundred
cash = cash % fivehundred

twohundred2 = cash // twohundred
cash = cash % twohundred

onehundred1 = cash // onehundred
cash = cash % onehundred

fifty5 = cash // fifty
cash = cash % fifty

twenty2 = cash // twenty
cash = cash % twenty

ten1 = cash // ten
cash = cash % ten

five5 = cash // five
cash = cash % five

one1 = cash // one
cash = cash % one

print("1000", "-" , onethousand1)
print("500", "-" , fivehundred5)
print("200", "-" , twohundred2)
print("100", "-" , onehundred1)
print("50", "-" , fifty5)
print("20", "-" , twenty2)
print("10", "-" , ten1)
print("5", "-" , five5)
print("1", "-" , one1)

#print("asawa pa rin ni yiran")
a=int(input("enter the marks :"))
print("ur marks is :",a)
if a > 90 :
	print("grade :A")
elif a < 90 and a > 80:
	print("grade :B")
elif a < 80 and a > 74:
	print("grade :C")
elif a < 74 and a > 35:
	print("grade :D")
else:
	print("fail")
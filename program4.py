names = ["john", "joy", "jaya"]
print(names)
names.remove("joy")
print(names)
names.append("jonny")
print(names)
names.insert(2, "jemmy")
print(names)
names.reverse()
print(names)
print()

digits = [0,1,2,3,4,5,6,7,8,9]
print(digits[0:6]) # 0 thke 6 er ag porjnto index er sob digit gulo print krbe
print(digits[6:]) # 6 thke baki sob print krbe
print(digits[0:10:2]) # 2 ghor jump kre print krbe
print(digits[0:10:3]) # 3 ghor jump kre print krbe
print(digits[-1]) # last number print krbe
print(digits[::-1]) # reversely sob print krbe
print(digits[::-2]) # reversely 2 ghor jump kre sob print krbe
print(digits[5:0:-2])
print(digits[0:-2:5])
print()

for i in range(len(digits)):
    print(digits[0:i])
    print()

window_size = 7
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])

    print()

problem = 'broke, pale, short, nearby'
print(problem)


'''f_name = "Ada "
l_name= "Lovelace"
fullname = f_name + l_name
print(fullname)
print("hello, " + fullname.title() + "!")
print(fullname.upper())
print(fullname.lower())
'''

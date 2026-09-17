str = "Abhilash nayak"
print(str[-2:-1])
print(str[::-1])
print(str[-1:-6:-1])
del str[-1:-5:2]
print(str)
str = 'abhialsh'
print(len(str+ " " +"nayak"))
print(str)

str = "Abhilash Nayak"
print(max(str))
print(min(str))
print(len(str))
print(sorted(str,reverse=True))
print(str.capitalize())
print(str.title())
print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.count("a"))
print(str.find("a"))
name = "Abhilash"
age = "23"

print("my name is {} and my age is {}".format(name,age))
s = "abhilash is my name and my age is 23"
print(s.split(" "))
print(s.join("-"))
print("-".join(['abhilash', 'is', 'my', 'name', 'and', 'my', 'age', 'is', '23']))
print("abhilash nayak is my name ".replace("abhilash","nayak"))

# creating strings in python and know how many methods to crate strings
# single inverted comma strings
s = 'hello_world'
print(s)
# dubble inverted comma strings
s = "hello_world"
print(s)
# both of single and double inverted comma string using in special cases such like ->"it's rainind outside"
# tripple inverted comma strings
s = """hello_world"""
print(s)
# using for multiline strings 
# Accessing substrings from a string :
# Postive indexing
s = "HELLO_WORLD"
print(s[0])
# output wii be H
# Negative indexing:
s = "HELLO_WORLD"
print(s[-1])
# output will be D
# Strings Sliceing:
s = "HELLO_WORLD"
print(s[0:5]) 
# output will be HELLO
s = "HELLO_WORLD"
print(s[0:])
# output will be 0 index to last_index print -HELLO_WORLD
s = "HELLO_WORLD"
print(s[2:])
# output will be 2nd index to last_index - LLO_WORLD
# basically we have another method like
s = "HELLO_WORLD"
print(s[:6]) 
# this program output will be 0 to 5 last one number is exclude -HELLO_
# Now we are studing step size in string
s = "HELLO_WORLD"
print(s[0::2])
# output will be - HLOWRD
# this progarm have 2 step size
# Negative Slicing
s = "hello_anhi"
print(s[7:0:-1])
# always remember negative indexing is always start with higher no and lower no
# # this programing code for revers the entire string
s = "hello_abhi"
print(s[::-1])
# output is ihba_olleh
# Neagtive stepsize in string
s = "HELLO_WORLD"
print(s[10:2:-1])
# output is DLROW_OL
# print only world
s = "hello_world"
print(s[-5:])
s = "hello_world"
print(s[-1:-11:-2])

word = "PROGRAMMING"

# Question 1: Positive Slicing
# Predict the output of: word[3:8]
print(word[3:8])

# Question 2: Negative Slicing
# Predict the output of: word[-7:-3]
print(word[-7:-3])

# Question 3: Step Size Slicing
# Predict the output of: word[1:9:3]
print(word[1:9:3])

# Question 4: Negative Slicing with Missing Bounds (End tak jana)
# Predict the output of: word[-5:]
print(word[-5:])

# Question 5: Advanced Reverse Slicing with Step
# Predict the output of: word[::-2]
print(word[::-2])
word = "ELECTRONICS"

# Question 1: Basic Negative Slicing
# Predict the output of: word[-9:-4]
print("Q1:", word[-9:-4])

# Question 2: Negative Slicing till the End (Stop missing)
# Predict the output of: word[-5:]
print("Q2:", word[-5:])

# Question 3: Negative Slicing from the Start (Start missing)
# Predict the output of: word[:-6]
print("Q3:", word[:-6])

# Question 4: Negative Slicing with Positive Step Size
# Predict the output of: word[-10:-2:2]
print("Q4:", word[-10:-2:2])

# Question 5: Negative Slicing with Negative Step Size (Reverse direction)
# Predict the output of: word[-2:-8:-1]
print("Q5:", word[-2:-8:-1])
word = "BERHAMPUR"

# Question 1: Positive Start, Negative Stop
# Predict the output of: word[2:-2]
print("Q1:", word[2:-2])

# Question 2: Negative Start, Positive Stop with Step
# Predict the output of: word[-8:6:2]
print("Q2:", word[-8:6:2])

# Question 3: Reverse Slicing with specific bounds
# Predict the output of: word[-2:2:-1]
print("Q3:", word[-2:2:-1])

# Question 4: Missing bounds with a Negative Step
# Predict the output of: word[::-3]
print("Q4:", word[::-3])
file = input("Enter the file name ->")
new_file = file[-3:]
print(new_file)
file = input("Enter the year file ->")
new_year_file = file[-8:-4]
print(new_year_file)
s = "Abhilash_Nayak"
del s
print(s)



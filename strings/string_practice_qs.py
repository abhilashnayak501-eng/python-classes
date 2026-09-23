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
s = "hello_abhi"
print(s[::-1])


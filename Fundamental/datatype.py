# List
x = [1, 2, 3, 4, 5, 6]
print(len(x))

x[:3]   #[1, 2, 3]
x[3:]   #[4, 5, 6]
x[-2:]  #[5, 6]

x.extend([7,8])   #[1, 2, 3, 4, 5, 6, 7, 8]
x.append(9)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]

y = [10, 11, 12]
listOfLists = [x, y]   #[[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12]]

z = [3, 2, 1]
z.sort()  # in-place sort by default, [1, 2, 3]
z.sort(reverse=True)   #[3, 2, 1]

# Tuple
x = (1, 2, 3)
len(x)   #3

y = (4, 5, 6)
y[2]   #6

listOfTuples = [x, y]   #[(1, 2, 3), (4, 5, 6)]

(age, income) = "32,120000".split(',')
print(age)    #32
print(income)      #120000

# Dictionaries
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print(captains["Voyager"])     #Janeway
print(captains.get("Enterprise"))     #Kirk
print(captains.get("NX-01"))             #None

















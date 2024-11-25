keys1 =[]
vals1 = []
num1 = int(input("Enter the Number of elements for Dictionary-1: "))
print("Enter Values for Keys")
for i in range(0, num1):
  x = str(input("Enter Key " + str(i + 1) + "=")) 
  keys1.append(x)
print("Enter Values for Values")
for i in range(0, num1):
  x = str(input("Enter Value "+ str(i + 1) +"=")) 
  vals1.append(x)
dict1 = dict(zip(keys1, vals1))
print("Dictionary_1 Items:", dict1)
set1 = set(dict1.keys())
keys2 = []
vals2 =[]
num2 = int(input("Enter the Number of elements for Dictionary-2: "))
print("Enter Values for Keys")
for i in range(0, num2):
  y = str(input("Enter Key " + str(i + 1) + "=")) 
  keys2.append(y)
print("Enter Values for Values")
for i in range(0, num2):
   y = str(input("Enter Value " + str(i + 1) + "=")) 
   vals2.append(y)
dict2= dict(zip(keys2, vals2))
print("Dictionary_2 Items:", dict2)
set2 = set(dict2.keys())
common_items = set1 & set2
print("Common items from dictionary 1 and dictionary 2:", common_items)

list_v1 = []

for numbers in range(1,11):
    list_v1.append(numbers)
    
print(list_v1)

list_v2 = [numbers  for numbers in range(1,11)]
print(list_v2)
numbers = [5, 3, 4, 2, 1]
strs = ['aaa', 'ccc', 'bbb', '한글', '세종대왕']
sort_numbers = sorted(numbers)     # cf. reversed(numbers)
print("sort_numbers=", sort_numbers)
print("numbers=", numbers)

print("QQQ>>", sorted(strs))

numbers.sort()
print("asc>>", numbers)

numbers.sort(reverse=True)
print("desc>>", numbers)

t = (1,5,3)
print("QQQ>>", sorted(t))
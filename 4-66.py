char = "1"
output = ""

for i in range(10):
    j = 0
    while j < len(char):
        curr = char[j]
        count = 1
        while j+1 < len(char) and curr == char[j+1]:
            count += 1
            j += 1
        output += curr + str(count)
        j += 1
    print (output)
    char = output
    output = ""



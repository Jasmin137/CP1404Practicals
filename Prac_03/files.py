# FILES

# 1.
out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()

# 2.
out_file = open("name.txt", "r")
out_file.readline()
print(f"Your name is {name}")
out_file.close()

# 3.
out_file = open("numbers.txt", "r")
number = out_file.readlines()
total = int(number[0]) + int(number[1])
print(total)
out_file.close()

# 4.
out_file = open("numbers.txt", "r")
total = 0
for line in out_file:
    total += int(line)
print(total)
out_file.close()

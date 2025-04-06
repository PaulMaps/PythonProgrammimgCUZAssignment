names = ['Anesu', 'Paul', 'Ashwens', 'Angelyn', 'Mel']

with open('names.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')


# Step 1: List of names
names = ['Anesu', 'Mel', 'Ashwens', 'Tariro', 'Kuda']

# Step 2: Write names to a file
with open('names.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')

# Step 3: Read and print names from the file
with open('names.txt', 'r') as file:
    for line in file:
        print(line.strip())

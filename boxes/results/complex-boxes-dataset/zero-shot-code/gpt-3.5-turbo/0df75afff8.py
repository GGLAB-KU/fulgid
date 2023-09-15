box0 = ['camera']
box1 = ['phone', 'brush', 'tiger', 'fork', 'dress']
box2 = ['keyboard', 'desert']
box3 = ['planet', 'basket']
box4 = ['shirt', 'snow']

# Swap dress in Box 1 with desert in Box 2
box1.remove('dress')
box2.remove('desert')
box1.append('desert')
box2.append('dress')

# Replace snow and shirt with bracelet and key in Box 4
box4.remove('shirt')
box4.remove('snow')
box4.append('bracelet')
box4.append('key')

# Remove bracelet and key from Box 4
box4.remove('bracelet')
box4.remove('key')

# Swap keyboard in Box 2 with planet in Box 3
box2.remove('keyboard')
box3.remove('planet')
box2.append('planet')
box3.append('keyboard')

# Remove keyboard from Box 3
box3.remove('keyboard')

# Put flower, oven, and branch into Box 2
box2.append('flower')
box2.append('oven')
box2.append('branch')

# Remove tiger, brush, and desert from Box 1
box1.remove('tiger')
box1.remove('brush')
box1.remove('desert')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
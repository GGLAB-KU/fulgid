box_0 = ['scarf', 'ocean', 'octopus', 'pants', 'freezer']
box_1 = ['branch', 'telescope']
box_2 = ['coat', 'bowl', 'shirt']
box_3 = ['rocket', 'boot', 'shelf', 'toothbrush']
box_4 = []
box_5 = ['car']
box_6 = ['tape', 'beach', 'dog', 'sun', 'console']
box_7 = ['rain', 'laptop']
box_8 = ['keyboard', 'cow']
box_9 = []

# Remove the beach and the dog from Box 6
box_6.remove('beach')
box_6.remove('dog')

# Move the sun and the console and the tape from Box 6 to Box 4
box_4.extend(['sun', 'console', 'tape'])
box_6.remove('sun')
box_6.remove('console')
box_6.remove('tape')

# Move the keyboard and the cow from Box 8 to Box 4
box_4.extend(['keyboard', 'cow'])
box_8.remove('keyboard')
box_8.remove('cow')

# Replace the cow and the console and the keyboard with the gloves and the comet and the branch in Box 4
box_4.remove('cow')
box_4.remove('console')
box_4.remove('keyboard')
box_4.extend(['gloves', 'comet', 'branch'])

# Swap the tape in Box 4 with the branch in Box 1
box_4.remove('tape')
box_1.remove('branch')
box_4.append('branch')
box_1.append('tape')

# Put the keyboard into Box 5
box_5.append('keyboard')

# Remove the sun and the branch from Box 4
box_4.remove('sun')
box_4.remove('branch')

# Move the shelf and the boot from Box 3 to Box 1
box_1.extend(['shelf', 'boot'])
box_3.remove('shelf')
box_3.remove('boot')

# Empty Box 1
box_1 = []

# Swap the car in Box 5 with the gloves in Box 4
box_5.remove('car')
box_4.remove('gloves')
box_5.append('gloves')
box_4.append('car')

# Move the rain from Box 7 to Box 4
box_4.append('rain')
box_7.remove('rain')

# Put the shorts and the coral into Box 4
box_4.extend(['shorts', 'coral'])

# Remove the laptop from Box 7
box_7.remove('laptop')

# Move the bowl from Box 2 to Box 5
box_5.append('bowl')
box_2.remove('bowl')

# Remove the bowl and the gloves and the keyboard from Box 5
box_5.remove('bowl')
box_5.remove('gloves')
box_5.remove('keyboard')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)
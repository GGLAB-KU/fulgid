box0 = ['spoon', 'rocket', 'fish', 'plate']
box1 = ['zipper']
box2 = ['bird']
box3 = ['ocean', 'belt', 'star', 'island', 'flower']
box4 = ['dice', 'coat', 'drum']

# Remove items from Box 3
box3.remove('star')
box3.remove('island')
box3.remove('belt')

# Move items from Box 4 to Box 2
box2.extend(box4)
box4.clear()

# Add items to Box 3
box3.extend(['charger', 'blanket', 'tape'])

# Remove ocean from Box 3
box3.remove('ocean')

# Replace zipper with charger in Box 1
box1[0] = 'charger'

# Empty Box 1
box1.clear()

# Remove blanket from Box 3
box3.remove('blanket')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
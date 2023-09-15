box0 = ['storm']
box1 = ['button', 'telescope']
box2 = ['rock', 'zipper']
box3 = ['blanket']
box4 = ['meteor', 'plane', 'lipstick', 'freezer']

# Swap button in box1 with meteor in box4
box1.remove('button')
box4.remove('meteor')
box1.append('meteor')
box4.append('button')

# Remove rock from box2
box2.remove('rock')

# Replace telescope and meteor with hat and jungle in box1
box1.remove('telescope')
box1.remove('meteor')
box1.append('hat')
box1.append('jungle')

# Put shampoo, coral, and boat into box4
box4.append('shampoo')
box4.append('coral')
box4.append('boat')

# Remove freezer, coral, and lipstick from box4
box4.remove('freezer')
box4.remove('coral')
box4.remove('lipstick')

# Swap storm in box0 with button in box4
box0.remove('storm')
box4.remove('button')
box0.append('button')
box4.append('storm')

# Put controller, star, and vase into box0
box0.append('controller')
box0.append('star')
box0.append('vase')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
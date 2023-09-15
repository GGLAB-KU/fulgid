box_0 = ['keyboard', 'plate']
box_1 = ['dog', 'forest', 'pen']
box_2 = ['tiger', 'toaster', 'razor', 'shoe']
box_3 = ['oven', 'hat', 'branch']
box_4 = ['jacket', 'lock']

# Move the hat from Box 3 to Box 1
box_1.append(box_3.pop(box_3.index('hat')))

# Replace the branch and the oven with the toaster and the key in Box 3
box_3.remove('branch')
box_3.remove('oven')
box_3.extend(['toaster', 'key'])

# Move the dog and the pen and the hat from Box 1 to Box 3
box_3.extend([box_1.pop(box_1.index('dog')), box_1.pop(box_1.index('pen')), box_1.pop(box_1.index('hat'))])

# Put the swimsuit and the table into Box 2
box_2.extend(['swimsuit', 'table'])

# Replace the jacket with the grass in Box 4
box_4[box_4.index('jacket')] = 'grass'

# Remove the forest from Box 1
box_1.remove('forest')

# Replace the dog and the pen and the key with the guitar and the scissors and the submarine in Box 3
box_3.remove('dog')
box_3.remove('pen')
box_3.remove('key')
box_3.extend(['guitar', 'scissors', 'submarine'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
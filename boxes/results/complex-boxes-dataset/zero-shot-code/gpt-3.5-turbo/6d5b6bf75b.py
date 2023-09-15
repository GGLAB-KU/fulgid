box0 = []
box1 = ['needle', 'ring', 'boot']
box2 = ['book']
box3 = ['bracelet', 'thread', 'whistle']
box4 = []
box5 = ['beach', 'octopus', 'plate', 'toy']
box6 = ['blanket', 'shampoo', 'scarf']

# Move items from Box 5 to Box 4
box4.extend([box5.pop(box5.index('octopus'))])
box4.extend([box5.pop(box5.index('toy'))])
box4.extend([box5.pop(box5.index('plate'))])

# Put 'ocean' into Box 5
box5.append('ocean')

# Empty Box 5
box5 = []

# Replace items in Box 3 with 'ocean' and 'note'
box3 = ['ocean', 'note']

# Put 'belt' into Box 6
box6.append('belt')

# Empty Box 3
box3 = []

# Move items from Box 6 to Box 1
box1.extend([box6.pop(box6.index('belt'))])
box1.extend([box6.pop(box6.index('shampoo'))])

# Replace 'book' with 'bell' in Box 2
box2 = ['bell']

# Put 'razor' and 'shoe' into Box 4
box4.extend(['razor', 'shoe'])

# Remove 'shoe', 'plate', and 'toy' from Box 4
box4.remove('shoe')
box4.remove('plate')
box4.remove('toy')

# Move items from Box 6 to Box 4
box4.extend([box6.pop(box6.index('blanket'))])
box4.extend([box6.pop(box6.index('scarf'))])

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)
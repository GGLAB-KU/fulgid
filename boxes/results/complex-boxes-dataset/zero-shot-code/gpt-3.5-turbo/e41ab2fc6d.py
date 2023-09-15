box_0 = ['book', 'skirt', 'cow']
box_1 = []
box_2 = ['coin', 'horse']
box_3 = ['dress', 'helmet']
box_4 = ['frame', 'mixer', 'earring']

# Put the shelf and the cat into Box 1
box_1.extend(['shelf', 'cat'])

# Remove the coin and the horse from Box 2
box_2.remove('coin')
box_2.remove('horse')

# Replace the frame with the flower in Box 4
box_4.remove('frame')
box_4.append('flower')

# Swap the book in Box 0 with the cat in Box 1
box_0.remove('book')
box_1.remove('cat')
box_0.append('cat')
box_1.append('book')

# Replace the book and the shelf with the tree and the branch in Box 1
box_1.remove('book')
box_1.remove('shelf')
box_1.extend(['tree', 'branch'])

# Swap the earring in Box 4 with the cow in Box 0
box_4.remove('earring')
box_0.remove('cow')
box_4.append('cow')
box_0.append('earring')

# Replace the branch and the tree with the bear and the flute in Box 1
box_1.remove('branch')
box_1.remove('tree')
box_1.extend(['bear', 'flute'])

# Move the skirt from Box 0 to Box 2
box_0.remove('skirt')
box_2.append('skirt')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
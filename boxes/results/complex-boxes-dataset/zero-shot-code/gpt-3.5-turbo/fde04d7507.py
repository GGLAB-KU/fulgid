box_0 = ['zipper']
box_1 = ['shoes', 'doll', 'dog']
box_2 = []
box_3 = ['flute', 'plate', 'toaster']
box_4 = []
box_5 = ['violin', 'elephant', 'comb']

# Replace the zipper with the chair in Box 0
box_0 = ['chair']

# Put the charger and the toaster and the pan into Box 5
box_5.extend(['charger', 'toaster', 'pan'])

# Remove the shoes and the dog and the doll from Box 1
box_1 = []

# Empty Box 3
box_3 = []

# Put the piano into Box 3
box_3 = ['piano']

# Remove the piano from Box 3
box_3 = []

# Swap the chair in Box 0 with the charger in Box 5
box_0, box_5 = box_5, box_0

# Move the pan and the toaster and the comb from Box 5 to Box 2
box_2.extend([box_5.pop(box_5.index('pan')), box_5.pop(box_5.index('toaster')), box_5.pop(box_5.index('comb'))])

# Move the violin and the chair from Box 5 to Box 3
box_3.extend([box_5.pop(box_5.index('violin')), box_5.pop(box_5.index('chair'))])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
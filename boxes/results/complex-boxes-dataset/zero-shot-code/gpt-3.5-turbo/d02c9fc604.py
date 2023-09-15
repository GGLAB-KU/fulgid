box_0 = ['table', 'shirt', 'card']
box_1 = ['river', 'phone']
box_2 = ['pen', 'grass']
box_3 = []
box_4 = ['mountain', 'truck', 'whistle', 'charger', 'frame']
box_5 = ['mixer', 'tiger', 'freezer']
box_6 = ['submarine', 'violin', 'boat']
box_7 = ['spoon', 'tree', 'sculpture']
box_8 = ['ocean', 'star', 'scarf', 'fish']

# Remove the card and the shirt from Box 0
box_0.remove('card')
box_0.remove('shirt')

# Remove the mixer from Box 5
box_5.remove('mixer')

# Move the submarine and the boat and the violin from Box 6 to Box 8
box_8.extend(box_6)
box_6.clear()

# Replace the fish and the scarf with the freezer and the cup in Box 8
box_8.remove('fish')
box_8.remove('scarf')
box_8.extend(['freezer', 'cup'])

# Put the shorts and the river into Box 3
box_3.extend(['shorts', 'river'])

# Put the zipper and the fish and the seaweed into Box 2
box_2.extend(['zipper', 'fish', 'seaweed'])

# Put the sculpture into Box 6
box_6.append('sculpture')

# Move the sculpture and the tree and the spoon from Box 7 to Box 4
box_4.extend([box_7.pop(2), box_7.pop(1), box_7.pop(0)])

# Move the phone from Box 1 to Box 3
box_3.append(box_1.pop(1))

# Put the car into Box 2
box_2.append('car')

# Swap the river in Box 1 with the star in Box 8
box_1[0], box_8[1] = box_8[1], box_1[0]

# Move the star from Box 1 to Box 0
box_0.append(box_1.pop(0))

# Move the sculpture from Box 6 to Box 8
box_8.append(box_6.pop(0))

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
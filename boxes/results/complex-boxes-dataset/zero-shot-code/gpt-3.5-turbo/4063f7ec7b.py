box_0 = ['doll', 'clock', 'helmet', 'zipper']
box_1 = ['table']
box_2 = ['note']
box_3 = ['shelf', 'horse', 'fridge', 'ring']
box_4 = ['scarf', 'forest']
box_5 = ['dog', 'pillow']
box_6 = ['bell', 'soap', 'boat', 'apple']

# Put the elephant and the frame into Box 4
box_4.extend(['elephant', 'frame'])

# Move the helmet and the doll from Box 0 to Box 2
box_2.extend([box_0.pop(2), box_0.pop(0)])

# Replace the note and the doll and the helmet with the bracelet and the storm and the harmonica in Box 2
box_2 = ['bracelet', 'storm', 'harmonica']

# Replace the horse and the ring and the shelf with the charger and the thunder and the ship in Box 3
box_3 = ['charger', 'thunder', 'ship']

# Replace the table with the spoon in Box 1
box_1 = ['spoon']

# Empty Box 5
box_5 = []

# Replace the zipper with the key in Box 0
box_0[3] = 'key'

# Put the mirror and the glove and the button into Box 2
box_2.extend(['mirror', 'glove', 'button'])

# Remove the soap and the boat and the apple from Box 6
box_6 = []

# Swap the bell in Box 6 with the storm in Box 2
box_2[0], box_6[0] = box_6[0], box_2[0]

# Remove the ship from Box 3
box_3.remove('ship')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
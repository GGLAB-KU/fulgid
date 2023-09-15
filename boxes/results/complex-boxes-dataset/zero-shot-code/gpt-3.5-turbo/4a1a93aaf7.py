box_0 = []
box_1 = ['mixer', 'elephant', 'key', 'boat', 'frame']
box_2 = ['gloves']
box_3 = ['jungle', 'shampoo']
box_4 = ['submarine', 'makeup', 'drum']
box_5 = []

# Empty Box 2
box_2 = []

# Remove shampoo and jungle from Box 3
box_3.remove('shampoo')
box_3.remove('jungle')

# Replace submarine, makeup, and drum with flower, apple, and pillow in Box 4
box_4.remove('submarine')
box_4.remove('makeup')
box_4.remove('drum')
box_4.extend(['flower', 'apple', 'pillow'])

# Put the coat into Box 2
box_2.append('coat')

# Replace pillow and apple with headphone and plane in Box 4
box_4.remove('pillow')
box_4.remove('apple')
box_4.extend(['headphone', 'plane'])

# Swap the key in Box 1 with the coat in Box 2
box_1.remove('key')
box_2.remove('coat')
box_1.append('coat')
box_2.append('key')

# Remove headphone and plane from Box 4
box_4.remove('headphone')
box_4.remove('plane')

# Move the flower from Box 4 to Box 3
box_4.remove('flower')
box_3.append('flower')

# Swap the key in Box 2 with the mixer in Box 1
box_2.remove('key')
box_1.remove('mixer')
box_2.append('mixer')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
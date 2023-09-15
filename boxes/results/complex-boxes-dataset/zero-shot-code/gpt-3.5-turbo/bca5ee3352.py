box_0 = ['spoon', 'elephant', 'shorts', 'laptop', 'necklace']
box_1 = ['moon', 'tiger', 'shark', 'tie']
box_2 = ['gloves', 'apple', 'pillow', 'sculpture', 'plane']
box_3 = ['book', 'lion']
box_4 = ['submarine', 'headphone', 'toy', 'forest']

# Move the tiger from Box 1 to Box 2
box_2.append(box_1.pop(box_1.index('tiger')))

# Replace the submarine with the hat in Box 4
box_4[box_4.index('submarine')] = 'hat'

# Move the pillow and the gloves from Box 2 to Box 3
box_3.extend([box_2.pop(box_2.index('pillow')), box_2.pop(box_2.index('gloves'))])

# Remove the pillow and the lion from Box 3
box_3.remove('pillow')
box_3.remove('lion')

# Put the toy and the shampoo into Box 3
box_3.extend(['toy', 'shampoo'])

# Move the tie and the moon and the shark from Box 1 to Box 3
box_3.extend([box_1.pop(box_1.index('tie')), box_1.pop(box_1.index('moon')), box_1.pop(box_1.index('shark'))])

# Put the rock and the shoe into Box 0
box_0.extend(['rock', 'shoe'])

# Swap the tiger in Box 2 with the shoe in Box 0
box_2[box_2.index('tiger')], box_0[box_0.index('shoe')] = box_0[box_0.index('shoe')], box_2[box_2.index('tiger')]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
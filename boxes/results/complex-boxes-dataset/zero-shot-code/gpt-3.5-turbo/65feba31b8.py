box_0 = ['forest']
box_1 = ['apple', 'toothpaste', 'horse']
box_2 = ['shelf', 'ring', 'rain', 'boat', 'lion']
box_3 = ['blanket', 'game', 'train', 'tie', 'hat']
box_4 = ['bag', 'shampoo', 'elephant', 'flute', 'mask']

# Replace the rain and the boat and the ring with the fork and the wig and the perfume in Box 2
box_2.remove('rain')
box_2.remove('boat')
box_2.remove('ring')
box_2.extend(['fork', 'wig', 'perfume'])

# Swap the wig in Box 2 with the tie in Box 3
box_2.remove('wig')
box_3.remove('tie')
box_2.append('tie')
box_3.append('wig')

# Put the perfume into Box 2
box_2.append('perfume')

# Remove the forest from Box 0
box_0.remove('forest')

# Move the flute from Box 4 to Box 2
box_4.remove('flute')
box_2.append('flute')

# Remove the shampoo and the elephant and the mask from Box 4
box_4.remove('shampoo')
box_4.remove('elephant')
box_4.remove('mask')

# Swap the tie in Box 2 with the horse in Box 1
box_2.remove('tie')
box_1.remove('horse')
box_2.append('horse')
box_1.append('tie')

# Move the bag from Box 4 to Box 3
box_4.remove('bag')
box_3.append('bag')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
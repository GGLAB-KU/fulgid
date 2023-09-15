box_0 = ['toaster', 'glove', 'train']
box_1 = ['thunder', 'cow', 'keyboard', 'boat', 'bus']
box_2 = ['pan', 'jungle', 'cup', 'console', 'car']
box_3 = ['key', 'plane', 'necklace', 'swimsuit', 'cat']
box_4 = ['coat', 'scarf', 'perfume', 'moon', 'basket']
box_5 = []
box_6 = []

# Put the lion and the boat into Box 5
box_5.extend(['lion', 'boat'])

# Swap the glove in Box 0 with the coat in Box 4
box_0[1], box_4[0] = box_4[0], box_0[1]

# Replace the lion with the polish in Box 5
box_5[0] = 'polish'

# Move the necklace from Box 3 to Box 0
box_0.append(box_3.pop(2))

# Remove the necklace and the toaster from Box 0
box_0.remove('necklace')
box_0.remove('toaster')

# Move the boat from Box 5 to Box 1
box_1.append(box_5.pop(1))

# Swap the polish in Box 5 with the coat in Box 0
box_5[0], box_0[1] = box_0[1], box_5[0]

# Swap the coat in Box 5 with the cat in Box 3
box_5[0], box_3[4] = box_3[4], box_5[0]

# Replace the pan and the car and the console with the grinder and the microwave and the cup in Box 2
box_2[0], box_2[2], box_2[3] = 'grinder', 'microwave', 'cup'

# Move the perfume and the scarf and the glove from Box 4 to Box 5
box_5.extend([box_4.pop(2), box_4.pop(1), box_4.pop(0)])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
box_0 = ['pot', 'oven']
box_1 = ['bowl']
box_2 = ['forest', 'harmonica', 'soap']
box_3 = ['towel', 'sculpture', 'toothbrush', 'mirror']
box_4 = ['grinder', 'toaster', 'ring', 'frame']
box_5 = ['magnet']
box_6 = ['octopus', 'lipstick', 'planet']
box_7 = ['crown', 'lock', 'motorcycle', 'wallet']
box_8 = ['usb']
box_9 = ['keyboard', 'pen', 'shelf']
box_10 = ['jacket', 'island', 'whistle', 'comb']

# Remove the oven from Box 0
box_0.remove('oven')

# Swap the bowl in Box 1 with the toothbrush in Box 3
box_1[0], box_3[2] = box_3[2], box_1[0]

# Move the grinder from Box 4 to Box 1
box_1.append(box_4.pop(0))

# Replace the octopus with the lamp in Box 6
box_6[0] = 'lamp'

# Move the harmonica and the soap and the forest from Box 2 to Box 10
box_10.extend(box_2)
box_2.clear()

# Put the horse into Box 1
box_1.append('horse')

# Put the apple and the toothbrush into Box 8
box_8.extend(['apple', 'toothbrush'])

# Put the microwave and the wire into Box 10
box_10.extend(['microwave', 'wire'])

# Swap the planet in Box 6 with the apple in Box 8
box_6[2], box_8[1] = box_8[1], box_6[2]

# Replace the lamp and the apple with the ring and the game in Box 6
box_6[0] = 'ring'
box_6[1] = 'game'

# Move the magnet from Box 5 to Box 1
box_1.append(box_5.pop(0))

# Put the shoes and the horse and the shampoo into Box 6
box_6.extend(['shoes', 'horse', 'shampoo'])

# Put the ocean into Box 9
box_9.append('ocean')

# Swap the usb in Box 8 with the game in Box 6
box_8[0], box_6[1] = box_6[1], box_8[0]

# Move the crown and the motorcycle and the lock from Box 7 to Box 9
box_9.extend(box_7[:3])
box_7 = box_7[3:]

# Put the octopus and the perfume and the microwave into Box 4
box_4.extend(['octopus', 'perfume', 'microwave'])

# Remove the wallet from Box 7
box_7.remove('wallet')

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
print("Box 9:", box_9)
print("Box 10:", box_10)
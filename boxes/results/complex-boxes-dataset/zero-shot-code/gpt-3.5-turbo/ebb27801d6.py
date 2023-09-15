box_0 = []
box_1 = ['crown']
box_2 = ['lamp']
box_3 = ['grinder', 'toothpaste', 'bear']
box_4 = ['toaster', 'tape', 'blender', 'wallet']
box_5 = ['pot', 'jungle', 'island', 'flute']
box_6 = ['shorts', 'toy']
box_7 = ['controller', 'dog', 'river']
box_8 = ['comet']
box_9 = ['butterfly', 'plane', 'note', 'fork']
box_10 = ['key', 'shoe', 'bell']
box_11 = ['drum', 'shirt']
box_12 = ['brush', 'table', 'coral', 'storm']
box_13 = ['frame', 'zipper', 'makeup', 'spoon']

# Swap the lamp in Box 2 with the grinder in Box 3
box_2, box_3 = box_3, box_2

# Move the grinder from Box 2 to Box 1
box_1.append(box_2.pop(0))

# Put the keyboard and the dress into Box 11
box_11.extend(['keyboard', 'dress'])

# Move the toothpaste from Box 3 to Box 2
box_2.append(box_3.pop(1))

# Move the wallet and the toaster from Box 4 to Box 10
box_10.extend(box_4[3:])
box_4 = box_4[:3]

# Put the toothbrush and the snow into Box 4
box_4.extend(['toothbrush', 'snow'])

# Move the toothpaste from Box 2 to Box 7
box_7.append(box_2.pop(1))

# Move the blender from Box 4 to Box 13
box_13.append(box_4.pop(2))

# Move the island and the flute from Box 5 to Box 10
box_10.extend(box_5[2:])
box_5 = box_5[:2]

# Put the scarf and the grass into Box 13
box_13.extend(['scarf', 'grass'])

# Empty Box 7
box_7 = []

# Remove the snow from Box 4
box_4.remove('snow')

# Move the island and the wallet from Box 10 to Box 11
box_11.extend(box_10[2:4])
box_10 = box_10[:2]

# Put the blender and the blanket and the bracelet into Box 5
box_5.extend(['blender', 'blanket', 'bracelet'])

# Remove the brush and the coral from Box 12
box_12.remove('brush')
box_12.remove('coral')

# Replace the toy and the shorts with the apple and the laptop in Box 6
box_6 = ['apple', 'laptop']

# Move the blanket and the bracelet from Box 5 to Box 11
box_11.extend(box_5[3:])
box_5 = box_5[:3]

# Put the motorcycle and the tie into Box 2
box_2.extend(['motorcycle', 'tie'])

# Put the telescope and the dolphin and the seaweed into Box 13
box_13.extend(['telescope', 'dolphin', 'seaweed'])

# Swap the apple in Box 6 with the comet in Box 8
box_6[0], box_8[0] = box_8[0], box_6[0]

# Replace the fork and the butterfly and the plane with the planet and the charger and the sun in Box 9
box_9 = ['planet', 'charger', 'sun']

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
print("Box 11:", box_11)
print("Box 12:", box_12)
print("Box 13:", box_13)
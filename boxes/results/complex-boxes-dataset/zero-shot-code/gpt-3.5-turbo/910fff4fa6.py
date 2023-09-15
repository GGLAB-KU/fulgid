box_0 = []
box_1 = ['crown', 'keyboard']
box_2 = ['makeup', 'flute', 'cow', 'truck']
box_3 = ['sock', 'skirt', 'shoe', 'toaster']
box_4 = ['pan', 'necklace', 'wig', 'book']
box_5 = ['phone', 'scissors']
box_6 = ['chair']
box_7 = ['battery', 'meteor', 'mountain', 'usb', 'card']
box_8 = ['lion', 'toy']
box_9 = ['harmonica', 'mask', 'shelf', 'apple', 'belt']
box_10 = []
box_11 = ['pot', 'umbrella', 'scarf', 'clock', 'swimsuit']
box_12 = []

# Remove the crown from Box 1
box_1.remove('crown')

# Remove the swimsuit and the clock from Box 11
box_11.remove('swimsuit')
box_11.remove('clock')

# Replace the keyboard with the speaker in Box 1
box_1.remove('keyboard')
box_1.append('speaker')

# Put the toothbrush into Box 2
box_2.append('toothbrush')

# Empty Box 11
box_11.clear()

# Put the blender and the bicycle and the vase into Box 11
box_11.extend(['blender', 'bicycle', 'vase'])

# Move the speaker from Box 1 to Box 0
box_0.append(box_1.pop())

# Put the telescope into Box 10
box_10.append('telescope')

# Put the freezer and the bracelet into Box 3
box_3.extend(['freezer', 'bracelet'])

# Replace the flute and the toothbrush with the train and the moon in Box 2
box_2.remove('flute')
box_2.remove('toothbrush')
box_2.extend(['train', 'moon'])

# Put the octopus and the jacket and the dice into Box 8
box_8.extend(['octopus', 'jacket', 'dice'])

# Put the octopus into Box 11
box_11.append('octopus')

# Replace the toy and the jacket and the octopus with the key and the wig and the telescope in Box 8
box_8.remove('toy')
box_8.remove('jacket')
box_8.remove('octopus')
box_8.extend(['key', 'wig', 'telescope'])

# Remove the usb and the mountain from Box 7
box_7.remove('usb')
box_7.remove('mountain')

# Swap the battery in Box 7 with the toaster in Box 3
box_7.remove('battery')
box_3.remove('toaster')
box_7.append('toaster')
box_3.append('battery')

# Swap the telescope in Box 10 with the mask in Box 9
box_10.remove('telescope')
box_9.remove('mask')
box_10.append('mask')
box_9.append('telescope')

# Put the microwave into Box 3
box_3.append('microwave')

# Put the bicycle and the bell into Box 6
box_6.extend(['bicycle', 'bell'])

# Put the polish and the helmet and the lamp into Box 9
box_9.extend(['polish', 'helmet', 'lamp'])

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
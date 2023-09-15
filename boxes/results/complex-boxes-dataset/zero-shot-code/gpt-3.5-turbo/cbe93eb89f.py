box_0 = []
box_1 = ['snow', 'razor', 'shorts', 'jungle', 'crown']
box_2 = ['tree', 'fridge', 'makeup', 'branch']
box_3 = ['charger', 'drum', 'cow', 'toothpaste']
box_4 = ['sandals']
box_5 = []
box_6 = ['frame', 'shark', 'car', 'vase', 'shoe']
box_7 = []
box_8 = ['game', 'glasses']
box_9 = ['pot', 'mirror']
box_10 = ['lamp', 'motorcycle', 'perfume', 'rock']
box_11 = ['battery']
box_12 = []
box_13 = ['cup']

def print_box(box_index, box_items):
    print(f"Box {box_index}: {box_items}")

# Move the pot and the mirror from Box 9 to Box 7
box_7.extend([box_9.pop(box_9.index('pot')), box_9.pop(box_9.index('mirror'))])

# Put the jungle and the shelf and the bracelet into Box 6
box_6.extend(['jungle', 'shelf', 'bracelet'])

# Move the lamp from Box 10 to Box 2
box_2.append(box_10.pop(box_10.index('lamp')))

# Put the phone and the blanket into Box 1
box_1.extend(['phone', 'blanket'])

# Put the perfume into Box 13
box_13.append(box_10.pop(box_10.index('perfume')))

# Put the blender into Box 2
box_2.append('blender')

# Swap the makeup in Box 2 with the game in Box 8
box_2[box_2.index('makeup')], box_8[box_8.index('game')] = box_8[box_8.index('game')], box_2[box_2.index('makeup')]

# Replace the battery with the bear in Box 11
box_11[box_11.index('battery')] = 'bear'

# Put the bus into Box 8
box_8.append('bus')

# Empty Box 2
box_2.clear()

# Replace the bear with the usb in Box 11
box_11[box_11.index('bear')] = 'usb'

# Swap the charger in Box 3 with the usb in Box 11
box_3[box_3.index('charger')], box_11[box_11.index('usb')] = box_11[box_11.index('usb')], box_3[box_3.index('charger')]

# Empty Box 3
box_3.clear()

# Swap the bus in Box 8 with the vase in Box 6
box_8[box_8.index('bus')], box_6[box_6.index('vase')] = box_6[box_6.index('vase')], box_8[box_8.index('bus')]

# Remove the vase from Box 8
box_8.remove('vase')

# Put the chair and the razor and the bird into Box 0
box_0.extend(['chair', 'razor', 'bird'])

# Move the sandals from Box 4 to Box 8
box_8.append(box_4.pop(box_4.index('sandals')))

# Empty Box 0
box_0.clear()

# Put the star and the toaster into Box 0
box_0.extend(['star', 'toaster'])

# Put the octopus and the earring into Box 1
box_1.extend(['octopus', 'earring'])

# Replace the cup and the perfume with the flower and the console in Box 13
box_13[box_13.index('cup')] = 'flower'
box_13[box_13.index('perfume')] = 'console'

# Print the contents of each box
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)
print_box(9, box_9)
print_box(10, box_10)
print_box(11, box_11)
print_box(12, box_12)
print_box(13, box_13)
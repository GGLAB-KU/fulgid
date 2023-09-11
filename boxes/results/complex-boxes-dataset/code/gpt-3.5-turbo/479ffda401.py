# Initial state of boxes
boxes = {
    0: ['octopus', 'car'],
    1: ['pillow', 'toy', 'bear'],
    2: ['shampoo', 'toothpaste'],
    3: ['glasses', 'cloud', 'starfish', 'chair'],
    4: ['charger', 'ship', 'laptop', 'toaster'],
    5: ['usb'],
    6: ['grinder', 'button', 'harmonica', 'mirror'],
    7: ['microwave', 'shorts', 'glove', 'thunder', 'jacket'],
    8: ['island', 'coat'],
    9: ['grass', 'pants'],
    10: ['lion', 'seaweed', 'tape', 'bird']
}

# Remove the usb from Box 5.
boxes[5].remove('usb')

# Swap the harmonica in Box 6 with the seaweed in Box 10.
boxes[6].remove('harmonica')
boxes[10].remove('seaweed')
boxes[6].append('seaweed')
boxes[10].append('harmonica')

# Empty Box 10.
boxes[10] = []

# Empty Box 1.
boxes[1] = []

# Replace the island and the coat with the cat and the perfume in Box 8.
boxes[8].remove('island')
boxes[8].remove('coat')
boxes[8].append('cat')
boxes[8].append('perfume')

# Replace the glasses and the cloud and the chair with the vase and the shoes and the wig in Box 3.
boxes[3].remove('glasses')
boxes[3].remove('cloud')
boxes[3].remove('chair')
boxes[3].append('vase')
boxes[3].append('shoes')
boxes[3].append('wig')

# Swap the shoes in Box 3 with the toaster in Box 4.
boxes[3].remove('shoes')
boxes[4].remove('toaster')
boxes[3].append('toaster')
boxes[4].append('shoes')

# Swap the grinder in Box 6 with the octopus in Box 0.
boxes[6].remove('grinder')
boxes[0].remove('octopus')
boxes[6].append('octopus')
boxes[0].append('grinder')

# Swap the grass in Box 9 with the car in Box 0.
boxes[9].remove('grass')
boxes[0].remove('car')
boxes[9].append('car')
boxes[0].append('grass')

# Swap the mirror in Box 6 with the cat in Box 8.
boxes[6].remove('mirror')
boxes[8].remove('cat')
boxes[6].append('cat')
boxes[8].append('mirror')

# Remove the starfish and the wig from Box 3.
boxes[3].remove('starfish')
boxes[3].remove('wig')

# Swap the grinder in Box 0 with the vase in Box 3.
boxes[0].remove('grinder')
boxes[3].remove('vase')
boxes[0].append('vase')
boxes[3].append('grinder')

# Put the mirror and the dice and the earring into Box 2.
items_to_move = ['mirror', 'dice', 'earring']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Replace the jacket with the controller in Box 7.
boxes[7].remove('jacket')
boxes[7].append('controller')

# Put the pen and the glasses into Box 0.
items_to_move = ['pen', 'glasses']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[0].append(item)

# Move the mirror from Box 8 to Box 7.
boxes[8].remove('mirror')
boxes[7].append('mirror')

# Replace the perfume with the tie in Box 8.
boxes[8].remove('perfume')
boxes[8].append('tie')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
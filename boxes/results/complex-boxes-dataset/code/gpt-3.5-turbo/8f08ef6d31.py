# Initial state of boxes
boxes = {
    0: ['moon', 'vase', 'watch'],
    1: ['microscope', 'telescope'],
    2: ['keyboard', 'shirt', 'horn', 'mirror'],
    3: ['sandals', 'horse', 'bag', 'spoon', 'octopus'],
    4: ['freezer'],
    5: [],
    6: ['harmonica'],
    7: ['card', 'comet', 'apple', 'oven'],
    8: ['ocean', 'starfish', 'lion'],
    9: ['sock', 'pen', 'towel', 'mask'],
    10: [],
    11: ['train', 'shorts', 'candle', 'elephant'],
    12: ['usb']
}

# Remove the harmonica from Box 6.
boxes[6].remove('harmonica')

# Remove the moon and the vase and the watch from Box 0.
items_to_remove = ['moon', 'vase', 'watch']
for item in items_to_remove:
    boxes[0].remove(item)

# Swap the telescope in Box 1 with the freezer in Box 4.
boxes[1].remove('telescope')
boxes[4].remove('freezer')
boxes[1].append('freezer')
boxes[4].append('telescope')

# Move the elephant from Box 11 to Box 9.
boxes[11].remove('elephant')
boxes[9].append('elephant')

# Swap the microscope in Box 1 with the telescope in Box 4.
boxes[1].remove('microscope')
boxes[4].remove('telescope')
boxes[1].append('telescope')
boxes[4].append('microscope')

# Swap the sock in Box 9 with the ocean in Box 8.
boxes[9].remove('sock')
boxes[8].remove('ocean')
boxes[9].append('ocean')
boxes[8].append('sock')

# Move the mirror from Box 2 to Box 1.
boxes[2].remove('mirror')
boxes[1].append('mirror')

# Replace the elephant and the mask and the towel with the glove and the bag and the tie in Box 9.
boxes[9].remove('elephant')
boxes[9].remove('mask')
boxes[9].remove('towel')
boxes[9].append('glove')
boxes[9].append('bag')
boxes[9].append('tie')

# Swap the sandals in Box 3 with the keyboard in Box 2.
boxes[3].remove('sandals')
boxes[2].remove('keyboard')
boxes[3].append('keyboard')
boxes[2].append('sandals')

# Put the tiger and the grinder and the sandals into Box 0.
items_to_put = ['tiger', 'grinder', 'sandals']
for item in items_to_put:
    boxes[0].append(item)

# Replace the tie and the bag and the glove with the plane and the fish and the controller in Box 9.
boxes[9].remove('tie')
boxes[9].remove('bag')
boxes[9].remove('glove')
boxes[9].append('plane')
boxes[9].append('fish')
boxes[9].append('controller')

# Replace the train and the candle and the shorts with the blanket and the comb and the basket in Box 11.
boxes[11].remove('train')
boxes[11].remove('candle')
boxes[11].remove('shorts')
boxes[11].append('blanket')
boxes[11].append('comb')
boxes[11].append('basket')

# Remove the sandals from Box 0.
boxes[0].remove('sandals')

# Replace the oven and the apple and the card with the pillow and the wire and the bell in Box 7.
boxes[7].remove('oven')
boxes[7].remove('apple')
boxes[7].remove('card')
boxes[7].append('pillow')
boxes[7].append('wire')
boxes[7].append('bell')

# Remove the basket and the blanket and the comb from Box 11.
items_to_remove = ['basket', 'blanket', 'comb']
for item in items_to_remove:
    boxes[11].remove(item)

# Empty Box 3.
boxes[3] = []

# Swap the freezer in Box 1 with the controller in Box 9.
boxes[1].remove('freezer')
boxes[9].remove('controller')
boxes[1].append('controller')
boxes[9].append('freezer')

# Move the fish and the plane from Box 9 to Box 12.
boxes[9].remove('fish')
boxes[9].remove('plane')
boxes[12].append('fish')
boxes[12].append('plane')

# Remove the plane from Box 12.
boxes[12].remove('plane')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
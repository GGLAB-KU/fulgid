# Initial state of boxes
boxes = {
    0: [],
    1: ['magnet', 'comb', 'spoon', 'truck'],
    2: ['headphone', 'star'],
    3: ['charger', 'pen', 'usb', 'island', 'telescope'],
    4: ['river', 'ring'],
    5: [],
    6: ['rocket', 'meteor', 'motorcycle', 'razor', 'battery'],
    7: ['zipper', 'towel'],
    8: ['piano', 'horse', 'jungle'],
    9: ['perfume', 'bowl', 'pot'],
    10: ['cow', 'horn'],
    11: ['plate', 'wig'],
    12: ['planet', 'cup'],
    13: ['mixer', 'shirt', 'pan', 'flute'],
    14: ['shoe', 'basket', 'lock', 'console', 'train']
}

# Put the doll into Box 5.
boxes[5].append('doll')

# Remove the perfume and the pot and the bowl from Box 9.
items_to_remove = ['perfume', 'pot', 'bowl']
for item in items_to_remove:
    boxes[9].remove(item)

# Remove the piano and the horse from Box 8.
boxes[8].remove('piano')
boxes[8].remove('horse')

# Swap the pen in Box 3 with the cow in Box 10.
boxes[3].remove('pen')
boxes[10].remove('cow')
boxes[3].append('cow')
boxes[10].append('pen')

# Put the toothpaste and the coin and the pants into Box 11.
items_to_put = ['toothpaste', 'coin', 'pants']
for item in items_to_put:
    boxes[11].append(item)

# Swap the truck in Box 1 with the jungle in Box 8.
boxes[1].remove('truck')
boxes[8].remove('jungle')
boxes[1].append('jungle')
boxes[8].append('truck')

# Swap the razor in Box 6 with the doll in Box 5.
boxes[6].remove('razor')
boxes[5].remove('doll')
boxes[6].append('doll')
boxes[5].append('razor')

# Put the scissors and the shoes and the telescope into Box 8.
items_to_put = ['scissors', 'shoes', 'telescope']
for item in items_to_put:
    boxes[8].append(item)

# Swap the shirt in Box 13 with the zipper in Box 7.
boxes[13].remove('shirt')
boxes[7].remove('zipper')
boxes[13].append('zipper')
boxes[7].append('shirt')

# Move the river from Box 4 to Box 2.
boxes[4].remove('river')
boxes[2].append('river')

# Swap the coin in Box 11 with the horn in Box 10.
boxes[11].remove('coin')
boxes[10].remove('horn')
boxes[11].append('horn')
boxes[10].append('coin')

# Move the jungle from Box 1 to Box 8.
boxes[1].remove('jungle')
boxes[8].append('jungle')

# Empty Box 10.
boxes[10] = []

# Put the perfume and the helmet and the glasses into Box 10.
items_to_put = ['perfume', 'helmet', 'glasses']
for item in items_to_put:
    boxes[10].append(item)

# Put the battery and the controller and the necklace into Box 13.
items_to_put = ['battery', 'controller', 'necklace']
for item in items_to_put:
    boxes[13].append(item)

# Remove the toothpaste and the plate and the horn from Box 11.
items_to_remove = ['toothpaste', 'plate', 'horn']
for item in items_to_remove:
    boxes[11].remove(item)

# Put the boot and the rain and the comet into Box 5.
items_to_put = ['boot', 'rain', 'comet']
for item in items_to_put:
    boxes[5].append(item)

# Swap the meteor in Box 6 with the shoe in Box 14.
boxes[6].remove('meteor')
boxes[14].remove('shoe')
boxes[6].append('shoe')
boxes[14].append('meteor')

# Swap the pants in Box 11 with the shirt in Box 7.
boxes[11].remove('pants')
boxes[7].remove('shirt')
boxes[11].append('shirt')
boxes[7].append('pants')

# Move the glasses and the helmet and the perfume from Box 10 to Box 8.
items_to_move = ['glasses', 'helmet', 'perfume']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[8].append(item)

# Move the comet from Box 5 to Box 4.
boxes[5].remove('comet')
boxes[4].append('comet')

# Swap the cup in Box 12 with the rain in Box 5.
boxes[12].remove('cup')
boxes[5].remove('rain')
boxes[12].append('rain')
boxes[5].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
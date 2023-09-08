# Initial state of boxes
boxes = {
    0: ['submarine', 'fridge', 'elephant', 'bowl', 'note'],
    1: ['scissors', 'speaker', 'puzzle'],
    2: ['boot', 'car', 'phone', 'starfish', 'card'],
    3: ['comb'],
    4: ['wallet', 'cup'],
    5: ['sock', 'branch', 'watch', 'sun'],
    6: ['wig', 'tie', 'toy'],
    7: ['beach', 'butterfly', 'shampoo', 'mask', 'flower'],
    8: ['pot', 'razor', 'telescope'],
    9: ['headphone', 'comet', 'shoes', 'soap']
}

# Swap the tie in Box 6 with the wallet in Box 4.
boxes[6].remove('tie')
boxes[4].remove('wallet')
boxes[6].append('wallet')
boxes[4].append('tie')

# Swap the speaker in Box 1 with the tie in Box 4.
boxes[1].remove('speaker')
boxes[4].remove('tie')
boxes[1].append('tie')
boxes[4].append('speaker')

# Replace the tie and the scissors and the puzzle with the boat and the apple and the flute in Box 1.
boxes[1].remove('tie')
boxes[1].remove('scissors')
boxes[1].remove('puzzle')
boxes[1].append('boat')
boxes[1].append('apple')
boxes[1].append('flute')

# Swap the wallet in Box 6 with the cup in Box 4.
boxes[6].remove('wallet')
boxes[4].remove('cup')
boxes[6].append('cup')
boxes[4].append('wallet')

# Move the shoes and the soap and the headphone from Box 9 to Box 4.
items_to_move = ['shoes', 'soap', 'headphone']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[4].append(item)

# Remove the comet from Box 9.
boxes[9].remove('comet')

# Put the microscope and the forest and the pan into Box 3.
items_to_put = ['microscope', 'forest', 'pan']
for item in items_to_put:
    boxes[3].append(item)

# Remove the card and the starfish and the boot from Box 2.
items_to_remove = ['card', 'starfish', 'boot']
for item in items_to_remove:
    boxes[2].remove(item)

# Put the candle into Box 9.
boxes[9].append('candle')

# Replace the speaker with the fish in Box 4.
boxes[4].remove('speaker')
boxes[4].append('fish')

# Swap the pot in Box 8 with the microscope in Box 3.
boxes[8].remove('pot')
boxes[3].remove('microscope')
boxes[8].append('microscope')
boxes[3].append('pot')

# Remove the branch and the sock from Box 5.
items_to_remove = ['branch', 'sock']
for item in items_to_remove:
    boxes[5].remove(item)

# Replace the cup and the wig and the toy with the usb and the shampoo and the battery in Box 6.
boxes[6].remove('cup')
boxes[6].remove('wig')
boxes[6].remove('toy')
boxes[6].append('usb')
boxes[6].append('shampoo')
boxes[6].append('battery')

# Remove the comb from Box 3.
boxes[3].remove('comb')

# Move the razor and the telescope and the microscope from Box 8 to Box 1.
items_to_move = ['razor', 'telescope', 'microscope']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
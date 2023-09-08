# Initial state of boxes
boxes = {
    0: ['cup', 'leaf', 'phone'],
    1: ['train', 'shirt', 'piano'],
    2: ['comb'],
    3: [],
    4: [],
    5: ['shorts'],
    6: ['scissors', 'clock'],
    7: ['headphone', 'skirt', 'boat', 'flower', 'toothpaste'],
    8: ['razor', 'flute'],
    9: ['guitar', 'chair', 'basket'],
    10: ['controller', 'truck'],
    11: ['book']
}

# Replace the chair with the soap in Box 9.
boxes[9].remove('chair')
boxes[9].append('soap')

# Swap the headphone in Box 7 with the flute in Box 8.
boxes[7].remove('headphone')
boxes[8].remove('flute')
boxes[7].append('flute')
boxes[8].append('headphone')

# Swap the leaf in Box 0 with the scissors in Box 6.
boxes[0].remove('leaf')
boxes[6].remove('scissors')
boxes[0].append('scissors')
boxes[6].append('leaf')

# Replace the book with the bicycle in Box 11.
boxes[11].remove('book')
boxes[11].append('bicycle')

# Remove the razor from Box 8.
boxes[8].remove('razor')

# Remove the leaf and the clock from Box 6.
boxes[6].remove('leaf')
boxes[6].remove('clock')

# Replace the boat and the flute with the lock and the wallet in Box 7.
boxes[7].remove('boat')
boxes[7].remove('flute')
boxes[7].append('lock')
boxes[7].append('wallet')

# Put the speaker into Box 5.
boxes[5].append('speaker')

# Move the headphone from Box 8 to Box 1.
boxes[8].remove('headphone')
boxes[1].append('headphone')

# Remove the bicycle from Box 11.
boxes[11].remove('bicycle')

# Move the basket and the guitar and the soap from Box 9 to Box 3.
items_to_move = ['basket', 'guitar', 'soap']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[3].append(item)

# Replace the toothpaste and the lock with the scissors and the guitar in Box 7.
boxes[7].remove('toothpaste')
boxes[7].remove('lock')
boxes[7].append('scissors')
boxes[7].append('guitar')

# Move the basket from Box 3 to Box 7.
boxes[3].remove('basket')
boxes[7].append('basket')

# Swap the soap in Box 3 with the truck in Box 10.
boxes[3].remove('soap')
boxes[10].remove('truck')
boxes[3].append('truck')
boxes[10].append('soap')

# Replace the guitar and the truck with the grinder and the lightning in Box 3.
boxes[3].remove('guitar')
boxes[3].remove('truck')
boxes[3].append('grinder')
boxes[3].append('lightning')

# Put the horn and the shoe into Box 2.
boxes[2].append('horn')
boxes[2].append('shoe')

# Replace the grinder and the lightning with the note and the phone in Box 3.
boxes[3].remove('grinder')
boxes[3].remove('lightning')
boxes[3].append('note')
boxes[3].append('phone')

# Remove the speaker and the shorts from Box 5.
boxes[5].remove('speaker')
boxes[5].remove('shorts')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
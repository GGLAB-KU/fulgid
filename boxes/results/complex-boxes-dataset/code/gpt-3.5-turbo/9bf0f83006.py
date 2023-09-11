# Initial state of boxes
boxes = {
    0: ['spoon', 'jacket', 'jungle'],
    1: ['brush', 'starfish'],
    2: ['mountain', 'coral', 'helmet', 'paint'],
    3: ['car', 'doll', 'wallet', 'tie'],
    4: ['bird', 'cloud'],
    5: ['coat', 'skirt'],
    6: ['card'],
    7: ['apple', 'usb', 'tiger'],
    8: [],
    9: ['makeup', 'freezer', 'blanket', 'branch', 'umbrella'],
    10: ['boat', 'battery', 'swimsuit', 'vase', 'clock'],
    11: ['sandals', 'moon', 'keyboard', 'gloves'],
    12: ['dolphin']
}

# Put the necklace into Box 0.
boxes[0].append('necklace')

# Move the doll and the car and the wallet from Box 3 to Box 12.
items_to_move = ['doll', 'car', 'wallet']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[12].append(item)

# Move the card from Box 6 to Box 5.
boxes[6].remove('card')
boxes[5].append('card')

# Remove the tiger and the apple and the usb from Box 7.
items_to_remove = ['tiger', 'apple', 'usb']
for item in items_to_remove:
    boxes[7].remove(item)

# Move the brush and the starfish from Box 1 to Box 5.
items_to_move = ['brush', 'starfish']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Move the paint and the helmet from Box 2 to Box 3.
items_to_move = ['paint', 'helmet']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Remove the freezer and the blanket from Box 9.
items_to_remove = ['freezer', 'blanket']
for item in items_to_remove:
    boxes[9].remove(item)

# Replace the moon and the gloves and the keyboard with the flower and the bag and the bus in Box 11.
boxes[11].remove('moon')
boxes[11].remove('gloves')
boxes[11].remove('keyboard')
boxes[11].append('flower')
boxes[11].append('bag')
boxes[11].append('bus')

# Remove the doll and the wallet from Box 12.
boxes[12].remove('doll')
boxes[12].remove('wallet')

# Replace the dolphin and the car with the speaker and the cup in Box 12.
boxes[12].remove('dolphin')
boxes[12].remove('car')
boxes[12].append('speaker')
boxes[12].append('cup')

# Swap the bird in Box 4 with the tie in Box 3.
boxes[4].remove('bird')
boxes[3].remove('tie')
boxes[4].append('tie')
boxes[3].append('bird')

# Put the island into Box 10.
boxes[10].append('island')

# Put the mixer and the toothpaste into Box 11.
boxes[11].append('mixer')
boxes[11].append('toothpaste')

# Move the paint from Box 3 to Box 10.
boxes[3].remove('paint')
boxes[10].append('paint')

# Put the bird into Box 5.
boxes[5].append('bird')

# Replace the tie and the cloud with the paint and the mountain in Box 4.
boxes[4].remove('tie')
boxes[4].remove('cloud')
boxes[4].append('paint')
boxes[4].append('mountain')

# Put the tiger into Box 6.
boxes[6].append('tiger')

# Move the bird and the helmet from Box 3 to Box 5.
boxes[3].remove('bird')
boxes[3].remove('helmet')
boxes[5].append('bird')
boxes[5].append('helmet')

# Move the toothpaste and the mixer and the flower from Box 11 to Box 2.
items_to_move = ['toothpaste', 'mixer', 'flower']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[2].append(item)

# Put the cup into Box 7.
boxes[7].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
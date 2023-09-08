# Initial state of boxes
boxes = {
    0: ['soap', 'thunder', 'coin'],
    1: ['dice'],
    2: ['flute', 'necklace', 'plate', 'comb', 'fork'],
    3: ['bus', 'train', 'river'],
    4: ['mountain', 'umbrella', 'forest', 'doll', 'usb'],
    5: ['charger', 'seaweed', 'wire', 'coral'],
    6: ['keyboard', 'planet']
}

# Replace the keyboard with the dice in Box 6.
boxes[6].remove('keyboard')
boxes[6].append('dice')

# Swap the soap in Box 0 with the comb in Box 2.
boxes[0].remove('soap')
boxes[2].remove('comb')
boxes[0].append('comb')
boxes[2].append('soap')

# Move the mountain from Box 4 to Box 0.
boxes[4].remove('mountain')
boxes[0].append('mountain')

# Remove the dice from Box 1.
boxes[1].remove('dice')

# Replace the bus and the river and the train with the cat and the toothpaste and the wire in Box 3.
boxes[3].remove('bus')
boxes[3].remove('train')
boxes[3].remove('river')
boxes[3].append('cat')
boxes[3].append('toothpaste')
boxes[3].append('wire')

# Move the planet and the dice from Box 6 to Box 4.
boxes[6].remove('planet')
boxes[6].remove('dice')
boxes[4].append('planet')
boxes[4].append('dice')

# Swap the thunder in Box 0 with the necklace in Box 2.
boxes[0].remove('thunder')
boxes[2].remove('necklace')
boxes[0].append('necklace')
boxes[2].append('thunder')

# Move the coral and the wire and the charger from Box 5 to Box 0.
items_to_move = ['coral', 'wire', 'charger']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Swap the thunder in Box 2 with the coin in Box 0.
boxes[2].remove('thunder')
boxes[0].remove('coin')
boxes[2].append('coin')
boxes[0].append('thunder')

# Remove the plate from Box 2.
boxes[2].remove('plate')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: ['puzzle', 'bicycle'],
    1: ['violin', 'freezer', 'earring'],
    2: ['polish', 'vase', 'brush'],
    3: ['grinder', 'truck'],
    4: ['note', 'butterfly', 'laptop', 'plate', 'lightning'],
    5: ['starfish', 'apple', 'horn', 'wig'],
    6: ['speaker', 'thunder', 'card', 'ocean'],
    7: ['bowl'],
    8: ['glasses'],
    9: ['pan', 'telescope', 'dice', 'shoes'],
    10: ['magnet', 'blanket', 'table', 'candle', 'fridge'],
    11: ['fish', 'book', 'bracelet', 'microwave']
}

# Put the ship and the console and the rocket into Box 3.
boxes[3].extend(['ship', 'console', 'rocket'])

# Move the puzzle and the bicycle from Box 0 to Box 3.
items_to_move = ['puzzle', 'bicycle']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Remove the magnet from Box 10.
boxes[10].remove('magnet')

# Swap the polish in Box 2 with the ocean in Box 6.
boxes[2].remove('polish')
boxes[6].remove('ocean')
boxes[2].append('ocean')
boxes[6].append('polish')

# Empty Box 10.
boxes[10] = []

# Move the butterfly from Box 4 to Box 6.
boxes[4].remove('butterfly')
boxes[6].append('butterfly')

# Remove the freezer and the earring and the violin from Box 1.
items_to_remove = ['freezer', 'earring', 'violin']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the thunder in Box 6 with the note in Box 4.
boxes[6].remove('thunder')
boxes[4].remove('note')
boxes[6].append('note')
boxes[4].append('thunder')

# Replace the ship and the console with the keyboard and the necklace in Box 3.
boxes[3].remove('ship')
boxes[3].remove('console')
boxes[3].append('keyboard')
boxes[3].append('necklace')

# Replace the puzzle with the fridge in Box 3.
boxes[3].remove('puzzle')
boxes[3].append('fridge')

# Move the speaker and the note from Box 6 to Box 2.
items_to_move = ['speaker', 'note']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Replace the butterfly with the whistle in Box 6.
boxes[6].remove('butterfly')
boxes[6].append('whistle')

# Put the keyboard and the ring into Box 5.
boxes[5].extend(['keyboard', 'ring'])

# Put the plane and the bell into Box 2.
boxes[2].extend(['plane', 'bell'])

# Replace the bowl with the usb in Box 7.
boxes[7].remove('bowl')
boxes[7].append('usb')

# Put the wallet and the basket into Box 1.
boxes[1].extend(['wallet', 'basket'])

# Swap the laptop in Box 4 with the card in Box 6.
boxes[4].remove('laptop')
boxes[6].remove('card')
boxes[4].append('card')
boxes[6].append('laptop')

# Replace the fridge with the lamp in Box 3.
boxes[3].remove('fridge')
boxes[3].append('lamp')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
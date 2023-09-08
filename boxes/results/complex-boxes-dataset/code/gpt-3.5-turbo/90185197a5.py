# Initial state of boxes
boxes = {
    0: ['blanket', 'perfume', 'gloves'],
    1: ['sun', 'harmonica', 'toothbrush', 'glove', 'forest'],
    2: ['sculpture'],
    3: ['bracelet'],
    4: [],
    5: ['phone', 'submarine'],
    6: ['jacket', 'hat'],
    7: ['meteor', 'freezer', 'coral', 'book'],
    8: ['pen'],
    9: ['lock', 'umbrella'],
    10: ['pot'],
    11: ['microwave', 'plane', 'elephant', 'scarf', 'pants']
}

# Swap the jacket in Box 6 with the toothbrush in Box 1.
boxes[6], boxes[1][2] = [boxes[1][2]], boxes[6]

# Replace the harmonica and the glove with the bus and the charger in Box 1.
boxes[1].remove('harmonica')
boxes[1].remove('glove')
boxes[1].append('bus')
boxes[1].append('charger')

# Move the phone and the submarine from Box 5 to Box 0.
items_to_move = ['phone', 'submarine']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Replace the bracelet with the glove in Box 3.
boxes[3].remove('bracelet')
boxes[3].append('glove')

# Replace the lock with the fridge in Box 9.
boxes[9].remove('lock')
boxes[9].append('fridge')

# Replace the bus and the charger and the jacket with the dog and the hat and the bird in Box 1.
boxes[1].remove('bus')
boxes[1].remove('charger')
boxes[1].remove('jacket')
boxes[1].append('dog')
boxes[1].append('hat')
boxes[1].append('bird')

# Swap the fridge in Box 9 with the sculpture in Box 2.
boxes[9], boxes[2] = [boxes[2]], [boxes[9]]

# Move the glove from Box 3 to Box 11.
boxes[3].remove('glove')
boxes[11].append('glove')

# Empty Box 8.
boxes[8] = []

# Put the lightning into Box 6.
boxes[6].append('lightning')

# Replace the fridge with the ship in Box 2.
boxes[2].remove('fridge')
boxes[2].append('ship')

# Remove the sculpture from Box 9.
boxes[9].remove('sculpture')

# Put the cow and the helmet and the tiger into Box 8.
boxes[8].extend(['cow', 'helmet', 'tiger'])

# Put the earring and the glasses into Box 9.
boxes[9].extend(['earring', 'glasses'])

# Move the gloves and the phone and the perfume from Box 0 to Box 3.
items_to_move = ['gloves', 'phone', 'perfume']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[3].append(item)

# Replace the book and the freezer with the lightning and the game in Box 7.
boxes[7].remove('book')
boxes[7].remove('freezer')
boxes[7].append('lightning')
boxes[7].append('game')

# Move the coral and the lightning and the game from Box 7 to Box 5.
items_to_move = ['coral', 'lightning', 'game']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[5].append(item)

# Swap the dog in Box 1 with the cow in Box 8.
boxes[1], boxes[8] = [boxes[8]], [boxes[1]]

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
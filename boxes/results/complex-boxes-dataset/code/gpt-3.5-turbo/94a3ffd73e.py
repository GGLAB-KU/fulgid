# Initial state of boxes
boxes = {
    0: ['forest', 'tiger', 'shoe', 'towel', 'wallet'],
    1: ['bus', 'seaweed', 'rocket', 'speaker', 'river'],
    2: [],
    3: ['plane', 'horn', 'mountain', 'laptop', 'button'],
    4: ['bear', 'necklace'],
    5: ['shelf', 'game', 'starfish', 'glove'],
    6: [],
    7: ['note', 'motorcycle', 'boat', 'perfume'],
    8: ['coat', 'pot', 'bell', 'comb'],
    9: ['console'],
    10: ['coral', 'chair', 'jacket', 'sock'],
    11: ['belt', 'glasses'],
    12: ['jungle', 'ring', 'horse', 'polish', 'ocean']
}

# Replace the console with the cat in Box 9.
boxes[9].remove('console')
boxes[9].append('cat')

# Move the glasses from Box 11 to Box 0.
boxes[11].remove('glasses')
boxes[0].append('glasses')

# Remove the jungle and the ocean and the ring from Box 12.
boxes[12].remove('jungle')
boxes[12].remove('ocean')
boxes[12].remove('ring')

# Move the cat from Box 9 to Box 1.
boxes[9].remove('cat')
boxes[1].append('cat')

# Remove the glove from Box 5.
boxes[5].remove('glove')

# Empty Box 0.
boxes[0] = []

# Move the pot and the coat and the comb from Box 8 to Box 6.
items_to_move = ['pot', 'coat', 'comb']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[6].append(item)

# Replace the boat and the note and the perfume with the bowl and the candle and the bear in Box 7.
boxes[7].remove('boat')
boxes[7].remove('note')
boxes[7].remove('perfume')
boxes[7].append('bowl')
boxes[7].append('candle')
boxes[7].append('bear')

# Put the guitar and the toothpaste and the star into Box 4.
items_to_put = ['guitar', 'toothpaste', 'star']
for item in items_to_put:
    boxes[4].append(item)

# Put the hat and the crown and the flute into Box 3.
items_to_put = ['hat', 'crown', 'flute']
for item in items_to_put:
    boxes[3].append(item)

# Replace the polish and the horse with the planet and the glove in Box 12.
boxes[12].remove('polish')
boxes[12].remove('horse')
boxes[12].append('planet')
boxes[12].append('glove')

# Put the chair and the magnet and the bracelet into Box 4.
items_to_put = ['chair', 'magnet', 'bracelet']
for item in items_to_put:
    boxes[4].append(item)

# Put the sculpture into Box 9.
boxes[9].append('sculpture')

# Move the belt from Box 11 to Box 1.
boxes[11].remove('belt')
boxes[1].append('belt')

# Put the plate into Box 9.
boxes[9].append('plate')

# Replace the shelf with the speaker in Box 5.
boxes[5].remove('shelf')
boxes[5].append('speaker')

# Move the comb and the pot from Box 6 to Box 8.
items_to_move = ['comb', 'pot']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[8].append(item)

# Move the starfish and the game from Box 5 to Box 11.
items_to_move = ['starfish', 'game']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[11].append(item)

# Replace the magnet with the controller in Box 4.
boxes[4].remove('magnet')
boxes[4].append('controller')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
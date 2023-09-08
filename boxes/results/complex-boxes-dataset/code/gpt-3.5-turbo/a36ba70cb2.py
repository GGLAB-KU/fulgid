# Initial state of boxes
boxes = {
    0: [],
    1: ['console', 'oven', 'dice', 'perfume', 'note'],
    2: ['lightning', 'thunder', 'comet', 'towel'],
    3: [],
    4: ['bear', 'magnet', 'zipper', 'card', 'controller'],
    5: ['polish', 'gloves'],
    6: ['snow', 'scarf', 'boot', 'horse'],
    7: [],
    8: [],
    9: []
}

# Put the camera and the meteor into Box 6.
boxes[6].append('camera')
boxes[6].append('meteor')

# Swap the comet in Box 2 with the note in Box 1.
boxes[2].remove('comet')
boxes[1].remove('note')
boxes[2].append('note')
boxes[1].append('comet')

# Remove the camera and the horse from Box 6.
boxes[6].remove('camera')
boxes[6].remove('horse')

# Replace the snow and the scarf with the bear and the bicycle in Box 6.
boxes[6].remove('snow')
boxes[6].remove('scarf')
boxes[6].append('bear')
boxes[6].append('bicycle')

# Swap the bear in Box 4 with the oven in Box 1.
boxes[4].remove('bear')
boxes[1].remove('oven')
boxes[4].append('oven')
boxes[1].append('bear')

# Put the fridge into Box 0.
boxes[0].append('fridge')

# Swap the controller in Box 4 with the fridge in Box 0.
boxes[4].remove('controller')
boxes[0].remove('fridge')
boxes[4].append('fridge')
boxes[0].append('controller')

# Put the toothpaste and the tie and the pot into Box 5.
boxes[5].append('toothpaste')
boxes[5].append('tie')
boxes[5].append('pot')

# Move the towel and the note and the lightning from Box 2 to Box 9.
items_to_move = ['towel', 'note', 'lightning']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[9].append(item)

# Remove the toothpaste and the pot from Box 5.
boxes[5].remove('toothpaste')
boxes[5].remove('pot')

# Move the note and the lightning from Box 9 to Box 8.
items_to_move = ['note', 'lightning']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[8].append(item)

# Swap the gloves in Box 5 with the oven in Box 4.
boxes[5].remove('gloves')
boxes[4].remove('oven')
boxes[5].append('oven')
boxes[4].append('gloves')

# Put the flower into Box 2.
boxes[2].append('flower')

# Replace the bear with the horse in Box 1.
boxes[1].remove('bear')
boxes[1].append('horse')

# Replace the comet and the horse and the perfume with the helmet and the spoon and the flute in Box 1.
boxes[1].remove('comet')
boxes[1].remove('horse')
boxes[1].remove('perfume')
boxes[1].append('helmet')
boxes[1].append('spoon')
boxes[1].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
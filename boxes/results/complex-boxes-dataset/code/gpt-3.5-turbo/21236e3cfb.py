# Initial state of boxes
boxes = {
    0: ['camera', 'dress', 'plane'],
    1: ['zipper', 'perfume', 'lightning', 'dice'],
    2: ['chair', 'makeup', 'button'],
    3: ['earring'],
    4: ['fork', 'puzzle'],
    5: [],
    6: [],
    7: [],
    8: ['controller', 'planet', 'shirt'],
    9: ['candle'],
    10: ['starfish', 'toy', 'horse', 'bird'],
    11: ['bell', 'meteor']
}

# Move the meteor from Box 11 to Box 0.
boxes[11].remove('meteor')
boxes[0].append('meteor')

# Replace the controller with the mountain in Box 8.
boxes[8].remove('controller')
boxes[8].append('mountain')

# Replace the button and the chair with the violin and the mixer in Box 2.
boxes[2].remove('button')
boxes[2].remove('chair')
boxes[2].append('violin')
boxes[2].append('mixer')

# Replace the bell with the branch in Box 11.
boxes[11].remove('bell')
boxes[11].append('branch')

# Remove the mixer and the violin and the makeup from Box 2.
items_to_remove = ['mixer', 'violin', 'makeup']
for item in items_to_remove:
    boxes[2].remove(item)

# Replace the earring with the shark in Box 3.
boxes[3].remove('earring')
boxes[3].append('shark')

# Swap the plane in Box 0 with the dice in Box 1.
boxes[0].remove('plane')
boxes[1].remove('dice')
boxes[0].append('dice')
boxes[1].append('plane')

# Remove the candle from Box 9.
boxes[9].remove('candle')

# Swap the branch in Box 11 with the dress in Box 0.
boxes[11].remove('branch')
boxes[0].remove('dress')
boxes[11].append('dress')
boxes[0].append('branch')

# Move the zipper and the perfume and the lightning from Box 1 to Box 3.
items_to_move = ['zipper', 'perfume', 'lightning']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Move the plane from Box 1 to Box 7.
boxes[1].remove('plane')
boxes[7].append('plane')

# Put the belt and the horn into Box 5.
boxes[5].append('belt')
boxes[5].append('horn')

# Put the battery into Box 2.
boxes[2].append('battery')

# Put the drum into Box 10.
boxes[10].append('drum')

# Put the bus into Box 4.
boxes[4].append('bus')

# Remove the plane from Box 7.
boxes[7].remove('plane')

# Empty Box 2.
boxes[2] = []

# Put the toothpaste and the forest into Box 0.
boxes[0].append('toothpaste')
boxes[0].append('forest')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
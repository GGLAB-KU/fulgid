# Initial state of boxes
boxes = {
    0: ['shoes', 'shorts', 'dice', 'swimsuit'],
    1: ['microwave', 'branch', 'doll'],
    2: ['ring', 'polish', 'blender', 'crown', 'zipper'],
    3: ['speaker', 'snow'],
    4: [],
    5: ['needle'],
    6: ['toaster'],
    7: ['coat', 'wire', 'pillow', 'harmonica'],
    8: ['boat'],
    9: ['bicycle', 'pot', 'brush'],
    10: ['bowl', 'sun', 'razor'],
    11: ['toy', 'comet'],
    12: ['leaf', 'towel', 'soap'],
    13: ['elephant', 'watch', 'tiger'],
    14: ['violin']
}

# Empty Box 14.
boxes[14] = []

# Put the book into Box 3.
boxes[3].append('book')

# Put the ocean and the clock and the card into Box 9.
items_to_move = ['ocean', 'clock', 'card']
for item in items_to_move:
    boxes[9].append(item)

# Move the watch from Box 13 to Box 4.
boxes[13].remove('watch')
boxes[4].append('watch')

# Move the speaker from Box 3 to Box 1.
boxes[3].remove('speaker')
boxes[1].append('speaker')

# Move the ocean and the brush and the bicycle from Box 9 to Box 1.
items_to_move = ['ocean', 'brush', 'bicycle']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Move the razor from Box 10 to Box 6.
boxes[10].remove('razor')
boxes[6].append('razor')

# Put the blender and the perfume and the sun into Box 12.
items_to_move = ['blender', 'perfume', 'sun']
for item in items_to_move:
    boxes[12].append(item)

# Move the needle from Box 5 to Box 3.
boxes[5].remove('needle')
boxes[3].append('needle')

# Swap the boat in Box 8 with the blender in Box 12.
boxes[8], boxes[12] = boxes[12], boxes[8]

# Swap the sun in Box 10 with the comet in Box 11.
boxes[10], boxes[11] = boxes[11], boxes[10]

# Remove the swimsuit and the dice from Box 0.
items_to_remove = ['swimsuit', 'dice']
for item in items_to_remove:
    boxes[0].remove(item)

# Move the needle from Box 3 to Box 7.
boxes[3].remove('needle')
boxes[7].append('needle')

# Replace the razor and the toaster with the keyboard and the thunder in Box 6.
boxes[6].remove('razor')
boxes[6].remove('toaster')
boxes[6].append('keyboard')
boxes[6].append('thunder')

# Put the glasses into Box 2.
boxes[2].append('glasses')

# Remove the zipper from Box 2.
boxes[2].remove('zipper')

# Swap the tiger in Box 13 with the soap in Box 12.
boxes[13], boxes[12] = boxes[12], boxes[13]

# Replace the towel and the sun with the fork and the paint in Box 12.
boxes[12].remove('towel')
boxes[12].remove('sun')
boxes[12].append('fork')
boxes[12].append('paint')

# Put the puzzle into Box 8.
boxes[8].append('puzzle')

# Move the shorts and the shoes from Box 0 to Box 2.
items_to_move = ['shorts', 'shoes']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Put the pen into Box 10.
boxes[10].append('pen')

# Empty Box 2.
boxes[2] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
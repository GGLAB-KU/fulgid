# Initial state of boxes
boxes = {
    0: [],
    1: ['wire'],
    2: ['bird', 'shoes', 'basket', 'card'],
    3: [],
    4: ['note', 'button'],
    5: ['blender', 'whistle', 'ring'],
    6: ['spoon'],
    7: ['needle'],
    8: ['toy', 'fridge', 'book']
}

# Move the needle from Box 7 to Box 6.
boxes[7].remove('needle')
boxes[6].append('needle')

# Put the razor and the beach and the river into Box 6.
items_to_move = ['razor', 'beach', 'river']
for item in items_to_move:
    boxes[6].append(item)

# Replace the button with the bicycle in Box 4.
boxes[4].remove('button')
boxes[4].append('bicycle')

# Put the coral and the basket and the starfish into Box 1.
items_to_move = ['coral', 'basket', 'starfish']
for item in items_to_move:
    boxes[1].append(item)

# Remove the basket and the shoes and the card from Box 2.
items_to_remove = ['basket', 'shoes', 'card']
for item in items_to_remove:
    boxes[2].remove(item)

# Empty Box 2.
boxes[2] = []

# Replace the coral with the microwave in Box 1.
boxes[1].remove('coral')
boxes[1].append('microwave')

# Replace the wire and the basket and the microwave with the harmonica and the keyboard and the bell in Box 1.
items_to_remove = ['wire', 'basket', 'microwave']
items_to_add = ['harmonica', 'keyboard', 'bell']
for item in items_to_remove:
    boxes[1].remove(item)
for item in items_to_add:
    boxes[1].append(item)

# Move the river from Box 6 to Box 0.
boxes[6].remove('river')
boxes[0].append('river')

# Move the book from Box 8 to Box 4.
boxes[8].remove('book')
boxes[4].append('book')

# Swap the river in Box 0 with the beach in Box 6.
boxes[0].remove('river')
boxes[6].remove('beach')
boxes[0].append('beach')
boxes[6].append('river')

# Put the motorcycle into Box 5.
boxes[5].append('motorcycle')

# Replace the fridge and the toy with the console and the zipper in Box 8.
boxes[8].remove('fridge')
boxes[8].remove('toy')
boxes[8].append('console')
boxes[8].append('zipper')

# Remove the console from Box 8.
boxes[8].remove('console')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
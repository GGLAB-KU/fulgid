# Initial state of boxes
boxes = {
    0: ['doll', 'shark', 'wig', 'whistle', 'drum'],
    1: ['cat', 'plate', 'wire', 'controller', 'shampoo'],
    2: ['clock', 'cow', 'thunder', 'laptop', 'guitar'],
    3: [],
    4: ['vase', 'earring', 'apple', 'shorts', 'swimsuit'],
    5: [],
    6: ['piano', 'pants', 'planet'],
    7: ['polish', 'pillow'],
    8: [],
    9: [],
    10: ['lightning', 'helmet', 'grass', 'bicycle', 'pan'],
    11: ['bracelet', 'truck', 'towel', 'magnet', 'mask']
}

# Put the seaweed into Box 11.
boxes[11].append('seaweed')

# Move the pillow and the polish from Box 7 to Box 2.
items_to_move = ['pillow', 'polish']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[2].append(item)

# Replace the piano with the star in Box 6.
boxes[6].remove('piano')
boxes[6].append('star')

# Put the needle and the blanket and the shelf into Box 8.
items_to_move = ['needle', 'blanket', 'shelf']
for item in items_to_move:
    boxes[8].append(item)

# Replace the blanket and the needle and the shelf with the apple and the leaf and the bicycle in Box 8.
boxes[8].remove('blanket')
boxes[8].remove('needle')
boxes[8].remove('shelf')
boxes[8].append('apple')
boxes[8].append('leaf')
boxes[8].append('bicycle')

# Remove the laptop and the polish from Box 2.
boxes[2].remove('laptop')
boxes[2].remove('polish')

# Swap the star in Box 6 with the bicycle in Box 8.
boxes[6].remove('star')
boxes[8].remove('bicycle')
boxes[6].append('bicycle')
boxes[8].append('star')

# Remove the bicycle and the pants from Box 6.
boxes[6].remove('bicycle')
boxes[6].remove('pants')

# Replace the grass and the bicycle with the seaweed and the harmonica in Box 10.
boxes[10].remove('grass')
boxes[10].remove('bicycle')
boxes[10].append('seaweed')
boxes[10].append('harmonica')

# Replace the thunder and the pillow with the apple and the violin in Box 2.
boxes[2].remove('thunder')
boxes[2].remove('pillow')
boxes[2].append('apple')
boxes[2].append('violin')

# Put the octopus and the rocket and the doll into Box 9.
items_to_move = ['octopus', 'rocket', 'doll']
for item in items_to_move:
    boxes[9].append(item)

# Move the octopus and the doll from Box 9 to Box 3.
items_to_move = ['octopus', 'doll']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[3].append(item)

# Remove the apple and the star and the leaf from Box 8.
boxes[8].remove('apple')
boxes[8].remove('star')
boxes[8].remove('leaf')

# Remove the apple and the swimsuit and the shorts from Box 4.
boxes[4].remove('apple')
boxes[4].remove('swimsuit')
boxes[4].remove('shorts')

# Replace the vase and the earring with the charger and the note in Box 4.
boxes[4].remove('vase')
boxes[4].remove('earring')
boxes[4].append('charger')
boxes[4].append('note')

# Move the pan from Box 10 to Box 0.
boxes[10].remove('pan')
boxes[0].append('pan')

# Replace the pan with the leaf in Box 0.
boxes[0].remove('pan')
boxes[0].append('leaf')

# Replace the note with the scarf in Box 4.
boxes[4].remove('note')
boxes[4].append('scarf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
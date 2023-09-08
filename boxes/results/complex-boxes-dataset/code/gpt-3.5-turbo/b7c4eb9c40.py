# Initial state of boxes
boxes = {
    0: ['train', 'butterfly', 'pants', 'spoon', 'lipstick'],
    1: ['tie'],
    2: ['blender', 'necklace', 'glove'],
    3: ['keyboard', 'cat', 'boat', 'moon'],
    4: ['speaker', 'towel', 'magnet'],
    5: ['cloud', 'plate', 'coral', 'frame', 'bird'],
    6: ['cow', 'wire', 'shoe', 'shoes', 'microwave'],
    7: ['harmonica'],
    8: ['river', 'grinder', 'helmet', 'apple'],
    9: ['watch', 'forest'],
    10: ['gloves', 'toy', 'perfume']
}

# Put the apple and the key and the ship into Box 0.
boxes[0].append('apple')
boxes[0].append('key')
boxes[0].append('ship')

# Swap the harmonica in Box 7 with the pants in Box 0.
boxes[7], boxes[0] = boxes[0], boxes[7]

# Put the speaker and the plate into Box 8.
boxes[8].append('speaker')
boxes[8].append('plate')

# Move the ship from Box 0 to Box 3.
boxes[0].remove('ship')
boxes[3].append('ship')

# Swap the toy in Box 10 with the speaker in Box 8.
boxes[10], boxes[8] = boxes[8], boxes[10]

# Put the sandals and the starfish into Box 8.
boxes[8].append('sandals')
boxes[8].append('starfish')

# Move the pants from Box 7 to Box 6.
boxes[7].remove('pants')
boxes[6].append('pants')

# Replace the blender and the necklace and the glove with the card and the planet and the controller in Box 2.
boxes[2].remove('blender')
boxes[2].remove('necklace')
boxes[2].remove('glove')
boxes[2].append('card')
boxes[2].append('planet')
boxes[2].append('controller')

# Move the helmet and the sandals and the river from Box 8 to Box 9.
items_to_move = ['helmet', 'sandals', 'river']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[9].append(item)

# Put the pen and the dog into Box 10.
boxes[10].append('pen')
boxes[10].append('dog')

# Put the shirt and the glasses into Box 2.
boxes[2].append('shirt')
boxes[2].append('glasses')

# Swap the magnet in Box 4 with the speaker in Box 10.
boxes[4], boxes[10] = boxes[10], boxes[4]

# Empty Box 4.
boxes[4] = []

# Put the lion and the bird into Box 9.
boxes[9].append('lion')
boxes[9].append('bird')

# Replace the coral and the plate with the basket and the tape in Box 5.
boxes[5].remove('coral')
boxes[5].remove('plate')
boxes[5].append('basket')
boxes[5].append('tape')

# Put the shelf and the doll and the pants into Box 9.
boxes[9].append('shelf')
boxes[9].append('doll')
boxes[9].append('pants')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
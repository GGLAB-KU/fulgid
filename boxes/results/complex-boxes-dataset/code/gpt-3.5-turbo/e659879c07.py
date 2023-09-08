# Initial state of boxes
boxes = {
    0: [],
    1: ['elephant', 'flute', 'boat'],
    2: ['umbrella', 'lock', 'book'],
    3: ['shoes', 'flower', 'train', 'grinder', 'desert'],
    4: ['dog', 'headphone'],
    5: [],
    6: ['violin'],
    7: ['swimsuit', 'crown', 'sandals'],
    8: ['branch'],
    9: ['tape', 'laptop', 'camera']
}

# Swap the branch in Box 8 with the dog in Box 4.
boxes[8], boxes[4] = boxes[4], boxes[8]

# Remove the violin from Box 6.
boxes[6].remove('violin')

# Put the wallet and the coat into Box 8.
boxes[8].append('wallet')
boxes[8].append('coat')

# Put the shoe and the seaweed into Box 0.
boxes[0].append('shoe')
boxes[0].append('seaweed')

# Remove the tape from Box 9.
boxes[9].remove('tape')

# Remove the crown and the swimsuit from Box 7.
boxes[7].remove('crown')
boxes[7].remove('swimsuit')

# Replace the desert and the shoes with the camera and the blender in Box 3.
boxes[3].remove('desert')
boxes[3].remove('shoes')
boxes[3].append('camera')
boxes[3].append('blender')

# Remove the wallet and the coat and the dog from Box 8.
boxes[8].remove('wallet')
boxes[8].remove('coat')
boxes[8].remove('dog')

# Move the boat and the elephant and the flute from Box 1 to Box 2.
items_to_move = ['boat', 'elephant', 'flute']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Swap the seaweed in Box 0 with the camera in Box 9.
boxes[0], boxes[9] = boxes[9], boxes[0]

# Replace the camera and the blender with the necklace and the sun in Box 3.
boxes[3].remove('camera')
boxes[3].remove('blender')
boxes[3].append('necklace')
boxes[3].append('sun')

# Put the blender into Box 4.
boxes[4].append('blender')

# Swap the headphone in Box 4 with the flute in Box 2.
boxes[4], boxes[2] = boxes[2], boxes[4]

# Remove the sandals from Box 7.
boxes[7].remove('sandals')

# Move the blender and the flute and the branch from Box 4 to Box 7.
items_to_move = ['blender', 'flute', 'branch']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[7].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
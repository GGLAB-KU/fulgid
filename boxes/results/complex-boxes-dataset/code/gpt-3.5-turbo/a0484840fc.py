# Initial state of boxes
boxes = {
    0: ['bell'],
    1: [],
    2: ['leaf'],
    3: ['flower', 'lock', 'controller'],
    4: ['shelf', 'cloud', 'toothpaste', 'dress'],
    5: ['perfume', 'pan', 'scarf', 'brush'],
    6: ['butterfly', 'glove', 'crown'],
    7: ['shoe', 'book', 'storm'],
    8: ['ship', 'frame'],
    9: ['grass', 'comb'],
    10: ['swimsuit', 'bus', 'puzzle', 'mountain'],
    11: ['rocket', 'dog', 'doll', 'blender'],
    12: ['belt', 'fridge', 'whistle', 'spoon', 'hat'],
    13: ['starfish', 'sandals', 'octopus', 'shirt'],
    14: ['note', 'lion', 'makeup', 'oven']
}

# Remove the frame and the ship from Box 8.
boxes[8].remove('frame')
boxes[8].remove('ship')

# Replace the glove with the starfish in Box 6.
boxes[6].remove('glove')
boxes[6].append('starfish')

# Swap the whistle in Box 12 with the shelf in Box 4.
boxes[12].remove('whistle')
boxes[4].remove('shelf')
boxes[12].append('shelf')
boxes[4].append('whistle')

# Put the violin and the crown into Box 1.
boxes[1].append('violin')
boxes[1].append('crown')

# Put the storm and the sculpture into Box 6.
boxes[6].append('storm')
boxes[6].append('sculpture')

# Move the note and the lion and the makeup from Box 14 to Box 7.
items_to_move = ['note', 'lion', 'makeup']
for item in items_to_move:
    boxes[14].remove(item)
    boxes[7].append(item)

# Swap the bell in Box 0 with the pan in Box 5.
boxes[0].remove('bell')
boxes[5].remove('pan')
boxes[0].append('pan')
boxes[5].append('bell')

# Put the controller and the candle and the plate into Box 13.
boxes[13].append('controller')
boxes[13].append('candle')
boxes[13].append('plate')

# Remove the lock from Box 3.
boxes[3].remove('lock')

# Replace the swimsuit with the truck in Box 10.
boxes[10].remove('swimsuit')
boxes[10].append('truck')

# Remove the scarf and the brush and the bell from Box 5.
items_to_remove = ['scarf', 'brush', 'bell']
for item in items_to_remove:
    boxes[5].remove(item)

# Swap the dog in Box 11 with the makeup in Box 7.
boxes[11].remove('dog')
boxes[7].remove('makeup')
boxes[11].append('makeup')
boxes[7].append('dog')

# Empty Box 11.
boxes[11] = []

# Put the scissors into Box 13.
boxes[13].append('scissors')

# Remove the oven from Box 14.
boxes[14].remove('oven')

# Swap the cloud in Box 4 with the butterfly in Box 6.
boxes[4].remove('cloud')
boxes[6].remove('butterfly')
boxes[4].append('butterfly')
boxes[6].append('cloud')

# Remove the controller and the flower from Box 3.
boxes[3].remove('controller')
boxes[3].remove('flower')

# Move the comb from Box 9 to Box 4.
boxes[9].remove('comb')
boxes[4].append('comb')

# Swap the mountain in Box 10 with the scissors in Box 13.
boxes[10].remove('mountain')
boxes[13].remove('scissors')
boxes[10].append('scissors')
boxes[13].append('mountain')

# Swap the lion in Box 7 with the grass in Box 9.
boxes[7].remove('lion')
boxes[9].remove('grass')
boxes[7].append('grass')
boxes[9].append('lion')

# Put the mirror and the key and the horn into Box 5.
boxes[5].append('mirror')
boxes[5].append('key')
boxes[5].append('horn')

# Replace the storm and the dog and the grass with the wig and the mixer and the branch in Box 7.
boxes[7].remove('storm')
boxes[7].remove('dog')
boxes[7].remove('grass')
boxes[7].append('wig')
boxes[7].append('mixer')
boxes[7].append('branch')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
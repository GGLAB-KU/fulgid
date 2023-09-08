# Initial state of boxes
boxes = {
    0: ['meteor', 'cup', 'cow', 'razor'],
    1: ['piano', 'desert', 'coral', 'helmet', 'submarine'],
    2: ['pants', 'flower', 'bell'],
    3: ['lamp'],
    4: ['dog'],
    5: [],
    6: [],
    7: [],
    8: [],
    9: ['shoe', 'boot', 'magnet', 'jacket'],
    10: ['thunder', 'key', 'fridge', 'toothpaste', 'octopus'],
    11: ['toothbrush', 'plate', 'apple', 'storm'],
    12: ['bird'],
    13: ['coat']
}

# Put the gloves into Box 2.
boxes[2].append('gloves')

# Remove the apple and the plate and the storm from Box 11.
items_to_remove = ['apple', 'plate', 'storm']
for item in items_to_remove:
    boxes[11].remove(item)

# Put the piano and the frame and the grass into Box 3.
items_to_move = ['piano', 'frame', 'grass']
for item in items_to_move:
    boxes[3].append(item)

# Empty Box 12.
boxes[12] = []

# Swap the lamp in Box 3 with the magnet in Box 9.
boxes[3].remove('lamp')
boxes[9].remove('magnet')
boxes[3].append('magnet')
boxes[9].append('lamp')

# Move the dog from Box 4 to Box 10.
boxes[4].remove('dog')
boxes[10].append('dog')

# Swap the jacket in Box 9 with the grass in Box 3.
boxes[9].remove('jacket')
boxes[3].remove('grass')
boxes[9].append('grass')
boxes[3].append('jacket')

# Remove the cow from Box 0.
boxes[0].remove('cow')

# Move the octopus from Box 10 to Box 3.
boxes[10].remove('octopus')
boxes[3].append('octopus')

# Swap the coat in Box 13 with the flower in Box 2.
boxes[13].remove('coat')
boxes[2].remove('flower')
boxes[13].append('flower')
boxes[2].append('coat')

# Put the makeup into Box 7.
boxes[7].append('makeup')

# Move the jacket and the frame and the piano from Box 3 to Box 7.
items_to_move = ['jacket', 'frame', 'piano']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[7].append(item)

# Remove the fridge and the toothpaste from Box 10.
items_to_remove = ['fridge', 'toothpaste']
for item in items_to_remove:
    boxes[10].remove(item)

# Put the puzzle and the train into Box 8.
boxes[8].append('puzzle')
boxes[8].append('train')

# Remove the cup and the meteor from Box 0.
items_to_remove = ['cup', 'meteor']
for item in items_to_remove:
    boxes[0].remove(item)

# Replace the boot and the grass and the lamp with the coral and the blender and the truck in Box 9.
boxes[9].remove('boot')
boxes[9].remove('grass')
boxes[9].remove('lamp')
boxes[9].append('coral')
boxes[9].append('blender')
boxes[9].append('truck')

# Replace the piano and the makeup with the scissors and the plate in Box 7.
boxes[7].remove('piano')
boxes[7].remove('makeup')
boxes[7].append('scissors')
boxes[7].append('plate')

# Swap the jacket in Box 7 with the key in Box 10.
boxes[7].remove('jacket')
boxes[10].remove('key')
boxes[7].append('key')
boxes[10].append('jacket')

# Remove the coral and the blender from Box 9.
boxes[9].remove('coral')
boxes[9].remove('blender')

# Replace the puzzle with the sculpture in Box 8.
boxes[8].remove('puzzle')
boxes[8].append('sculpture')

# Replace the key and the plate and the frame with the gloves and the soap and the dress in Box 7.
boxes[7].remove('key')
boxes[7].remove('plate')
boxes[7].remove('frame')
boxes[7].append('gloves')
boxes[7].append('soap')
boxes[7].append('dress')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
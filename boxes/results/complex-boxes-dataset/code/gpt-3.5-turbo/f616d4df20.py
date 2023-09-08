# Initial state of boxes
boxes = {
    0: ['camera', 'pen', 'crown'],
    1: ['brush', 'shark'],
    2: [],
    3: ['blanket', 'vase', 'island', 'paint', 'sculpture'],
    4: ['puzzle', 'lipstick', 'key', 'charger'],
    5: ['toothbrush', 'blender', 'drum', 'coral', 'keyboard'],
    6: ['tape', 'magnet', 'bracelet'],
    7: ['shoe', 'tree', 'star'],
    8: ['octopus'],
    9: ['submarine'],
    10: [],
    11: ['lion', 'wire', 'umbrella'],
    12: ['shorts', 'bear', 'necklace', 'leaf'],
    13: []
}

# Swap the bear in Box 12 with the umbrella in Box 11.
boxes[12].remove('bear')
boxes[11].remove('umbrella')
boxes[12].append('umbrella')
boxes[11].append('bear')

# Replace the star and the shoe and the tree with the spoon and the scarf and the fork in Box 7.
boxes[7].remove('star')
boxes[7].remove('shoe')
boxes[7].remove('tree')
boxes[7].append('spoon')
boxes[7].append('scarf')
boxes[7].append('fork')

# Put the needle into Box 7.
boxes[7].append('needle')

# Move the brush and the shark from Box 1 to Box 12.
boxes[1].remove('brush')
boxes[1].remove('shark')
boxes[12].append('brush')
boxes[12].append('shark')

# Move the blender and the coral from Box 5 to Box 10.
boxes[5].remove('blender')
boxes[5].remove('coral')
boxes[10].append('blender')
boxes[10].append('coral')

# Put the crown into Box 12.
boxes[0].remove('crown')
boxes[12].append('crown')

# Move the keyboard from Box 5 to Box 6.
boxes[5].remove('keyboard')
boxes[6].append('keyboard')

# Remove the needle from Box 7.
boxes[7].remove('needle')

# Put the toothbrush into Box 4.
boxes[4].append('toothbrush')

# Replace the coral with the glasses in Box 10.
boxes[10].remove('coral')
boxes[10].append('glasses')

# Remove the crown and the pen and the camera from Box 0.
boxes[0].remove('crown')
boxes[0].remove('pen')
boxes[0].remove('camera')

# Swap the keyboard in Box 6 with the charger in Box 4.
boxes[6].remove('keyboard')
boxes[4].remove('charger')
boxes[6].append('charger')
boxes[4].append('keyboard')

# Move the wire and the lion from Box 11 to Box 10.
boxes[11].remove('wire')
boxes[11].remove('lion')
boxes[10].append('wire')
boxes[10].append('lion')

# Move the sculpture from Box 3 to Box 8.
boxes[3].remove('sculpture')
boxes[8].append('sculpture')

# Replace the wire and the glasses and the lion with the cloud and the vase and the fish in Box 10.
boxes[10].remove('wire')
boxes[10].remove('glasses')
boxes[10].remove('lion')
boxes[10].append('cloud')
boxes[10].append('vase')
boxes[10].append('fish')

# Remove the fork and the spoon and the scarf from Box 7.
boxes[7].remove('fork')
boxes[7].remove('spoon')
boxes[7].remove('scarf')

# Put the bird and the grass and the pot into Box 11.
boxes[11].append('bird')
boxes[11].append('grass')
boxes[11].append('pot')

# Replace the octopus with the snow in Box 8.
boxes[8].remove('octopus')
boxes[8].append('snow')

# Replace the submarine with the apple in Box 9.
boxes[9].remove('submarine')
boxes[9].append('apple')

# Put the scarf and the frame into Box 9.
boxes[9].append('scarf')
boxes[9].append('frame')

# Remove the keyboard from Box 4.
boxes[4].remove('keyboard')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
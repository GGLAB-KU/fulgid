# Initial state of boxes
boxes = {
    0: ['plane', 'camera', 'bear'],
    1: [],
    2: [],
    3: ['candle', 'island'],
    4: ['coral', 'submarine'],
    5: [],
    6: ['planet'],
    7: ['grass', 'cat'],
    8: ['dress'],
    9: ['drum', 'toothpaste', 'table'],
    10: ['fork'],
    11: ['sculpture', 'flute'],
    12: ['doll', 'wig', 'motorcycle', 'octopus', 'fish'],
    13: ['hat', 'violin', 'mixer'],
    14: []
}

# Empty Box 13.
boxes[13] = []

# Replace the fish and the octopus and the motorcycle with the speaker and the bracelet and the rock in Box 12.
boxes[12].remove('fish')
boxes[12].remove('octopus')
boxes[12].remove('motorcycle')
boxes[12].append('speaker')
boxes[12].append('bracelet')
boxes[12].append('rock')

# Replace the speaker and the doll and the bracelet with the mask and the plate and the dog in Box 12.
boxes[12].remove('speaker')
boxes[12].remove('doll')
boxes[12].remove('bracelet')
boxes[12].append('mask')
boxes[12].append('plate')
boxes[12].append('dog')

# Move the plane and the bear from Box 0 to Box 10.
boxes[0].remove('plane')
boxes[0].remove('bear')
boxes[10].append('plane')
boxes[10].append('bear')

# Remove the bear and the plane and the fork from Box 10.
boxes[10].remove('bear')
boxes[10].remove('plane')
boxes[10].remove('fork')

# Replace the mask with the lightning in Box 12.
boxes[12].remove('mask')
boxes[12].append('lightning')

# Remove the planet from Box 6.
boxes[6].remove('planet')

# Remove the camera from Box 0.
boxes[0].remove('camera')

# Replace the drum and the table and the toothpaste with the spoon and the dog and the thunder in Box 9.
boxes[9].remove('drum')
boxes[9].remove('table')
boxes[9].remove('toothpaste')
boxes[9].append('spoon')
boxes[9].append('dog')
boxes[9].append('thunder')

# Swap the sculpture in Box 11 with the island in Box 3.
boxes[11].remove('sculpture')
boxes[3].remove('island')
boxes[11].append('island')
boxes[3].append('sculpture')

# Put the fish into Box 1.
boxes[1].append('fish')

# Swap the dog in Box 9 with the submarine in Box 4.
boxes[9].remove('dog')
boxes[4].remove('submarine')
boxes[9].append('submarine')
boxes[4].append('dog')

# Swap the island in Box 11 with the coral in Box 4.
boxes[11].remove('island')
boxes[4].remove('coral')
boxes[11].append('coral')
boxes[4].append('island')

# Put the skirt and the elephant and the wallet into Box 5.
boxes[5].append('skirt')
boxes[5].append('elephant')
boxes[5].append('wallet')

# Remove the lightning from Box 12.
boxes[12].remove('lightning')

# Swap the skirt in Box 5 with the submarine in Box 9.
boxes[5].remove('skirt')
boxes[9].remove('submarine')
boxes[5].append('submarine')
boxes[9].append('skirt')

# Replace the wallet and the elephant and the submarine with the rain and the frame and the puzzle in Box 5.
boxes[5].remove('wallet')
boxes[5].remove('elephant')
boxes[5].remove('submarine')
boxes[5].append('rain')
boxes[5].append('frame')
boxes[5].append('puzzle')

# Swap the rain in Box 5 with the dress in Box 8.
boxes[5].remove('rain')
boxes[8].remove('dress')
boxes[5].append('dress')
boxes[8].append('rain')

# Remove the fish from Box 1.
boxes[1].remove('fish')

# Replace the wig with the cup in Box 12.
boxes[12].remove('wig')
boxes[12].append('cup')

# Replace the skirt and the spoon with the grinder and the violin in Box 9.
boxes[9].remove('skirt')
boxes[9].remove('spoon')
boxes[9].append('grinder')
boxes[9].append('violin')

# Swap the rain in Box 8 with the grass in Box 7.
boxes[8].remove('rain')
boxes[7].remove('grass')
boxes[8].append('grass')
boxes[7].append('rain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: ['freezer'],
    1: ['guitar', 'bell', 'pot'],
    2: [],
    3: ['whistle', 'starfish'],
    4: ['rock', 'earring', 'lipstick', 'shorts', 'apple'],
    5: ['grass', 'elephant'],
    6: ['scissors', 'gloves'],
    7: ['snow'],
    8: ['speaker', 'rain', 'cloud', 'wallet'],
    9: [],
    10: ['cat', 'camera', 'doll', 'puzzle'],
    11: ['butterfly', 'oven', 'harmonica', 'coin', 'brush'],
    12: ['charger', 'sculpture', 'mixer', 'watch'],
    13: []
}

# Replace the camera with the wire in Box 10.
boxes[10].remove('camera')
boxes[10].append('wire')

# Replace the snow with the bowl in Box 7.
boxes[7].remove('snow')
boxes[7].append('bowl')

# Put the meteor and the soap into Box 4.
boxes[4].append('meteor')
boxes[4].append('soap')

# Swap the freezer in Box 0 with the gloves in Box 6.
boxes[0].remove('freezer')
boxes[6].remove('gloves')
boxes[0].append('gloves')
boxes[6].append('freezer')

# Move the elephant and the grass from Box 5 to Box 0.
items_to_move = ['elephant', 'grass']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[0].append(item)

# Move the earring from Box 4 to Box 11.
boxes[4].remove('earring')
boxes[11].append('earring')

# Replace the scissors with the needle in Box 6.
boxes[6].remove('scissors')
boxes[6].append('needle')

# Move the elephant from Box 0 to Box 3.
boxes[0].remove('elephant')
boxes[3].append('elephant')

# Move the apple from Box 4 to Box 0.
boxes[4].remove('apple')
boxes[0].append('apple')

# Swap the needle in Box 6 with the rock in Box 4.
boxes[6].remove('needle')
boxes[4].remove('rock')
boxes[6].append('rock')
boxes[4].append('needle')

# Swap the gloves in Box 0 with the sculpture in Box 12.
boxes[0].remove('gloves')
boxes[12].remove('sculpture')
boxes[0].append('sculpture')
boxes[12].append('gloves')

# Empty Box 8.
boxes[8] = []

# Move the pot and the guitar and the bell from Box 1 to Box 13.
items_to_move = ['pot', 'guitar', 'bell']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[13].append(item)

# Empty Box 11.
boxes[11] = []

# Swap the bell in Box 13 with the freezer in Box 6.
boxes[13].remove('bell')
boxes[6].remove('freezer')
boxes[13].append('freezer')
boxes[6].append('bell')

# Move the soap from Box 4 to Box 10.
boxes[4].remove('soap')
boxes[10].append('soap')

# Move the apple from Box 0 to Box 3.
boxes[0].remove('apple')
boxes[3].append('apple')

# Remove the mixer from Box 12.
boxes[12].remove('mixer')

# Swap the sculpture in Box 0 with the lipstick in Box 4.
boxes[0].remove('sculpture')
boxes[4].remove('lipstick')
boxes[0].append('lipstick')
boxes[4].append('sculpture')

# Swap the lipstick in Box 0 with the watch in Box 12.
boxes[0].remove('lipstick')
boxes[12].remove('watch')
boxes[0].append('watch')
boxes[12].append('lipstick')

# Swap the bowl in Box 7 with the shorts in Box 4.
boxes[7].remove('bowl')
boxes[4].remove('shorts')
boxes[7].append('shorts')
boxes[4].append('bowl')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
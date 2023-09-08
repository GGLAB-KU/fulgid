# Initial state of boxes
boxes = {
    0: [],
    1: ['chair', 'elephant', 'seaweed'],
    2: ['swimsuit', 'plate'],
    3: [],
    4: ['island', 'tiger', 'grass', 'lamp', 'whistle']
}

# Replace the tiger and the whistle with the bowl and the bus in Box 4.
boxes[4].remove('tiger')
boxes[4].remove('whistle')
boxes[4].append('bowl')
boxes[4].append('bus')

# Remove the chair from Box 1.
boxes[1].remove('chair')

# Replace the swimsuit and the plate with the dolphin and the beach in Box 2.
boxes[2].remove('swimsuit')
boxes[2].remove('plate')
boxes[2].append('dolphin')
boxes[2].append('beach')

# Replace the seaweed with the pan in Box 1.
boxes[1].remove('seaweed')
boxes[1].append('pan')

# Swap the elephant in Box 1 with the bus in Box 4.
boxes[1].remove('elephant')
boxes[4].remove('bus')
boxes[1].append('bus')
boxes[4].append('elephant')

# Replace the grass and the island and the lamp with the bracelet and the comb and the guitar in Box 4.
boxes[4].remove('grass')
boxes[4].remove('island')
boxes[4].remove('lamp')
boxes[4].append('bracelet')
boxes[4].append('comb')
boxes[4].append('guitar')

# Swap the bracelet in Box 4 with the bus in Box 1.
boxes[4].remove('bracelet')
boxes[1].remove('bus')
boxes[4].append('bus')
boxes[1].append('bracelet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
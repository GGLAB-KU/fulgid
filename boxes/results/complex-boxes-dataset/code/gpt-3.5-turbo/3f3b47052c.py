# Initial state of boxes
boxes = {
    0: ['pot', 'shorts', 'key', 'bell', 'toothpaste'],
    1: ['sandals', 'violin', 'spoon', 'apple'],
    2: ['cat'],
    3: ['clock', 'puzzle', 'ring', 'laptop', 'comb'],
    4: [],
    5: ['paint'],
    6: ['camera']
}

# Remove the cat from Box 2.
boxes[2].remove('cat')

# Swap the bell in Box 0 with the clock in Box 3.
boxes[0].remove('bell')
boxes[3].remove('clock')
boxes[0].append('clock')
boxes[3].append('bell')

# Put the sculpture and the grinder and the bicycle into Box 0.
boxes[0].extend(['sculpture', 'grinder', 'bicycle'])

# Replace the bicycle and the grinder and the key with the lion and the ship and the dolphin in Box 0.
boxes[0].remove('bicycle')
boxes[0].remove('grinder')
boxes[0].remove('key')
boxes[0].append('lion')
boxes[0].append('ship')
boxes[0].append('dolphin')

# Swap the spoon in Box 1 with the clock in Box 0.
boxes[1].remove('spoon')
boxes[0].remove('clock')
boxes[1].append('clock')
boxes[0].append('spoon')

# Replace the paint with the storm in Box 5.
boxes[5].remove('paint')
boxes[5].append('storm')

# Replace the camera with the shelf in Box 6.
boxes[6].remove('camera')
boxes[6].append('shelf')

# Swap the shelf in Box 6 with the apple in Box 1.
boxes[6].remove('shelf')
boxes[1].remove('apple')
boxes[6].append('apple')
boxes[1].append('shelf')

# Move the violin from Box 1 to Box 3.
boxes[1].remove('violin')
boxes[3].append('violin')

# Put the motorcycle and the sculpture and the planet into Box 1.
boxes[1].extend(['motorcycle', 'sculpture', 'planet'])

# Replace the motorcycle with the shoe in Box 1.
boxes[1].remove('motorcycle')
boxes[1].append('shoe')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
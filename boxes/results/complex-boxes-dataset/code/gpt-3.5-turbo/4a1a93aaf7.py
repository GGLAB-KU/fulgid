# Initial state of boxes
boxes = {
    0: [],
    1: ['mixer', 'elephant', 'key', 'boat', 'frame'],
    2: ['gloves'],
    3: ['jungle', 'shampoo'],
    4: ['submarine', 'makeup', 'drum'],
    5: []
}

# Empty Box 2
boxes[2] = []

# Remove the shampoo and the jungle from Box 3
boxes[3].remove('shampoo')
boxes[3].remove('jungle')

# Replace the submarine and the makeup and the drum with the flower and the apple and the pillow in Box 4
boxes[4].remove('submarine')
boxes[4].remove('makeup')
boxes[4].remove('drum')
boxes[4].append('flower')
boxes[4].append('apple')
boxes[4].append('pillow')

# Put the coat into Box 2
boxes[2].append('coat')

# Replace the pillow and the apple with the headphone and the plane in Box 4
boxes[4].remove('pillow')
boxes[4].remove('apple')
boxes[4].append('headphone')
boxes[4].append('plane')

# Swap the key in Box 1 with the coat in Box 2
boxes[1].remove('key')
boxes[2].remove('coat')
boxes[1].append('coat')
boxes[2].append('key')

# Remove the headphone and the plane from Box 4
boxes[4].remove('headphone')
boxes[4].remove('plane')

# Move the flower from Box 4 to Box 3
boxes[4].remove('flower')
boxes[3].append('flower')

# Swap the key in Box 2 with the mixer in Box 1
boxes[2].remove('key')
boxes[1].remove('mixer')
boxes[2].append('mixer')
boxes[1].append('key')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
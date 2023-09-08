# Initial state of boxes
boxes = {
    0: ['pot', 'pan', 'microscope', 'car', 'bird'],
    1: ['note', 'starfish', 'camera', 'chair'],
    2: ['necklace', 'swimsuit', 'doll', 'wallet', 'polish'],
    3: [],
    4: ['motorcycle', 'razor'],
    5: ['bowl'],
    6: ['bus'],
    7: ['wire']
}

# Replace the pot and the bird with the glove and the blender in Box 0.
boxes[0].remove('pot')
boxes[0].remove('bird')
boxes[0].append('glove')
boxes[0].append('blender')

# Swap the razor in Box 4 with the bus in Box 6.
boxes[4].remove('razor')
boxes[6].remove('bus')
boxes[4].append('bus')
boxes[6].append('razor')

# Replace the motorcycle and the bus with the tiger and the plane in Box 4.
boxes[4].remove('motorcycle')
boxes[4].remove('bus')
boxes[4].append('tiger')
boxes[4].append('plane')

# Put the chair and the meteor and the speaker into Box 4.
items_to_put = ['chair', 'meteor', 'speaker']
for item in items_to_put:
    boxes[4].append(item)

# Put the glove into Box 0.
boxes[0].append('glove')

# Put the lion and the horse into Box 3.
boxes[3].append('lion')
boxes[3].append('horse')

# Remove the meteor and the plane from Box 4.
boxes[4].remove('meteor')
boxes[4].remove('plane')

# Replace the bowl with the makeup in Box 5.
boxes[5].remove('bowl')
boxes[5].append('makeup')

# Swap the lion in Box 3 with the polish in Box 2.
boxes[3].remove('lion')
boxes[2].remove('polish')
boxes[3].append('polish')
boxes[2].append('lion')

# Swap the horse in Box 3 with the razor in Box 6.
boxes[3].remove('horse')
boxes[6].remove('razor')
boxes[3].append('razor')
boxes[6].append('horse')

# Swap the horse in Box 6 with the starfish in Box 1.
boxes[6].remove('horse')
boxes[1].remove('starfish')
boxes[6].append('starfish')
boxes[1].append('horse')

# Swap the makeup in Box 5 with the wire in Box 7.
boxes[5].remove('makeup')
boxes[7].remove('wire')
boxes[5].append('wire')
boxes[7].append('makeup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
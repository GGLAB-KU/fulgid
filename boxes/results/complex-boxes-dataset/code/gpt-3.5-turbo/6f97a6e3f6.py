# Initial state of boxes
boxes = {
    0: ['drum', 'note', 'blender', 'mixer', 'sun'],
    1: ['train', 'plate'],
    2: ['thunder'],
    3: ['toy', 'bowl', 'phone', 'butterfly', 'charger'],
    4: []
}

# Remove the blender from Box 0.
boxes[0].remove('blender')

# Replace the toy and the charger with the doll and the bird in Box 3.
boxes[3].remove('toy')
boxes[3].remove('charger')
boxes[3].append('doll')
boxes[3].append('bird')

# Remove the bowl and the doll from Box 3.
boxes[3].remove('bowl')
boxes[3].remove('doll')

# Put the pillow and the flower into Box 1.
boxes[1].append('pillow')
boxes[1].append('flower')

# Replace the thunder with the shelf in Box 2.
boxes[2].remove('thunder')
boxes[2].append('shelf')

# Replace the butterfly with the skirt in Box 3.
boxes[3].remove('butterfly')
boxes[3].append('skirt')

# Put the shark into Box 0.
boxes[0].append('shark')

# Replace the plate and the pillow with the cup and the towel in Box 1.
boxes[1].remove('plate')
boxes[1].remove('pillow')
boxes[1].append('cup')
boxes[1].append('towel')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
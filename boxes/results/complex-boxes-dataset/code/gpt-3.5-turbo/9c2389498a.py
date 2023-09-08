# Initial state of boxes
boxes = {
    0: ['laptop', 'desert', 'lion'],
    1: ['cow', 'fork', 'tape', 'bracelet'],
    2: [],
    3: ['zipper', 'microwave', 'wire'],
    4: ['makeup', 'thunder', 'grinder'],
    5: [],
    6: ['piano', 'headphone'],
    7: ['pot', 'river', 'fish', 'doll', 'phone'],
    8: ['glasses', 'shoes', 'grass']
}

# Put the charger and the blender and the grinder into Box 0.
boxes[0].extend(['charger', 'blender', 'grinder'])

# Swap the fish in Box 7 with the lion in Box 0.
boxes[0].remove('lion')
boxes[7].remove('fish')
boxes[0].append('fish')
boxes[7].append('lion')

# Swap the blender in Box 0 with the grass in Box 8.
boxes[0].remove('blender')
boxes[8].remove('grass')
boxes[0].append('grass')
boxes[8].append('blender')

# Move the grinder and the thunder from Box 4 to Box 7.
boxes[4].remove('grinder')
boxes[4].remove('thunder')
boxes[7].extend(['grinder', 'thunder'])

# Put the rocket and the train into Box 3.
boxes[3].extend(['rocket', 'train'])

# Swap the rocket in Box 3 with the headphone in Box 6.
boxes[3].remove('rocket')
boxes[6].remove('headphone')
boxes[3].append('headphone')
boxes[6].append('rocket')

# Replace the desert and the fish and the grinder with the octopus and the submarine and the note in Box 0.
boxes[0].remove('desert')
boxes[0].remove('fish')
boxes[0].remove('grinder')
boxes[0].extend(['octopus', 'submarine', 'note'])

# Put the scissors into Box 4.
boxes[4].append('scissors')

# Remove the thunder from Box 7.
boxes[7].remove('thunder')

# Put the polish and the blanket and the plane into Box 4.
boxes[4].extend(['polish', 'blanket', 'plane'])

# Put the bowl and the forest into Box 0.
boxes[0].extend(['bowl', 'forest'])

# Remove the grinder from Box 7.
boxes[7].remove('grinder')

# Remove the lion and the phone from Box 7.
boxes[7].remove('lion')
boxes[7].remove('phone')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
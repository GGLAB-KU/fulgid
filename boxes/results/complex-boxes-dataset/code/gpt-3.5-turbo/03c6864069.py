# Initial state of boxes
boxes = {
    0: ['umbrella', 'cup', 'grinder'],
    1: ['toy', 'camera', 'toothpaste'],
    2: ['puzzle', 'paint', 'lion', 'microwave'],
    3: ['guitar', 'sun', 'brush'],
    4: [],
    5: ['frame', 'doll', 'earring', 'necklace'],
    6: ['lock', 'table', 'bus', 'rocket'],
    7: ['blender', 'makeup'],
    8: ['console', 'lightning', 'tape', 'wig', 'sandals']
}

# Swap the camera in Box 1 with the bus in Box 6.
boxes[1].remove('camera')
boxes[6].remove('bus')
boxes[1].append('bus')
boxes[6].append('camera')

# Remove the brush and the sun and the guitar from Box 3.
items_to_remove = ['brush', 'sun', 'guitar']
for item in items_to_remove:
    boxes[3].remove(item)

# Remove the lock and the rocket and the table from Box 6.
items_to_remove = ['lock', 'rocket', 'table']
for item in items_to_remove:
    boxes[6].remove(item)

# Replace the paint and the puzzle with the belt and the needle in Box 2.
boxes[2].remove('paint')
boxes[2].remove('puzzle')
boxes[2].append('belt')
boxes[2].append('needle')

# Replace the grinder with the bus in Box 0.
boxes[0].remove('grinder')
boxes[6].remove('bus')
boxes[0].append('bus')
boxes[6].append('grinder')

# Swap the necklace in Box 5 with the toy in Box 1.
boxes[5].remove('necklace')
boxes[1].remove('toy')
boxes[5].append('toy')
boxes[1].append('necklace')

# Put the elephant and the bird into Box 0.
boxes[0].append('elephant')
boxes[0].append('bird')

# Replace the necklace and the toothpaste and the bus with the ship and the console and the plane in Box 1.
boxes[1].remove('necklace')
boxes[1].remove('toothpaste')
boxes[6].remove('bus')
boxes[1].append('ship')
boxes[1].append('console')
boxes[6].append('plane')

# Replace the camera with the bell in Box 6.
boxes[6].remove('camera')
boxes[6].append('bell')

# Remove the wig from Box 8.
boxes[8].remove('wig')

# Put the doll into Box 3.
boxes[5].remove('doll')
boxes[3].append('doll')

# Replace the bird with the lamp in Box 0.
boxes[0].remove('bird')
boxes[0].append('lamp')

# Replace the cup with the button in Box 0.
boxes[0].remove('cup')
boxes[0].append('button')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
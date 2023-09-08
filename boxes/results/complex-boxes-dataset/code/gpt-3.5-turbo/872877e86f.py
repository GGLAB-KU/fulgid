# Initial state of boxes
boxes = {
    0: ['jacket', 'plane'],
    1: ['sock', 'gloves', 'branch', 'fish'],
    2: ['blender', 'truck', 'dog', 'mask'],
    3: ['glasses'],
    4: ['puzzle', 'river'],
    5: [],
    6: ['swimsuit', 'pot', 'helmet', 'speaker', 'pen']
}

# Move the speaker and the swimsuit from Box 6 to Box 4.
boxes[6].remove('speaker')
boxes[6].remove('swimsuit')
boxes[4].append('speaker')
boxes[4].append('swimsuit')

# Replace the jacket with the necklace in Box 0.
boxes[0].remove('jacket')
boxes[0].append('necklace')

# Put the hat and the tree into Box 0.
boxes[0].append('hat')
boxes[0].append('tree')

# Remove the necklace from Box 0.
boxes[0].remove('necklace')

# Move the sock and the branch from Box 1 to Box 3.
boxes[1].remove('sock')
boxes[1].remove('branch')
boxes[3].append('sock')
boxes[3].append('branch')

# Swap the swimsuit in Box 4 with the branch in Box 3.
boxes[4].remove('swimsuit')
boxes[3].remove('branch')
boxes[4].append('branch')
boxes[3].append('swimsuit')

# Replace the tree and the plane and the hat with the helmet and the crown and the violin in Box 0.
boxes[0].remove('tree')
boxes[0].remove('plane')
boxes[0].remove('hat')
boxes[0].append('helmet')
boxes[0].append('crown')
boxes[0].append('violin')

# Swap the blender in Box 2 with the glasses in Box 3.
boxes[2].remove('blender')
boxes[3].remove('glasses')
boxes[2].append('glasses')
boxes[3].append('blender')

# Move the glasses from Box 2 to Box 3.
boxes[2].remove('glasses')
boxes[3].append('glasses')

# Put the star into Box 6.
boxes[6].append('star')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
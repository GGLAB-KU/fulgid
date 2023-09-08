# Initial state of boxes
boxes = {
    0: [],
    1: ['bear', 'violin', 'frame', 'chair'],
    2: [],
    3: [],
    4: ['desert'],
    5: ['submarine', 'river', 'fish', 'button'],
    6: ['wire', 'pot', 'pan', 'bus', 'sculpture'],
    7: ['belt', 'helmet'],
    8: ['mask', 'mountain'],
    9: ['wallet'],
    10: ['clock'],
    11: ['bird', 'swimsuit'],
    12: ['piano'],
    13: ['lipstick', 'car', 'gloves', 'wig', 'microwave']
}

# Replace the violin with the plate in Box 1.
boxes[1].remove('violin')
boxes[1].append('plate')

# Move the river from Box 5 to Box 11.
boxes[5].remove('river')
boxes[11].append('river')

# Swap the desert in Box 4 with the piano in Box 12.
boxes[4], boxes[12] = boxes[12], boxes[4]

# Move the desert from Box 12 to Box 13.
boxes[12].remove('desert')
boxes[13].append('desert')

# Put the polish into Box 6.
boxes[6].append('polish')

# Put the crown and the fish into Box 4.
boxes[4].append('crown')
boxes[4].append('fish')

# Replace the bear and the plate with the pan and the coral in Box 1.
boxes[1].remove('bear')
boxes[1].remove('plate')
boxes[1].append('pan')
boxes[1].append('coral')

# Remove the clock from Box 10.
boxes[10].remove('clock')

# Remove the bird from Box 11.
boxes[11].remove('bird')

# Replace the button and the fish and the submarine with the helmet and the grinder and the camera in Box 5.
boxes[5].remove('button')
boxes[5].remove('fish')
boxes[5].remove('submarine')
boxes[5].append('helmet')
boxes[5].append('grinder')
boxes[5].append('camera')

# Move the helmet from Box 5 to Box 1.
boxes[5].remove('helmet')
boxes[1].append('helmet')

# Put the cup into Box 2.
boxes[2].append('cup')

# Move the belt from Box 7 to Box 9.
boxes[7].remove('belt')
boxes[9].append('belt')

# Empty Box 9.
boxes[9] = []

# Replace the mask and the mountain with the grinder and the coral in Box 8.
boxes[8].remove('mask')
boxes[8].remove('mountain')
boxes[8].append('grinder')
boxes[8].append('coral')

# Move the swimsuit from Box 11 to Box 3.
boxes[11].remove('swimsuit')
boxes[3].append('swimsuit')

# Replace the grinder with the bell in Box 8.
boxes[8].remove('grinder')
boxes[8].append('bell')

# Replace the swimsuit with the shark in Box 3.
boxes[3].remove('swimsuit')
boxes[3].append('shark')

# Swap the bell in Box 8 with the pan in Box 1.
boxes[8], boxes[1] = boxes[1], boxes[8]

# Replace the cup with the rock in Box 2.
boxes[2].remove('cup')
boxes[2].append('rock')

# Put the grass and the microwave into Box 4.
boxes[4].append('grass')
boxes[4].append('microwave')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
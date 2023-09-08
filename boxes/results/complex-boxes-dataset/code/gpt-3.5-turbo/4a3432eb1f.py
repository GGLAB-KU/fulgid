# Initial state of boxes
boxes = {
    0: ['bus', 'ring', 'pot', 'candle'],
    1: ['shark', 'thunder', 'skirt', 'bag', 'meteor'],
    2: ['microscope', 'bird', 'oven', 'horse'],
    3: ['lipstick', 'necklace'],
    4: ['fish', 'telescope', 'button', 'boot', 'ship'],
    5: [],
    6: ['lamp'],
    7: ['blender', 'wire', 'freezer', 'tree'],
    8: ['cup', 'basket', 'table', 'rock'],
    9: ['tiger', 'camera', 'toothpaste'],
    10: ['grinder'],
    11: ['shoe', 'sock', 'needle', 'butterfly', 'cat'],
    12: ['shelf'],
    13: ['sandals', 'glasses', 'game', 'glove', 'truck'],
    14: ['soap', 'gloves', 'octopus']
}

# Put the gloves into Box 3.
boxes[13].remove('gloves')
boxes[3].append('gloves')

# Replace the tree and the blender with the plane and the battery in Box 7.
boxes[7].remove('tree')
boxes[7].remove('blender')
boxes[7].append('plane')
boxes[7].append('battery')

# Remove the battery and the plane from Box 7.
boxes[7].remove('battery')
boxes[7].remove('plane')

# Remove the meteor from Box 1.
boxes[1].remove('meteor')

# Replace the bird and the microscope with the console and the shoes in Box 2.
boxes[2].remove('bird')
boxes[2].remove('microscope')
boxes[2].append('console')
boxes[2].append('shoes')

# Swap the ship in Box 4 with the shoes in Box 2.
boxes[4].remove('ship')
boxes[2].remove('shoes')
boxes[4].append('shoes')
boxes[2].append('ship')

# Replace the lamp with the blanket in Box 6.
boxes[6].remove('lamp')
boxes[6].append('blanket')

# Put the blender and the tape into Box 13.
boxes[7].remove('blender')
boxes[13].append('blender')
boxes[13].append('tape')

# Swap the ring in Box 0 with the horse in Box 2.
boxes[0].remove('ring')
boxes[2].remove('horse')
boxes[0].append('horse')
boxes[2].append('ring')

# Swap the camera in Box 9 with the oven in Box 2.
boxes[9].remove('camera')
boxes[2].remove('oven')
boxes[9].append('oven')
boxes[2].append('camera')

# Replace the freezer with the bell in Box 7.
boxes[7].remove('freezer')
boxes[7].append('bell')

# Move the soap from Box 14 to Box 10.
boxes[14].remove('soap')
boxes[10].append('soap')

# Swap the truck in Box 13 with the necklace in Box 3.
boxes[13].remove('truck')
boxes[3].remove('necklace')
boxes[13].append('necklace')
boxes[3].append('truck')

# Swap the boot in Box 4 with the bell in Box 7.
boxes[4].remove('boot')
boxes[7].remove('bell')
boxes[4].append('bell')
boxes[7].append('boot')

# Swap the shelf in Box 12 with the game in Box 13.
boxes[12].remove('shelf')
boxes[13].remove('game')
boxes[12].append('game')
boxes[13].append('shelf')

# Swap the oven in Box 9 with the gloves in Box 3.
boxes[9].remove('oven')
boxes[3].remove('gloves')
boxes[9].append('gloves')
boxes[3].append('oven')

# Empty Box 0.
boxes[0] = []

# Move the blanket from Box 6 to Box 10.
boxes[6].remove('blanket')
boxes[10].append('blanket')

# Replace the cup and the basket with the boat and the pillow in Box 8.
boxes[8].remove('cup')
boxes[8].remove('basket')
boxes[8].append('boat')
boxes[8].append('pillow')

# Remove the wire and the boot from Box 7.
boxes[7].remove('wire')
boxes[7].remove('boot')

# Remove the gloves from Box 14.
boxes[14].remove('gloves')

# Remove the fish and the bell from Box 4.
boxes[4].remove('fish')
boxes[4].remove('bell')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
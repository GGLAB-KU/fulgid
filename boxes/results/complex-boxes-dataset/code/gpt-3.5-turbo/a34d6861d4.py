# Initial state of boxes
boxes = {
    0: ['meteor', 'button', 'basket', 'headphone', 'phone'],
    1: ['cup'],
    2: ['camera', 'bicycle', 'coin', 'tape', 'lightning'],
    3: ['console', 'magnet', 'lamp', 'grass', 'planet'],
    4: ['rocket', 'shoe', 'skirt', 'puzzle'],
    5: ['tiger', 'paint', 'shirt', 'belt'],
    6: ['whistle'],
    7: [],
    8: ['game', 'flute', 'blender']
}

# Swap the lamp in Box 3 with the cup in Box 1.
boxes[3].remove('lamp')
boxes[1].remove('cup')
boxes[3].append('cup')
boxes[1].append('lamp')

# Replace the lamp with the vase in Box 1.
boxes[1].remove('lamp')
boxes[1].append('vase')

# Replace the basket and the button with the shirt and the needle in Box 0.
boxes[0].remove('basket')
boxes[0].remove('button')
boxes[0].append('shirt')
boxes[0].append('needle')

# Remove the headphone and the needle and the meteor from Box 0.
items_to_remove = ['headphone', 'needle', 'meteor']
for item in items_to_remove:
    boxes[0].remove(item)

# Remove the rocket from Box 4.
boxes[4].remove('rocket')

# Swap the blender in Box 8 with the shirt in Box 0.
boxes[8].remove('blender')
boxes[0].remove('shirt')
boxes[8].append('shirt')
boxes[0].append('blender')

# Remove the shoe and the puzzle from Box 4.
boxes[4].remove('shoe')
boxes[4].remove('puzzle')

# Swap the whistle in Box 6 with the skirt in Box 4.
boxes[6].remove('whistle')
boxes[4].remove('skirt')
boxes[6].append('skirt')
boxes[4].append('whistle')

# Move the camera from Box 2 to Box 0.
boxes[2].remove('camera')
boxes[0].append('camera')

# Remove the tiger and the paint and the belt from Box 5.
items_to_remove = ['tiger', 'paint', 'belt']
for item in items_to_remove:
    boxes[5].remove(item)

# Replace the skirt with the octopus in Box 6.
boxes[6].remove('skirt')
boxes[6].append('octopus')

# Replace the game and the flute and the shirt with the towel and the wire and the snow in Box 8.
boxes[8].remove('game')
boxes[8].remove('flute')
boxes[8].remove('shirt')
boxes[8].append('towel')
boxes[8].append('wire')
boxes[8].append('snow')

# Replace the planet and the magnet with the plate and the bell in Box 3.
boxes[3].remove('planet')
boxes[3].remove('magnet')
boxes[3].append('plate')
boxes[3].append('bell')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: ['bell', 'violin', 'bus', 'coin'],
    1: ['sculpture', 'belt', 'microwave', 'rock', 'seaweed'],
    2: ['controller'],
    3: ['storm'],
    4: ['magnet', 'thunder', 'blanket', 'dice', 'truck'],
    5: ['river', 'forest', 'rocket', 'comet'],
    6: ['pillow']
}

# Swap the comet in Box 5 with the rock in Box 1.
boxes[1].remove('rock')
boxes[5].remove('comet')
boxes[1].append('comet')
boxes[5].append('rock')

# Remove the river and the forest from Box 5.
boxes[5].remove('river')
boxes[5].remove('forest')

# Remove the controller from Box 2.
boxes[2].remove('controller')

# Swap the pillow in Box 6 with the truck in Box 4.
boxes[4].remove('truck')
boxes[6].remove('pillow')
boxes[4].append('pillow')
boxes[6].append('truck')

# Replace the bus and the coin and the bell with the plate and the ship and the headphone in Box 0.
boxes[0].remove('bus')
boxes[0].remove('coin')
boxes[0].remove('bell')
boxes[0].append('plate')
boxes[0].append('ship')
boxes[0].append('headphone')

# Replace the rock with the comet in Box 5.
boxes[5].remove('rock')
boxes[5].append('comet')

# Move the dice and the magnet from Box 4 to Box 0.
boxes[4].remove('dice')
boxes[4].remove('magnet')
boxes[0].append('dice')
boxes[0].append('magnet')

# Put the puzzle into Box 4.
boxes[4].append('puzzle')

# Swap the storm in Box 3 with the comet in Box 5.
boxes[3].remove('storm')
boxes[5].remove('comet')
boxes[3].append('comet')
boxes[5].append('storm')

# Put the laptop into Box 3.
boxes[3].append('laptop')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
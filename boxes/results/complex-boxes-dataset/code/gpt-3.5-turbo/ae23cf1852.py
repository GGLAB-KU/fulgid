# Initial state of boxes
boxes = {
    0: ['ship', 'shoe', 'lipstick', 'piano', 'magnet'],
    1: ['table', 'mountain'],
    2: [],
    3: ['guitar', 'octopus', 'fish', 'dress', 'helmet'],
    4: ['dog', 'boot', 'coin', 'horn', 'coral'],
    5: ['motorcycle', 'tiger', 'plate', 'island'],
    6: ['gloves', 'clock', 'shampoo'],
    7: ['camera', 'microwave', 'lion', 'leaf', 'razor']
}

# Replace the clock and the shampoo with the comb and the starfish in Box 6.
boxes[6].remove('clock')
boxes[6].remove('shampoo')
boxes[6].append('comb')
boxes[6].append('starfish')

# Swap the dog in Box 4 with the table in Box 1.
boxes[4].remove('dog')
boxes[1].remove('table')
boxes[4].append('table')
boxes[1].append('dog')

# Move the ship and the shoe and the magnet from Box 0 to Box 6.
items_to_move = ['ship', 'shoe', 'magnet']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[6].append(item)

# Put the rock and the river and the storm into Box 1.
items_to_put = ['rock', 'river', 'storm']
for item in items_to_put:
    boxes[1].append(item)

# Remove the camera and the razor and the leaf from Box 7.
items_to_remove = ['camera', 'razor', 'leaf']
for item in items_to_remove:
    boxes[7].remove(item)

# Swap the starfish in Box 6 with the guitar in Box 3.
boxes[6].remove('starfish')
boxes[3].remove('guitar')
boxes[6].append('guitar')
boxes[3].append('starfish')

# Replace the ship with the plane in Box 6.
boxes[6].remove('ship')
boxes[6].append('plane')

# Remove the storm from Box 1.
boxes[1].remove('storm')

# Put the puzzle into Box 4.
boxes[4].append('puzzle')

# Replace the coral with the coin in Box 4.
boxes[4].remove('coral')
boxes[4].append('coin')

# Put the shoes and the lightning into Box 5.
boxes[0].remove('shoe')
boxes[5].append('shoe')
boxes[0].remove('lightning')
boxes[5].append('lightning')

# Move the plate and the island from Box 5 to Box 4.
items_to_move = ['plate', 'island']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
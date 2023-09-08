# Initial state of boxes
boxes = {
    0: [],
    1: ['bracelet', 'desert', 'tiger'],
    2: ['gloves', 'tape'],
    3: ['scarf', 'frame'],
    4: ['forest', 'elephant', 'plate', 'watch', 'umbrella'],
    5: ['scissors', 'phone', 'cat', 'coin'],
    6: [],
    7: [],
    8: [],
    9: ['pot'],
    10: ['bear', 'clock', 'necklace', 'needle']
}

# Replace the pot with the toaster in Box 9.
boxes[9].remove('pot')
boxes[9].append('toaster')

# Swap the gloves in Box 2 with the toaster in Box 9.
boxes[2].remove('gloves')
boxes[9].remove('toaster')
boxes[2].append('toaster')
boxes[9].append('gloves')

# Put the battery and the dolphin into Box 10.
boxes[10].append('battery')
boxes[10].append('dolphin')

# Put the dolphin into Box 0.
boxes[0].append('dolphin')

# Swap the tiger in Box 1 with the scissors in Box 5.
boxes[1].remove('tiger')
boxes[5].remove('scissors')
boxes[1].append('scissors')
boxes[5].append('tiger')

# Remove the scissors from Box 1.
boxes[1].remove('scissors')

# Put the flower and the dolphin and the telescope into Box 4.
boxes[4].append('flower')
boxes[4].append('dolphin')
boxes[4].append('telescope')

# Put the seaweed into Box 3.
boxes[3].append('seaweed')

# Remove the frame and the scarf and the seaweed from Box 3.
boxes[3].remove('frame')
boxes[3].remove('scarf')
boxes[3].remove('seaweed')

# Swap the tape in Box 2 with the dolphin in Box 0.
boxes[2].remove('tape')
boxes[0].remove('dolphin')
boxes[2].append('dolphin')
boxes[0].append('tape')

# Move the forest and the watch from Box 4 to Box 1.
boxes[4].remove('forest')
boxes[4].remove('watch')
boxes[1].append('forest')
boxes[1].append('watch')

# Swap the coin in Box 5 with the telescope in Box 4.
boxes[5].remove('coin')
boxes[4].remove('telescope')
boxes[5].append('telescope')
boxes[4].append('coin')

# Move the dolphin from Box 2 to Box 1.
boxes[2].remove('dolphin')
boxes[1].append('dolphin')

# Put the fridge into Box 0.
boxes[0].append('fridge')

# Move the toaster from Box 2 to Box 5.
boxes[2].remove('toaster')
boxes[5].append('toaster')

# Replace the fridge with the train in Box 0.
boxes[0].remove('fridge')
boxes[0].append('train')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
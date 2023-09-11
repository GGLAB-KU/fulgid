# Initial state of boxes
boxes = {
    0: ['umbrella', 'river', 'octopus', 'scarf'],
    1: ['bag', 'whistle', 'coral', 'mountain', 'bird'],
    2: ['beach', 'shorts', 'brush', 'telescope', 'pot'],
    3: ['bell'],
    4: ['boot', 'mixer', 'dress', 'flute', 'oven'],
    5: ['lightning'],
    6: []
}

# Replace the umbrella with the coin in Box 0.
boxes[0].remove('umbrella')
boxes[0].append('coin')

# Put the lipstick and the train and the earring into Box 6.
items_to_move = ['lipstick', 'train', 'earring']
for item in items_to_move:
    boxes[6].append(item)

# Remove the mixer and the boot from Box 4.
boxes[4].remove('mixer')
boxes[4].remove('boot')

# Put the forest into Box 2.
boxes[2].append('forest')

# Remove the coin and the octopus from Box 0.
boxes[0].remove('coin')
boxes[0].remove('octopus')

# Swap the lipstick in Box 6 with the scarf in Box 0.
boxes[0].remove('scarf')
boxes[6].remove('lipstick')
boxes[0].append('lipstick')
boxes[6].append('scarf')

# Replace the bag and the bird and the mountain with the piano and the microscope and the storm in Box 1.
boxes[1].remove('bag')
boxes[1].remove('bird')
boxes[1].remove('mountain')
boxes[1].append('piano')
boxes[1].append('microscope')
boxes[1].append('storm')

# Swap the river in Box 0 with the dress in Box 4.
boxes[0].remove('river')
boxes[4].remove('dress')
boxes[0].append('dress')
boxes[4].append('river')

# Move the shorts and the forest and the beach from Box 2 to Box 3.
items_to_move = ['shorts', 'forest', 'beach']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Swap the earring in Box 6 with the dress in Box 0.
boxes[0].remove('dress')
boxes[6].remove('earring')
boxes[0].append('earring')
boxes[6].append('dress')

# Swap the forest in Box 3 with the earring in Box 0.
boxes[3].remove('forest')
boxes[0].remove('earring')
boxes[3].append('earring')
boxes[0].append('forest')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
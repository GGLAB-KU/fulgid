# Initial state of boxes
boxes = {
    0: ['necklace'],
    1: [],
    2: ['thunder', 'bell', 'battery', 'umbrella'],
    3: ['rocket', 'lock', 'pan', 'chair', 'charger'],
    4: ['mountain'],
    5: [],
    6: ['desert', 'shorts', 'card'],
    7: [],
    8: ['makeup', 'sun', 'sculpture', 'boat']
}

# Remove the umbrella from Box 2.
boxes[2].remove('umbrella')

# Swap the mountain in Box 4 with the desert in Box 6.
boxes[4], boxes[6] = boxes[6], boxes[4]

# Remove the desert from Box 4.
boxes[4].remove('desert')

# Replace the necklace with the dolphin in Box 0.
boxes[0].remove('necklace')
boxes[0].append('dolphin')

# Move the rocket from Box 3 to Box 7.
boxes[3].remove('rocket')
boxes[7].append('rocket')

# Remove the makeup and the sculpture and the boat from Box 8.
items_to_remove = ['makeup', 'sculpture', 'boat']
for item in items_to_remove:
    boxes[8].remove(item)

# Empty Box 8.
boxes[8] = []

# Swap the charger in Box 3 with the mountain in Box 6.
boxes[3], boxes[6] = boxes[6], boxes[3]

# Put the shampoo and the magnet and the frame into Box 1.
items_to_move = ['shampoo', 'magnet', 'frame']
for item in items_to_move:
    boxes[1].append(item)

# Replace the battery and the thunder and the bell with the speaker and the flute and the hat in Box 2.
boxes[2].remove('battery')
boxes[2].remove('thunder')
boxes[2].remove('bell')
boxes[2].append('speaker')
boxes[2].append('flute')
boxes[2].append('hat')

# Remove the pan from Box 3.
boxes[3].remove('pan')

# Remove the dolphin from Box 0.
boxes[0].remove('dolphin')

# Remove the lock and the mountain and the chair from Box 3.
items_to_remove = ['lock', 'mountain', 'chair']
for item in items_to_remove:
    boxes[3].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
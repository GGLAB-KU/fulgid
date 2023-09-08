# Initial state of boxes
boxes = {
    0: ['clock', 'truck', 'glove'],
    1: ['seaweed'],
    2: ['butterfly'],
    3: [],
    4: [],
    5: ['toothbrush', 'grinder'],
    6: ['beach', 'telescope'],
    7: ['mirror', 'island', 'sun', 'lightning', 'snow'],
    8: ['helmet', 'frame']
}

# Put the fish and the truck into Box 7.
boxes[7].append('fish')
boxes[7].append('truck')

# Replace the fish and the mirror and the sun with the note and the piano and the controller in Box 7.
boxes[7].remove('fish')
boxes[7].remove('mirror')
boxes[7].remove('sun')
boxes[7].append('note')
boxes[7].append('piano')
boxes[7].append('controller')

# Move the lightning from Box 7 to Box 6.
boxes[7].remove('lightning')
boxes[6].append('lightning')

# Put the battery and the bell into Box 4.
boxes[4].append('battery')
boxes[4].append('bell')

# Put the car and the gloves and the boat into Box 3.
boxes[3].append('car')
boxes[3].append('gloves')
boxes[3].append('boat')

# Put the jacket and the blender into Box 6.
boxes[6].append('jacket')
boxes[6].append('blender')

# Move the car from Box 3 to Box 0.
boxes[3].remove('car')
boxes[0].append('car')

# Replace the boat and the gloves with the hat and the microwave in Box 3.
boxes[3].remove('boat')
boxes[3].remove('gloves')
boxes[3].append('hat')
boxes[3].append('microwave')

# Swap the butterfly in Box 2 with the hat in Box 3.
boxes[2].remove('butterfly')
boxes[3].remove('hat')
boxes[2].append('hat')
boxes[3].append('butterfly')

# Move the blender and the telescope from Box 6 to Box 2.
boxes[6].remove('blender')
boxes[6].remove('telescope')
boxes[2].append('blender')
boxes[2].append('telescope')

# Move the seaweed from Box 1 to Box 3.
boxes[1].remove('seaweed')
boxes[3].append('seaweed')

# Remove the lightning and the beach from Box 6.
boxes[6].remove('lightning')
boxes[6].remove('beach')

# Replace the jacket with the watch in Box 6.
boxes[6].remove('jacket')
boxes[6].append('watch')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
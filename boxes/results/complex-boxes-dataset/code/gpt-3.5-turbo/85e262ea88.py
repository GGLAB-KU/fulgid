# Initial state of boxes
boxes = {
    0: ['cat', 'telescope', 'glove'],
    1: ['truck'],
    2: ['seaweed', 'bear', 'moon', 'sock'],
    3: ['bowl', 'umbrella'],
    4: ['horse', 'rock', 'gloves'],
    5: ['cloud', 'forest', 'book']
}

# Swap the moon in Box 2 with the forest in Box 5.
boxes[2].remove('moon')
boxes[5].remove('forest')
boxes[2].append('forest')
boxes[5].append('moon')

# Replace the horse and the rock and the gloves with the mask and the cloud and the wig in Box 4.
boxes[4].remove('horse')
boxes[4].remove('rock')
boxes[4].remove('gloves')
boxes[4].append('mask')
boxes[4].append('cloud')
boxes[4].append('wig')

# Swap the truck in Box 1 with the wig in Box 4.
boxes[1].remove('truck')
boxes[4].remove('wig')
boxes[1].append('wig')
boxes[4].append('truck')

# Swap the bear in Box 2 with the wig in Box 1.
boxes[2].remove('bear')
boxes[1].remove('wig')
boxes[2].append('wig')
boxes[1].append('bear')

# Swap the bear in Box 1 with the moon in Box 5.
boxes[1].remove('bear')
boxes[5].remove('moon')
boxes[1].append('moon')
boxes[5].append('bear')

# Remove the sock from Box 2.
boxes[2].remove('sock')

# Remove the bowl from Box 3.
boxes[3].remove('bowl')

# Remove the umbrella from Box 3.
boxes[3].remove('umbrella')

# Swap the moon in Box 1 with the wig in Box 2.
boxes[1].remove('moon')
boxes[2].remove('wig')
boxes[1].append('wig')
boxes[2].append('moon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
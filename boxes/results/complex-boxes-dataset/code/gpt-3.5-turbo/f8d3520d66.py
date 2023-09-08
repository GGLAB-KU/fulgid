# Initial state of boxes
boxes = {
    0: ['octopus', 'fridge', 'beach', 'glove'],
    1: ['coin'],
    2: ['camera', 'laptop', 'submarine', 'speaker', 'pen'],
    3: [],
    4: ['toy', 'mixer', 'desert'],
    5: [],
    6: ['harmonica'],
    7: ['lion', 'plate', 'belt', 'lightning']
}

# Replace the desert and the mixer and the toy with the cloud and the microwave and the sculpture in Box 4.
boxes[4].remove('desert')
boxes[4].remove('mixer')
boxes[4].remove('toy')
boxes[4].append('cloud')
boxes[4].append('microwave')
boxes[4].append('sculpture')

# Replace the submarine and the pen and the laptop with the toy and the car and the lightning in Box 2.
boxes[2].remove('submarine')
boxes[2].remove('pen')
boxes[2].remove('laptop')
boxes[2].append('toy')
boxes[2].append('car')
boxes[2].append('lightning')

# Remove the belt from Box 7.
boxes[7].remove('belt')

# Move the beach and the octopus from Box 0 to Box 4.
boxes[0].remove('beach')
boxes[0].remove('octopus')
boxes[4].append('beach')
boxes[4].append('octopus')

# Replace the coin with the dress in Box 1.
boxes[1].remove('coin')
boxes[1].append('dress')

# Swap the sculpture in Box 4 with the plate in Box 7.
boxes[4].remove('sculpture')
boxes[7].remove('plate')
boxes[4].append('plate')
boxes[7].append('sculpture')

# Empty Box 2.
boxes[2] = []

# Replace the cloud and the octopus and the beach with the battery and the thread and the umbrella in Box 4.
boxes[4].remove('cloud')
boxes[4].remove('octopus')
boxes[4].remove('beach')
boxes[4].append('battery')
boxes[4].append('thread')
boxes[4].append('umbrella')

# Move the harmonica from Box 6 to Box 4.
boxes[6].remove('harmonica')
boxes[4].append('harmonica')

# Replace the lion and the lightning with the key and the card in Box 7.
boxes[7].remove('lion')
boxes[7].remove('lightning')
boxes[7].append('key')
boxes[7].append('card')

# Replace the key with the forest in Box 7.
boxes[7].remove('key')
boxes[7].append('forest')

# Remove the forest and the card and the sculpture from Box 7.
boxes[7].remove('forest')
boxes[7].remove('card')
boxes[7].remove('sculpture')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
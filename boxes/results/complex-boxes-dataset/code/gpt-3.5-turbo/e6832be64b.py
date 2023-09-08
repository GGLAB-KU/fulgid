# Initial state of boxes
boxes = {
    0: [],
    1: ['mask', 'desert', 'violin', 'rock', 'scarf'],
    2: ['sandals', 'dog', 'coin'],
    3: ['mixer', 'plate', 'cloud', 'dolphin', 'bowl'],
    4: ['pants', 'thunder'],
    5: ['boat'],
    6: ['comb', 'comet'],
    7: ['island', 'toy', 'chair'],
    8: [],
    9: ['seaweed', 'ocean', 'moon', 'storm']
}

# Swap the violin in Box 1 with the moon in Box 9.
boxes[1].remove('violin')
boxes[9].remove('moon')
boxes[1].append('moon')
boxes[9].append('violin')

# Swap the island in Box 7 with the rock in Box 1.
boxes[7].remove('island')
boxes[1].remove('rock')
boxes[7].append('rock')
boxes[1].append('island')

# Swap the mixer in Box 3 with the moon in Box 1.
boxes[3].remove('mixer')
boxes[1].remove('moon')
boxes[3].append('moon')
boxes[1].append('mixer')

# Empty Box 2.
boxes[2] = []

# Empty Box 1.
boxes[1] = []

# Move the violin and the ocean from Box 9 to Box 8.
items_to_move = ['violin', 'ocean']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[8].append(item)

# Remove the toy and the chair and the rock from Box 7.
items_to_remove = ['toy', 'chair', 'rock']
for item in items_to_remove:
    boxes[7].remove(item)

# Empty Box 4.
boxes[4] = []

# Move the boat from Box 5 to Box 2.
boxes[5].remove('boat')
boxes[2].append('boat')

# Replace the boat with the headphone in Box 2.
boxes[2].remove('boat')
boxes[2].append('headphone')

# Put the gloves into Box 6.
boxes[6].append('gloves')

# Put the submarine and the thunder into Box 0.
boxes[0].append('submarine')
boxes[0].append('thunder')

# Put the lion and the bus and the comb into Box 0.
boxes[0].append('lion')
boxes[0].append('bus')
boxes[0].append('comb')

# Replace the lion and the submarine and the thunder with the tape and the lamp and the bracelet in Box 0.
boxes[0].remove('lion')
boxes[0].remove('submarine')
boxes[0].remove('thunder')
boxes[0].append('tape')
boxes[0].append('lamp')
boxes[0].append('bracelet')

# Remove the dolphin and the moon and the cloud from Box 3.
items_to_remove = ['dolphin', 'moon', 'cloud']
for item in items_to_remove:
    boxes[3].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
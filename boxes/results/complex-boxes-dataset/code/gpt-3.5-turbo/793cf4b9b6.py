# Initial state of boxes
boxes = {
    0: ['polish', 'phone', 'tape', 'doll', 'toaster'],
    1: ['cloud', 'butterfly'],
    2: ['earring'],
    3: ['keyboard', 'key'],
    4: ['cow', 'fridge', 'blender'],
    5: ['helmet', 'star', 'bus', 'basket'],
    6: ['shorts', 'violin'],
    7: ['drum', 'thunder', 'meteor', 'fish', 'cup'],
    8: ['perfume', 'desert', 'boot', 'needle'],
    9: ['skirt', 'mirror', 'pen', 'charger'],
    10: ['bag', 'mixer', 'lightning'],
    11: ['toothpaste', 'makeup', 'coat', 'scissors', 'wire'],
    12: [],
    13: ['towel', 'glasses', 'fork', 'flower']
}

# Move the glasses from Box 13 to Box 12.
boxes[13].remove('glasses')
boxes[12].append('glasses')

# Move the mixer and the lightning and the bag from Box 10 to Box 9.
items_to_move = ['mixer', 'lightning', 'bag']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[9].append(item)

# Swap the violin in Box 6 with the thunder in Box 7.
boxes[6].remove('violin')
boxes[7].remove('thunder')
boxes[6].append('thunder')
boxes[7].append('violin')

# Remove the skirt from Box 9.
boxes[9].remove('skirt')

# Replace the pen and the mixer and the mirror with the tiger and the moon and the comb in Box 9.
boxes[9].remove('pen')
boxes[9].remove('mixer')
boxes[9].remove('mirror')
boxes[9].append('tiger')
boxes[9].append('moon')
boxes[9].append('comb')

# Remove the lightning and the comb and the moon from Box 9.
items_to_remove = ['lightning', 'comb', 'moon']
for item in items_to_remove:
    boxes[9].remove(item)

# Put the motorcycle and the shark and the boat into Box 9.
items_to_add = ['motorcycle', 'shark', 'boat']
for item in items_to_add:
    boxes[9].append(item)

# Remove the shorts and the thunder from Box 6.
boxes[6].remove('shorts')
boxes[6].remove('thunder')

# Empty Box 2.
boxes[2] = []

# Move the keyboard and the key from Box 3 to Box 5.
boxes[3].remove('keyboard')
boxes[3].remove('key')
boxes[5].append('keyboard')
boxes[5].append('key')

# Remove the phone and the doll from Box 0.
boxes[0].remove('phone')
boxes[0].remove('doll')

# Move the tiger from Box 9 to Box 13.
boxes[9].remove('tiger')
boxes[13].append('tiger')

# Put the puzzle into Box 13.
boxes[13].append('puzzle')

# Move the tape and the polish from Box 0 to Box 13.
items_to_move = ['tape', 'polish']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[13].append(item)

# Replace the violin and the cup and the fish with the watch and the bear and the key in Box 7.
boxes[7].remove('violin')
boxes[7].remove('cup')
boxes[7].remove('fish')
boxes[7].append('watch')
boxes[7].append('bear')
boxes[7].append('key')

# Move the tape and the polish from Box 13 to Box 2.
items_to_move = ['tape', 'polish']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[2].append(item)

# Replace the wire and the scissors with the octopus and the thread in Box 11.
boxes[11].remove('wire')
boxes[11].remove('scissors')
boxes[11].append('octopus')
boxes[11].append('thread')

# Swap the cloud in Box 1 with the charger in Box 9.
boxes[1].remove('cloud')
boxes[9].remove('charger')
boxes[1].append('charger')
boxes[9].append('cloud')

# Swap the blender in Box 4 with the cloud in Box 9.
boxes[4].remove('blender')
boxes[9].remove('cloud')
boxes[4].append('cloud')
boxes[9].append('blender')

# Replace the desert with the thread in Box 8.
boxes[8].remove('desert')
boxes[8].append('thread')

# Move the charger and the butterfly from Box 1 to Box 7.
boxes[1].remove('charger')
boxes[1].remove('butterfly')
boxes[7].append('charger')
boxes[7].append('butterfly')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
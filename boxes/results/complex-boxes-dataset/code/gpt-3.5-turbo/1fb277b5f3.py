# Initial state of boxes
boxes = {
    0: ['microwave'],
    1: [],
    2: ['brush', 'bracelet', 'pants', 'rock'],
    3: ['flute', 'moon', 'polish'],
    4: ['speaker', 'motorcycle', 'island'],
    5: ['lamp', 'jacket', 'scissors', 'console', 'soap'],
    6: [],
    7: ['tape'],
    8: ['clock', 'crown', 'pen', 'blender', 'glasses'],
    9: [],
    10: ['mirror', 'paint', 'shelf', 'bird', 'sock']
}

# Replace the flute and the polish and the moon with the card and the charger and the bracelet in Box 3.
boxes[3].remove('flute')
boxes[3].remove('moon')
boxes[3].remove('polish')
boxes[3].append('card')
boxes[3].append('charger')
boxes[3].append('bracelet')

# Swap the pants in Box 2 with the card in Box 3.
boxes[2].remove('pants')
boxes[3].remove('card')
boxes[2].append('card')
boxes[3].append('pants')

# Swap the bracelet in Box 3 with the mirror in Box 10.
boxes[3].remove('bracelet')
boxes[10].remove('mirror')
boxes[3].append('mirror')
boxes[10].append('bracelet')

# Move the tape from Box 7 to Box 2.
boxes[7].remove('tape')
boxes[2].append('tape')

# Swap the island in Box 4 with the jacket in Box 5.
boxes[4].remove('island')
boxes[5].remove('jacket')
boxes[4].append('jacket')
boxes[5].append('island')

# Move the tape from Box 2 to Box 6.
boxes[2].remove('tape')
boxes[6].append('tape')

# Replace the speaker and the motorcycle with the phone and the coin in Box 4.
boxes[4].remove('speaker')
boxes[4].remove('motorcycle')
boxes[4].append('phone')
boxes[4].append('coin')

# Replace the microwave with the blanket in Box 0.
boxes[0].remove('microwave')
boxes[0].append('blanket')

# Put the cloud and the swimsuit and the speaker into Box 5.
boxes[5].append('cloud')
boxes[5].append('swimsuit')
boxes[5].append('speaker')

# Swap the crown in Box 8 with the card in Box 2.
boxes[8].remove('crown')
boxes[2].remove('card')
boxes[8].append('card')
boxes[2].append('crown')

# Swap the jacket in Box 4 with the charger in Box 3.
boxes[4].remove('jacket')
boxes[3].remove('charger')
boxes[4].append('charger')
boxes[3].append('jacket')

# Move the shelf and the bracelet from Box 10 to Box 4.
boxes[10].remove('shelf')
boxes[10].remove('bracelet')
boxes[4].append('shelf')
boxes[4].append('bracelet')

# Swap the jacket in Box 3 with the bracelet in Box 2.
boxes[3].remove('jacket')
boxes[2].remove('bracelet')
boxes[3].append('bracelet')
boxes[2].append('jacket')

# Swap the pants in Box 3 with the charger in Box 4.
boxes[3].remove('pants')
boxes[4].remove('charger')
boxes[3].append('charger')
boxes[4].append('pants')

# Remove the sock from Box 10.
boxes[10].remove('sock')

# Remove the rock and the brush and the crown from Box 2.
boxes[2].remove('rock')
boxes[2].remove('brush')
boxes[2].remove('crown')

# Replace the cloud and the lamp and the speaker with the thread and the train and the mountain in Box 5.
boxes[5].remove('cloud')
boxes[5].remove('lamp')
boxes[5].remove('speaker')
boxes[5].append('thread')
boxes[5].append('train')
boxes[5].append('mountain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
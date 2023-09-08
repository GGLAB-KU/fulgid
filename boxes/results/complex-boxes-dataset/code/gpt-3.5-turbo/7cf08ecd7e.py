# Initial state of boxes
boxes = {
    0: ['motorcycle'],
    1: ['fish', 'thread', 'mirror'],
    2: ['phone', 'towel', 'shorts', 'fridge'],
    3: [],
    4: ['blanket'],
    5: ['apple', 'note'],
    6: ['violin', 'bag', 'horn']
}

# Replace the violin and the horn and the bag with the starfish and the speaker and the wig in Box 6.
boxes[6].remove('violin')
boxes[6].remove('bag')
boxes[6].remove('horn')
boxes[6].append('starfish')
boxes[6].append('speaker')
boxes[6].append('wig')

# Swap the blanket in Box 4 with the motorcycle in Box 0.
boxes[0].remove('motorcycle')
boxes[4].remove('blanket')
boxes[0].append('blanket')
boxes[4].append('motorcycle')

# Empty Box 2.
boxes[2] = []

# Swap the thread in Box 1 with the note in Box 5.
boxes[1].remove('thread')
boxes[5].remove('note')
boxes[1].append('note')
boxes[5].append('thread')

# Put the coat into Box 1.
boxes[1].append('coat')

# Move the motorcycle from Box 4 to Box 2.
boxes[4].remove('motorcycle')
boxes[2].append('motorcycle')

# Replace the fish and the note and the coat with the gloves and the flower and the magnet in Box 1.
boxes[1].remove('fish')
boxes[1].remove('note')
boxes[1].remove('coat')
boxes[1].append('gloves')
boxes[1].append('flower')
boxes[1].append('magnet')

# Replace the blanket with the horse in Box 0.
boxes[0].remove('blanket')
boxes[0].append('horse')

# Move the flower and the magnet from Box 1 to Box 3.
boxes[1].remove('flower')
boxes[1].remove('magnet')
boxes[3].append('flower')
boxes[3].append('magnet')

# Put the ocean and the cloud into Box 2.
boxes[2].append('ocean')
boxes[2].append('cloud')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
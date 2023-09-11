# Initial state of boxes
boxes = {
    0: ['thunder'],
    1: ['rain'],
    2: ['dolphin', 'belt', 'rock'],
    3: ['fish'],
    4: ['dress', 'piano', 'motorcycle', 'horse', 'toothpaste'],
    5: [],
    6: ['speaker', 'pot', 'harmonica', 'polish'],
    7: ['magnet', 'lock'],
    8: ['button', 'pan'],
    9: ['phone', 'watch', 'skirt'],
    10: ['bell', 'necklace', 'pillow', 'desert', 'console'],
    11: ['fridge', 'ocean', 'tiger', 'laptop'],
    12: ['blender', 'razor', 'lipstick', 'glove']
}

# Move the harmonica and the pot and the speaker from Box 6 to Box 2.
items_to_move = ['harmonica', 'pot', 'speaker']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Replace the speaker and the dolphin and the rock with the star and the puzzle and the fridge in Box 2.
boxes[2].remove('speaker')
boxes[2].remove('dolphin')
boxes[2].remove('rock')
boxes[2].append('star')
boxes[2].append('puzzle')
boxes[2].append('fridge')

# Remove the belt and the puzzle and the fridge from Box 2.
items_to_remove = ['belt', 'puzzle', 'fridge']
for item in items_to_remove:
    boxes[2].remove(item)

# Swap the magnet in Box 7 with the harmonica in Box 2.
boxes[7].remove('magnet')
boxes[2].remove('harmonica')
boxes[7].append('harmonica')
boxes[2].append('magnet')

# Remove the fish from Box 3.
boxes[3].remove('fish')

# Put the elephant and the fork into Box 11.
boxes[11].append('elephant')
boxes[11].append('fork')

# Put the gloves and the thread and the crown into Box 5.
items_to_move = ['gloves', 'thread', 'crown']
for item in items_to_move:
    boxes[5].append(item)

# Move the skirt from Box 9 to Box 8.
boxes[9].remove('skirt')
boxes[8].append('skirt')

# Put the mountain and the pen into Box 6.
boxes[6].append('mountain')
boxes[6].append('pen')

# Replace the glove and the blender with the ring and the train in Box 12.
boxes[12].remove('glove')
boxes[12].remove('blender')
boxes[12].append('ring')
boxes[12].append('train')

# Put the dog and the drum into Box 12.
boxes[12].append('dog')
boxes[12].append('drum')

# Replace the dog with the magnet in Box 12.
boxes[12].remove('dog')
boxes[12].append('magnet')

# Move the thunder from Box 0 to Box 10.
boxes[0].remove('thunder')
boxes[10].append('thunder')

# Swap the watch in Box 9 with the gloves in Box 5.
boxes[9].remove('watch')
boxes[5].remove('gloves')
boxes[9].append('gloves')
boxes[5].append('watch')

# Empty Box 5.
boxes[5] = []

# Remove the ring from Box 12.
boxes[12].remove('ring')

# Remove the magnet from Box 2.
boxes[2].remove('magnet')

# Remove the console and the pillow and the desert from Box 10.
items_to_remove = ['console', 'pillow', 'desert']
for item in items_to_remove:
    boxes[10].remove(item)

# Put the elephant and the forest into Box 5.
boxes[5].append('elephant')
boxes[5].append('forest')

# Remove the mountain and the polish from Box 6.
boxes[6].remove('mountain')
boxes[6].remove('polish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
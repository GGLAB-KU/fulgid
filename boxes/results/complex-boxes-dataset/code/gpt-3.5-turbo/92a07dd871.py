# Initial state of boxes
boxes = {
    0: ['ship', 'plane', 'ring', 'swimsuit', 'towel'],
    1: ['truck', 'horn', 'wig', 'shoes', 'keyboard'],
    2: ['drum', 'branch'],
    3: ['doll', 'tree', 'glasses'],
    4: ['storm', 'piano', 'pan', 'skirt', 'coin'],
    5: [],
    6: ['octopus', 'watch', 'river', 'sock'],
    7: ['paint'],
    8: ['butterfly', 'seaweed', 'lightning', 'battery']
}

# Replace the plane with the harmonica in Box 0.
boxes[0].remove('plane')
boxes[0].append('harmonica')

# Swap the tree in Box 3 with the skirt in Box 4.
boxes[3].remove('tree')
boxes[4].remove('skirt')
boxes[3].append('skirt')
boxes[4].append('tree')

# Move the storm from Box 4 to Box 5.
boxes[4].remove('storm')
boxes[5].append('storm')

# Put the keyboard and the rain into Box 7.
boxes[1].remove('keyboard')
boxes[7].append('keyboard')
boxes[7].append('rain')

# Move the butterfly from Box 8 to Box 4.
boxes[8].remove('butterfly')
boxes[4].append('butterfly')

# Move the octopus and the sock and the river from Box 6 to Box 7.
items_to_move = ['octopus', 'sock', 'river']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[7].append(item)

# Remove the storm from Box 5.
boxes[5].remove('storm')

# Replace the piano with the spoon in Box 4.
boxes[4].remove('piano')
boxes[4].append('spoon')

# Swap the branch in Box 2 with the swimsuit in Box 0.
boxes[2].remove('branch')
boxes[0].remove('swimsuit')
boxes[2].append('swimsuit')
boxes[0].append('branch')

# Move the watch from Box 6 to Box 0.
boxes[6].remove('watch')
boxes[0].append('watch')

# Put the horn and the sock and the bracelet into Box 8.
items_to_move = ['horn', 'sock', 'bracelet']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Remove the horn from Box 1.
boxes[1].remove('horn')

# Swap the drum in Box 2 with the rain in Box 7.
boxes[2].remove('drum')
boxes[7].remove('rain')
boxes[2].append('rain')
boxes[7].append('drum')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
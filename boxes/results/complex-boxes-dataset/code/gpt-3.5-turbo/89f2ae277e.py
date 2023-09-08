# Initial state of boxes
boxes = {
    0: ['mirror', 'rock', 'microscope'],
    1: ['note', 'comet', 'thread', 'truck', 'coin'],
    2: [],
    3: ['skirt', 'ring', 'vase', 'pen'],
    4: ['forest', 'game', 'lion', 'table'],
    5: ['towel', 'rain', 'flower', 'snow'],
    6: ['coat', 'bell', 'island', 'mixer'],
    7: ['makeup', 'phone', 'harmonica', 'motorcycle', 'tiger']
}

# Remove the vase from Box 3.
boxes[3].remove('vase')

# Replace the skirt and the pen and the ring with the butterfly and the plane and the speaker in Box 3.
boxes[3].remove('skirt')
boxes[3].remove('pen')
boxes[3].remove('ring')
boxes[3].append('butterfly')
boxes[3].append('plane')
boxes[3].append('speaker')

# Replace the rain and the snow and the flower with the controller and the ship and the scarf in Box 5.
boxes[5].remove('rain')
boxes[5].remove('snow')
boxes[5].remove('flower')
boxes[5].append('controller')
boxes[5].append('ship')
boxes[5].append('scarf')

# Replace the comet and the note with the wire and the river in Box 1.
boxes[1].remove('comet')
boxes[1].remove('note')
boxes[1].append('wire')
boxes[1].append('river')

# Replace the table with the freezer in Box 4.
boxes[4].remove('table')
boxes[4].append('freezer')

# Move the thread from Box 1 to Box 3.
boxes[1].remove('thread')
boxes[3].append('thread')

# Swap the freezer in Box 4 with the tiger in Box 7.
boxes[4].remove('freezer')
boxes[7].remove('tiger')
boxes[4].append('tiger')
boxes[7].append('freezer')

# Swap the island in Box 6 with the wire in Box 1.
boxes[6].remove('island')
boxes[1].remove('wire')
boxes[6].append('wire')
boxes[1].append('island')

# Remove the butterfly and the thread and the speaker from Box 3.
boxes[3].remove('butterfly')
boxes[3].remove('thread')
boxes[3].remove('speaker')

# Put the swimsuit and the mountain and the island into Box 6.
boxes[6].append('swimsuit')
boxes[6].append('mountain')
boxes[6].append('island')

# Move the truck from Box 1 to Box 0.
boxes[1].remove('truck')
boxes[0].append('truck')

# Remove the swimsuit and the mountain and the wire from Box 6.
boxes[6].remove('swimsuit')
boxes[6].remove('mountain')
boxes[6].remove('wire')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
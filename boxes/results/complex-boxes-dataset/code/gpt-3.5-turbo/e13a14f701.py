# Initial state of boxes
boxes = {
    0: ['sun', 'dice', 'cloud', 'thunder'],
    1: [],
    2: ['wig', 'hat', 'key', 'controller'],
    3: ['whistle', 'horse'],
    4: ['blanket', 'fish'],
    5: ['mask', 'cow', 'soap', 'plate', 'dog'],
    6: ['note'],
    7: ['toaster']
}

# Replace the thunder and the cloud with the needle and the boat in Box 0.
boxes[0].remove('thunder')
boxes[0].remove('cloud')
boxes[0].append('needle')
boxes[0].append('boat')

# Put the sun and the spoon into Box 2.
boxes[2].append('sun')
boxes[2].append('spoon')

# Remove the horse from Box 3.
boxes[3].remove('horse')

# Put the grinder and the bell into Box 5.
boxes[5].append('grinder')
boxes[5].append('bell')

# Move the whistle from Box 3 to Box 7.
boxes[3].remove('whistle')
boxes[7].append('whistle')

# Swap the toaster in Box 7 with the blanket in Box 4.
boxes[7].remove('toaster')
boxes[4].remove('blanket')
boxes[7].append('blanket')
boxes[4].append('toaster')

# Replace the whistle and the blanket with the dice and the ship in Box 7.
boxes[7].remove('whistle')
boxes[7].remove('blanket')
boxes[7].append('dice')
boxes[7].append('ship')

# Replace the fish and the toaster with the rock and the keyboard in Box 4.
boxes[4].remove('fish')
boxes[4].remove('toaster')
boxes[4].append('rock')
boxes[4].append('keyboard')

# Remove the ship and the dice from Box 7.
boxes[7].remove('ship')
boxes[7].remove('dice')

# Remove the note from Box 6.
boxes[6].remove('note')

# Put the coin into Box 1.
boxes[1].append('coin')

# Swap the sun in Box 0 with the keyboard in Box 4.
boxes[0].remove('sun')
boxes[4].remove('keyboard')
boxes[0].append('keyboard')
boxes[4].append('sun')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
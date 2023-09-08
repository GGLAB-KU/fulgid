# Initial state of boxes
boxes = {
    0: ['bird', 'bell'],
    1: ['wire', 'river', 'comet', 'camera', 'sock'],
    2: ['dog', 'table', 'sandals'],
    3: ['cat', 'pants'],
    4: ['bicycle', 'magnet', 'scissors', 'whistle', 'soap']
}

# Put the grinder and the vase into Box 4.
boxes[4].append('grinder')
boxes[4].append('vase')

# Put the ship and the ring into Box 1.
boxes[1].append('ship')
boxes[1].append('ring')

# Replace the whistle and the magnet and the scissors with the shelf and the butterfly and the plate in Box 4.
boxes[4].remove('whistle')
boxes[4].remove('magnet')
boxes[4].remove('scissors')
boxes[4].append('shelf')
boxes[4].append('butterfly')
boxes[4].append('plate')

# Put the moon into Box 4.
boxes[4].append('moon')

# Move the wire from Box 1 to Box 2.
boxes[1].remove('wire')
boxes[2].append('wire')

# Swap the ship in Box 1 with the cat in Box 3.
boxes[1].remove('ship')
boxes[3].remove('cat')
boxes[1].append('cat')
boxes[3].append('ship')

# Swap the butterfly in Box 4 with the sandals in Box 2.
boxes[4].remove('butterfly')
boxes[2].remove('sandals')
boxes[4].append('sandals')
boxes[2].append('butterfly')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
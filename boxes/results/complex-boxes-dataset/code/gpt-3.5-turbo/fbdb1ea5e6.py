# Initial state of boxes
boxes = {
    0: ['speaker'],
    1: ['coral', 'flower'],
    2: ['tie', 'lipstick', 'battery', 'helmet', 'glasses'],
    3: ['jacket', 'rocket'],
    4: [],
    5: [],
    6: ['meteor', 'telescope', 'lock', 'pan'],
    7: ['table', 'lightning'],
    8: [],
    9: ['crown', 'key', 'camera'],
    10: ['pillow', 'snow'],
    11: ['blanket', 'toaster', 'tiger', 'storm', 'plate'],
    12: []
}

# Swap the lightning in Box 7 with the pan in Box 6.
boxes[7].remove('lightning')
boxes[6].remove('pan')
boxes[7].append('pan')
boxes[6].append('lightning')

# Put the controller into Box 10.
boxes[10].append('controller')

# Put the umbrella and the glasses into Box 11.
boxes[11].append('umbrella')
boxes[11].append('glasses')

# Swap the table in Box 7 with the storm in Box 11.
boxes[7].remove('table')
boxes[11].remove('storm')
boxes[7].append('storm')
boxes[11].append('table')

# Empty Box 7.
boxes[7] = []

# Replace the crown and the camera and the key with the apple and the train and the sun in Box 9.
boxes[9].remove('crown')
boxes[9].remove('key')
boxes[9].remove('camera')
boxes[9].append('apple')
boxes[9].append('train')
boxes[9].append('sun')

# Swap the flower in Box 1 with the blanket in Box 11.
boxes[1].remove('flower')
boxes[11].remove('blanket')
boxes[1].append('blanket')
boxes[11].append('flower')

# Move the speaker from Box 0 to Box 7.
boxes[0].remove('speaker')
boxes[7].append('speaker')

# Put the gloves and the drum and the tiger into Box 2.
boxes[2].append('gloves')
boxes[2].append('drum')
boxes[2].append('tiger')

# Replace the jacket and the rocket with the plane and the cow in Box 3.
boxes[3].remove('jacket')
boxes[3].remove('rocket')
boxes[3].append('plane')
boxes[3].append('cow')

# Replace the plane with the butterfly in Box 3.
boxes[3].remove('plane')
boxes[3].append('butterfly')

# Move the toaster from Box 11 to Box 4.
boxes[11].remove('toaster')
boxes[4].append('toaster')

# Swap the toaster in Box 4 with the lipstick in Box 2.
boxes[4].remove('toaster')
boxes[2].remove('lipstick')
boxes[4].append('lipstick')
boxes[2].append('toaster')

# Remove the speaker from Box 7.
boxes[7].remove('speaker')

# Put the ship and the tape into Box 12.
boxes[12].append('ship')
boxes[12].append('tape')

# Put the fork into Box 0.
boxes[0].append('fork')

# Replace the telescope and the lock with the pot and the mirror in Box 6.
boxes[6].remove('telescope')
boxes[6].remove('lock')
boxes[6].append('pot')
boxes[6].append('mirror')

# Remove the sun and the train from Box 9.
boxes[9].remove('sun')
boxes[9].remove('train')

# Swap the plate in Box 11 with the ship in Box 12.
boxes[11].remove('plate')
boxes[12].remove('ship')
boxes[11].append('ship')
boxes[12].append('plate')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
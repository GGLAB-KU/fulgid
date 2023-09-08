# Initial state of boxes
boxes = {
    0: ['chair', 'toaster'],
    1: ['shoes', 'basket', 'fridge'],
    2: ['ring', 'pan', 'crown', 'storm'],
    3: ['speaker', 'makeup'],
    4: ['tree', 'harmonica'],
    5: ['sun', 'bird', 'camera', 'octopus']
}

# Put the tape into Box 5.
boxes[5].append('tape')

# Remove the harmonica and the tree from Box 4.
boxes[4].remove('tree')
boxes[4].remove('harmonica')

# Remove the ring and the pan and the storm from Box 2.
boxes[2].remove('ring')
boxes[2].remove('pan')
boxes[2].remove('storm')

# Put the octopus and the necklace into Box 1.
boxes[1].append('octopus')
boxes[1].append('necklace')

# Swap the crown in Box 2 with the speaker in Box 3.
boxes[2].remove('crown')
boxes[3].remove('speaker')
boxes[2].append('speaker')
boxes[3].append('crown')

# Replace the necklace with the lipstick in Box 1.
boxes[1].remove('necklace')
boxes[1].append('lipstick')

# Move the speaker from Box 2 to Box 5.
boxes[2].remove('speaker')
boxes[5].append('speaker')

# Replace the shoes and the fridge with the plate and the plane in Box 1.
boxes[1].remove('shoes')
boxes[1].remove('fridge')
boxes[1].append('plate')
boxes[1].append('plane')

# Move the chair from Box 0 to Box 2.
boxes[0].remove('chair')
boxes[2].append('chair')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: [],
    1: ['boot', 'lipstick', 'shoe'],
    2: ['needle', 'star'],
    3: ['razor', 'pen'],
    4: [],
    5: ['microwave', 'truck', 'comb'],
    6: ['plate', 'shorts', 'umbrella', 'cat', 'flute'],
    7: ['blanket', 'blender']
}

# Move the razor from Box 3 to Box 7.
boxes[3].remove('razor')
boxes[7].append('razor')

# Replace the microwave and the truck with the octopus and the freezer in Box 5.
boxes[5].remove('microwave')
boxes[5].remove('truck')
boxes[5].append('octopus')
boxes[5].append('freezer')

# Remove the pen from Box 3.
boxes[3].remove('pen')

# Put the swimsuit and the lamp into Box 1.
boxes[1].append('swimsuit')
boxes[1].append('lamp')

# Replace the umbrella and the plate with the elephant and the brush in Box 6.
boxes[6].remove('umbrella')
boxes[6].remove('plate')
boxes[6].append('elephant')
boxes[6].append('brush')

# Move the shorts and the flute from Box 6 to Box 3.
boxes[6].remove('shorts')
boxes[6].remove('flute')
boxes[3].append('shorts')
boxes[3].append('flute')

# Move the needle from Box 2 to Box 4.
boxes[2].remove('needle')
boxes[4].append('needle')

# Put the shoe and the bicycle into Box 3.
boxes[3].append('shoe')
boxes[3].append('bicycle')

# Remove the lamp and the lipstick and the swimsuit from Box 1.
boxes[1].remove('lamp')
boxes[1].remove('lipstick')
boxes[1].remove('swimsuit')

# Move the blanket and the razor from Box 7 to Box 0.
boxes[7].remove('blanket')
boxes[7].remove('razor')
boxes[0].append('blanket')
boxes[0].append('razor')

# Put the controller into Box 5.
boxes[5].append('controller')

# Move the cat and the brush and the elephant from Box 6 to Box 0.
boxes[6].remove('cat')
boxes[6].remove('brush')
boxes[6].remove('elephant')
boxes[0].append('cat')
boxes[0].append('brush')
boxes[0].append('elephant')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
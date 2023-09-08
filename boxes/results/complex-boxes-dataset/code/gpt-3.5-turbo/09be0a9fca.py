# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['telescope', 'butterfly', 'mountain', 'dolphin', 'sculpture'],
    3: ['necklace'],
    4: ['laptop', 'toaster'],
    5: ['cow', 'dress', 'shirt', 'watch', 'seaweed'],
    6: ['bus', 'helmet', 'razor', 'star', 'storm'],
    7: ['fridge'],
    8: ['sandals', 'dice', 'glove', 'microwave', 'submarine'],
    9: ['rain', 'planet'],
    10: ['freezer', 'leaf', 'branch', 'battery'],
    11: [],
    12: ['thunder', 'paint'],
    13: ['usb', 'doll']
}

# Replace the submarine and the microwave with the coin and the button in Box 8.
boxes[8].remove('submarine')
boxes[8].remove('microwave')
boxes[8].append('coin')
boxes[8].append('button')

# Put the perfume and the elephant into Box 1.
boxes[1].append('perfume')
boxes[1].append('elephant')

# Put the bicycle into Box 1.
boxes[1].append('bicycle')

# Empty Box 8.
boxes[8] = []

# Replace the laptop and the toaster with the hat and the glasses in Box 4.
boxes[4].remove('laptop')
boxes[4].remove('toaster')
boxes[4].append('hat')
boxes[4].append('glasses')

# Replace the doll with the plate in Box 13.
boxes[13].remove('doll')
boxes[13].append('plate')

# Replace the planet and the rain with the helmet and the plate in Box 9.
boxes[9].remove('planet')
boxes[9].remove('rain')
boxes[9].append('helmet')
boxes[9].append('plate')

# Replace the plate with the microscope in Box 13.
boxes[13].remove('plate')
boxes[13].append('microscope')

# Put the pants into Box 13.
boxes[13].append('pants')

# Put the table and the boat into Box 13.
boxes[13].append('table')
boxes[13].append('boat')

# Replace the pants and the table with the starfish and the book in Box 13.
boxes[13].remove('pants')
boxes[13].remove('table')
boxes[13].append('starfish')
boxes[13].append('book')

# Put the shoes and the elephant and the toaster into Box 6.
boxes[6].append('shoes')
boxes[6].append('elephant')
boxes[6].append('toaster')

# Remove the helmet from Box 9.
boxes[9].remove('helmet')

# Remove the hat from Box 4.
boxes[4].remove('hat')

# Move the freezer and the leaf from Box 10 to Box 1.
boxes[10].remove('freezer')
boxes[10].remove('leaf')
boxes[1].append('freezer')
boxes[1].append('leaf')

# Remove the bicycle from Box 1.
boxes[1].remove('bicycle')

# Move the branch from Box 10 to Box 8.
boxes[10].remove('branch')
boxes[8].append('branch')

# Replace the leaf and the freezer and the elephant with the drum and the battery and the frame in Box 1.
boxes[1].remove('leaf')
boxes[1].remove('freezer')
boxes[1].remove('elephant')
boxes[1].append('drum')
boxes[1].append('battery')
boxes[1].append('frame')

# Put the jacket into Box 7.
boxes[7].append('jacket')

# Move the jacket from Box 7 to Box 13.
boxes[7].remove('jacket')
boxes[13].append('jacket')

# Move the fridge from Box 7 to Box 12.
boxes[7].remove('fridge')
boxes[12].append('fridge')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
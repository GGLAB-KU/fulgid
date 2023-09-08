# Initial state of boxes
boxes = {
    0: ['needle', 'bowl', 'lightning'],
    1: ['console', 'umbrella', 'blender', 'planet'],
    2: ['car'],
    3: ['seaweed'],
    4: [],
    5: ['whistle'],
    6: ['sock', 'jacket', 'wire'],
    7: ['horse'],
    8: ['hat'],
    9: ['skirt'],
    10: ['sculpture', 'storm', 'plane', 'earring'],
    11: [],
    12: ['spoon', 'shark', 'harmonica', 'plate']
}

# Move the car from Box 2 to Box 4.
boxes[2].remove('car')
boxes[4].append('car')

# Move the earring and the plane from Box 10 to Box 11.
boxes[10].remove('earring')
boxes[10].remove('plane')
boxes[11].append('earring')
boxes[11].append('plane')

# Empty Box 3.
boxes[3] = []

# Replace the shark and the plate with the boot and the mask in Box 12.
boxes[12].remove('shark')
boxes[12].remove('plate')
boxes[12].append('boot')
boxes[12].append('mask')

# Swap the bowl in Box 0 with the hat in Box 8.
boxes[0].remove('bowl')
boxes[8].remove('hat')
boxes[0].append('hat')
boxes[8].append('bowl')

# Put the grinder and the comet and the microscope into Box 3.
items_to_move = ['grinder', 'comet', 'microscope']
for item in items_to_move:
    boxes[3].append(item)

# Swap the console in Box 1 with the grinder in Box 3.
boxes[1].remove('console')
boxes[3].remove('grinder')
boxes[1].append('grinder')
boxes[3].append('console')

# Remove the wire and the jacket from Box 6.
boxes[6].remove('wire')
boxes[6].remove('jacket')

# Replace the plane and the earring with the fridge and the battery in Box 11.
boxes[11].remove('plane')
boxes[11].remove('earring')
boxes[11].append('fridge')
boxes[11].append('battery')

# Move the whistle from Box 5 to Box 3.
boxes[5].remove('whistle')
boxes[3].append('whistle')

# Remove the storm from Box 10.
boxes[10].remove('storm')

# Replace the hat and the lightning and the needle with the perfume and the toaster and the flower in Box 0.
boxes[0].remove('hat')
boxes[0].remove('lightning')
boxes[0].remove('needle')
boxes[0].append('perfume')
boxes[0].append('toaster')
boxes[0].append('flower')

# Remove the microscope and the console and the whistle from Box 3.
boxes[3].remove('microscope')
boxes[3].remove('console')
boxes[3].remove('whistle')

# Swap the bowl in Box 8 with the harmonica in Box 12.
boxes[8].remove('bowl')
boxes[12].remove('harmonica')
boxes[8].append('harmonica')
boxes[12].append('bowl')

# Replace the fridge with the wallet in Box 11.
boxes[11].remove('fridge')
boxes[11].append('wallet')

# Remove the car from Box 4.
boxes[4].remove('car')

# Remove the sculpture from Box 10.
boxes[10].remove('sculpture')

# Move the skirt from Box 9 to Box 6.
boxes[9].remove('skirt')
boxes[6].append('skirt')

# Replace the mask with the polish in Box 12.
boxes[12].remove('mask')
boxes[12].append('polish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
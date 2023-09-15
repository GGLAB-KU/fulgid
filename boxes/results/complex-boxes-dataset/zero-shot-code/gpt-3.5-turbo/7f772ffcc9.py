box = {
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

def print_boxes():
    for i in range(13):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Move the car from Box 2 to Box 4
box[4].append(box[2].pop(0))

# Move the earring and the plane from Box 10 to Box 11
box[11].extend(box[10].pop(3))
box[11].extend(box[10].pop(2))

# Empty Box 3
box[3] = []

# Replace the shark and the plate with the boot and the mask in Box 12
box[12].remove('shark')
box[12].remove('plate')
box[12].extend(['boot', 'mask'])

# Swap the bowl in Box 0 with the hat in Box 8
box[0][box[0].index('bowl')] = 'hat'
box[8] = ['bowl']

# Put the grinder and the comet and the microscope into Box 3
box[3].extend(['grinder', 'comet', 'microscope'])

# Swap the console in Box 1 with the grinder in Box 3
box[1][box[1].index('console')] = 'grinder'
box[3][box[3].index('grinder')] = 'console'

# Remove the wire and the jacket from Box 6
box[6].remove('wire')
box[6].remove('jacket')

# Replace the plane and the earring with the fridge and the battery in Box 11
box[11][box[11].index('plane')] = 'fridge'
box[11][box[11].index('earring')] = 'battery'

# Move the whistle from Box 5 to Box 3
box[3].append(box[5].pop(0))

# Remove the storm from Box 10
box[10].remove('storm')

# Replace the hat and the lightning and the needle with the perfume and the toaster and the flower in Box 0
box[0][box[0].index('hat')] = 'perfume'
box[0][box[0].index('lightning')] = 'toaster'
box[0][box[0].index('needle')] = 'flower'

# Remove the microscope and the console and the whistle from Box 3
box[3].remove('microscope')
box[3].remove('console')
box[3].remove('whistle')

# Swap the bowl in Box 8 with the harmonica in Box 12
box[8][box[8].index('bowl')] = 'harmonica'
box[12][box[12].index('harmonica')] = 'bowl'

# Replace the fridge with the wallet in Box 11
box[11][box[11].index('fridge')] = 'wallet'

# Remove the car from Box 4
box[4].remove('car')

# Remove the sculpture from Box 10
box[10].remove('sculpture')

# Move the skirt from Box 9 to Box 6
box[6].append(box[9].pop(0))

# Replace the mask with the polish in Box 12
box[12][box[12].index('mask')] = 'polish'

# Print the final state of the boxes
print_boxes()
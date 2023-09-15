box = {
    0: ['elephant', 'blender', 'umbrella', 'flower'],
    1: [],
    2: ['tape', 'thread'],
    3: ['horse', 'shorts', 'gloves', 'magnet'],
    4: ['vase', 'frame', 'doll', 'toothpaste', 'scarf'],
    5: ['earring', 'meteor'],
    6: ['pillow', 'bell'],
    7: ['plate'],
    8: ['bowl', 'horn', 'harmonica'],
    9: [],
    10: [],
    11: [],
    12: ['rain'],
    13: ['paint', 'sun']
}

# Move the umbrella and the flower from Box 0 to Box 3
box[3].extend(box[0].pop(box[0].index('umbrella')))
box[3].extend(box[0].pop(box[0].index('flower')))

# Put the sculpture into Box 6
box[6].append(box[0].pop(box[0].index('sculpture')))

# Move the sun from Box 13 to Box 2
box[2].append(box[13].pop(box[13].index('sun')))

# Put the scissors and the cup and the telescope into Box 3
box[3].extend(box[0].pop(box[0].index('scissors')))
box[3].extend(box[0].pop(box[0].index('cup')))
box[3].extend(box[0].pop(box[0].index('telescope')))

# Put the dolphin into Box 9
box[9].append(box[0].pop(box[0].index('dolphin')))

# Swap the vase in Box 4 with the tape in Box 2
box[2].append(box[4].pop(box[4].index('tape')))
box[4].append(box[2].pop(box[2].index('vase')))

# Replace the paint with the star in Box 13
box[13].append(box[13].pop(box[13].index('star')))
box[13].remove('paint')

# Remove the plate from Box 7
box[7].remove('plate')

# Swap the rain in Box 12 with the sun in Box 2
box[2].append(box[12].pop(box[12].index('sun')))
box[12].remove('rain')

# Move the star from Box 13 to Box 11
box[11].append(box[13].pop(box[13].index('star')))

# Move the horse and the magnet from Box 3 to Box 10
box[10].extend(box[3].pop(box[3].index('horse')))
box[10].extend(box[3].pop(box[3].index('magnet')))

# Swap the magnet in Box 10 with the scarf in Box 4
box[4].append(box[10].pop(box[10].index('scarf')))
box[10].append(box[4].pop(box[4].index('magnet')))

# Replace the bowl with the vase in Box 8
box[8].append(box[8].pop(box[8].index('bowl')))
box[8].append(box[4].pop(box[4].index('vase')))

# Remove the horse and the scarf from Box 10
box[10].remove('horse')
box[10].remove('scarf')

# Remove the sun from Box 12
box[12].remove('sun')

# Move the earring and the meteor from Box 5 to Box 4
box[4].extend(box[5].pop(box[5].index('earring')))
box[4].extend(box[5].pop(box[5].index('meteor')))

# Swap the dolphin in Box 9 with the sculpture in Box 6
box[6].append(box[9].pop(box[9].index('dolphin')))
box[9].append(box[6].pop(box[6].index('sculpture')))

# Empty Box 0
box[0] = []

# Replace the vase and the rain with the coat and the freezer in Box 2
box[2].append(box[2].pop(box[2].index('vase')))
box[2].append(box[2].pop(box[2].index('rain')))
box[2].extend(['coat', 'freezer'])

# Put the cow and the beach and the lipstick into Box 0
box[0].extend(['cow', 'beach', 'lipstick'])

# Remove the tape and the doll and the frame from Box 4
box[4].remove('tape')
box[4].remove('doll')
box[4].remove('frame')

# Print the contents of each box
for i in range(14):
    print(f"Box {i}: {box[i]}")
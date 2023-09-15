box = {
    0: [],
    1: ['shorts', 'dice', 'soap'],
    2: ['doll'],
    3: [],
    4: ['toy'],
    5: ['polish', 'snow', 'coin'],
    6: [],
    7: ['fridge', 'umbrella', 'camera', 'plate', 'shoes'],
    8: ['sock', 'boot'],
    9: ['truck', 'speaker'],
    10: []
}

# Remove the toy from Box 4
box[4].remove('toy')

# Put the glasses and the makeup into Box 3
box[3].extend(['glasses', 'makeup'])

# Remove the fridge from Box 7
box[7].remove('fridge')

# Swap the doll in Box 2 with the shorts in Box 1
box[1].remove('shorts')
box[2], box[1] = box[1], box[2]

# Move the dice from Box 1 to Box 7
box[7].append('dice')
box[1].remove('dice')

# Replace the sock with the console in Box 8
box[8].remove('sock')
box[8].append('console')

# Move the polish and the coin from Box 5 to Box 7
box[7].extend(['polish', 'coin'])
box[5].remove('polish')
box[5].remove('coin')

# Empty Box 1
box[1] = []

# Remove the console from Box 8
box[8].remove('console')

# Swap the shorts in Box 2 with the speaker in Box 9
box[2], box[9] = box[9], box[2]

# Remove the speaker from Box 2
box[2].remove('speaker')

# Swap the boot in Box 8 with the glasses in Box 3
box[8], box[3] = box[3], box[8]

# Put the dress into Box 4
box[4].append('dress')

# Put the bird and the makeup into Box 7
box[7].extend(['bird', 'makeup'])

# Move the makeup from Box 3 to Box 0
box[0].append('makeup')
box[3].remove('makeup')

# Move the snow from Box 5 to Box 10
box[10].append('snow')
box[5].remove('snow')

# Move the shorts and the truck from Box 9 to Box 3
box[3].extend(['shorts', 'truck'])
box[9].remove('shorts')
box[9].remove('truck')

# Print the contents of each box
for i in range(11):
    print(f"Box {i}: {box[i]}")
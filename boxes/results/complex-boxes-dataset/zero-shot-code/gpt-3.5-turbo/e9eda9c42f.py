box = {
    0: ['seaweed', 'rock'],
    1: [],
    2: ['game'],
    3: [],
    4: ['ocean', 'octopus'],
    5: ['lock', 'button', 'soap', 'book'],
    6: ['sculpture', 'needle', 'piano'],
    7: ['dog', 'crown'],
    8: ['battery', 'candle'],
    9: ['snow', 'scarf'],
    10: ['fridge']
}

def print_boxes():
    for i in range(11):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Put the laptop and the scarf and the headphone into Box 6
box[6].extend(['laptop', 'scarf', 'headphone'])

# Move the scarf from Box 9 to Box 3
box[3].append(box[9].pop(box[9].index('scarf')))

# Replace the rock and the seaweed with the helmet and the speaker in Box 0
box[0].remove('rock')
box[0].remove('seaweed')
box[0].extend(['helmet', 'speaker'])

# Remove the snow from Box 9
box[9].remove('snow')

# Empty Box 10
box[10] = []

# Put the plate and the card into Box 7
box[7].extend(['plate', 'card'])

# Swap the game in Box 2 with the plate in Box 7
box[2], box[7] = box[7], box[2]

# Remove the octopus from Box 4
box[4].remove('octopus')

# Replace the helmet and the speaker with the bowl and the blender in Box 0
box[0].remove('helmet')
box[0].remove('speaker')
box[0].extend(['bowl', 'blender'])

# Move the battery and the candle from Box 8 to Box 2
box[2].extend(['battery', 'candle'])
box[8] = []

# Put the bear and the coat into Box 5
box[5].extend(['bear', 'coat'])

# Remove the headphone and the scarf from Box 6
box[6].remove('headphone')
box[6].remove('scarf')

# Swap the bowl in Box 0 with the book in Box 5
box[0], box[5] = box[5], box[0]

# Move the book from Box 0 to Box 4
box[4].append(box[0].pop(box[0].index('book')))

# Move the sculpture and the piano from Box 6 to Box 5
box[5].extend(['sculpture', 'piano'])
box[6] = []

# Swap the plate in Box 2 with the book in Box 4
box[2], box[4] = box[4], box[2]

# Swap the dog in Box 7 with the needle in Box 6
box[7], box[6] = box[6], box[7]

print_boxes()
box = {
    0: ['flower', 'shirt'],
    1: ['rain', 'scarf', 'needle', 'comet'],
    2: ['lamp', 'mirror', 'bicycle'],
    3: ['paint', 'shelf'],
    4: ['sun', 'necklace', 'guitar'],
    5: ['meteor'],
    6: ['blanket', 'wig', 'grass'],
    7: ['snow', 'butterfly', 'horse', 'puzzle'],
    8: ['wallet', 'lock', 'coin', 'makeup'],
    9: ['note', 'piano'],
    10: ['perfume', 'chair', 'console', 'sculpture'],
    11: [],
    12: ['horn', 'umbrella'],
    13: ['toaster']
}

def print_box_contents():
    for i in range(14):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Swap the perfume in Box 10 with the shirt in Box 0
box[0], box[10] = box[10], box[0]

# Remove the mirror from Box 2
box[2].remove('mirror')

# Move the toaster from Box 13 to Box 12
box[12].append(box[13].pop())

# Move the flower and the perfume from Box 0 to Box 10
box[10].extend(box[0])
box[0] = []

# Swap the horn in Box 12 with the shelf in Box 3
box[12], box[3] = box[3], box[12]

# Put the tree and the soap into Box 3
box[3].extend(['tree', 'soap'])

# Swap the meteor in Box 5 with the soap in Box 3
box[5], box[3][1] = box[3][1], box[5]

# Replace the piano with the cat in Box 9
box[9] = ['cat']

# Swap the sculpture in Box 10 with the note in Box 9
box[10], box[9] = box[9], box[10]

# Move the sculpture from Box 9 to Box 3
box[3].append(box[9].pop())

# Move the rain and the scarf from Box 1 to Box 6
box[6].extend(box[1][:2])
box[1] = box[1][2:]

# Replace the note with the belt in Box 10
box[10][box[10].index('note')] = 'belt'

# Move the cat from Box 9 to Box 7
box[7].append(box[9].pop())

# Move the puzzle and the cat from Box 7 to Box 5
box[5].extend(box[7][-2:])
box[7] = box[7][:-2]

# Put the bicycle and the tree into Box 11
box[11].extend(['bicycle', 'tree'])

# Move the butterfly and the horse and the snow from Box 7 to Box 11
box[11].extend(box[7][:3])
box[7] = box[7][3:]

# Put the lion and the blanket into Box 7
box[7].extend(['lion', 'blanket'])

# Move the needle and the comet from Box 1 to Box 8
box[8].extend(box[1][:2])
box[1] = box[1][2:]

# Move the horse from Box 11 to Box 13
box[13].append(box[11].pop(box[11].index('horse')))

# Replace the snow and the butterfly and the tree with the flute and the octopus and the controller in Box 11
box[11] = ['flute', 'octopus', 'controller']

# Move the bicycle from Box 2 to Box 3
box[3].append(box[2].pop(box[2].index('bicycle')))

print_box_contents()
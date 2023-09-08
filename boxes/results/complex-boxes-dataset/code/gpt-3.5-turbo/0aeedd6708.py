# Initial state of boxes
boxes = {
    0: ['card', 'motorcycle', 'plane', 'basket'],
    1: ['planet', 'mixer', 'bag', 'plate', 'paint'],
    2: [],
    3: ['needle'],
    4: ['shorts', 'meteor', 'piano'],
    5: ['coin', 'tree'],
    6: ['dolphin', 'fork'],
    7: ['star', 'pillow'],
    8: [],
    9: [],
    10: ['shoe', 'tiger'],
    11: ['glove']
}

# Put the elephant and the vase and the tape into Box 8.
boxes[8].extend(['elephant', 'vase', 'tape'])

# Put the island into Box 8.
boxes[8].append('island')

# Replace the shoe with the phone in Box 10.
boxes[10].remove('shoe')
boxes[10].append('phone')

# Swap the needle in Box 3 with the tape in Box 8.
boxes[3].remove('needle')
boxes[8].remove('tape')
boxes[3].append('tape')
boxes[8].append('needle')

# Replace the shorts and the piano with the bicycle and the train in Box 4.
boxes[4].remove('shorts')
boxes[4].remove('piano')
boxes[4].append('bicycle')
boxes[4].append('train')

# Remove the train and the bicycle and the meteor from Box 4.
items_to_remove = ['train', 'bicycle', 'meteor']
for item in items_to_remove:
    boxes[4].remove(item)

# Put the tape and the forest and the grass into Box 3.
boxes[3].extend(['tape', 'forest', 'grass'])

# Put the dress and the cloud and the wig into Box 10.
boxes[10].extend(['dress', 'cloud', 'wig'])

# Empty Box 11.
boxes[11] = []

# Empty Box 0.
boxes[0] = []

# Move the fork and the dolphin from Box 6 to Box 9.
boxes[6].remove('fork')
boxes[6].remove('dolphin')
boxes[9].extend(['fork', 'dolphin'])

# Move the tree and the coin from Box 5 to Box 3.
boxes[5].remove('tree')
boxes[5].remove('coin')
boxes[3].extend(['tree', 'coin'])

# Swap the bag in Box 1 with the forest in Box 3.
boxes[1].remove('bag')
boxes[3].remove('forest')
boxes[1].append('forest')
boxes[3].append('bag')

# Remove the planet from Box 1.
boxes[1].remove('planet')

# Swap the tiger in Box 10 with the star in Box 7.
boxes[10].remove('tiger')
boxes[7].remove('star')
boxes[10].append('star')
boxes[7].append('tiger')

# Swap the paint in Box 1 with the needle in Box 8.
boxes[1].remove('paint')
boxes[8].remove('needle')
boxes[1].append('needle')
boxes[8].append('paint')

# Move the mixer from Box 1 to Box 9.
boxes[1].remove('mixer')
boxes[9].append('mixer')

# Put the bell and the shelf and the necklace into Box 11.
boxes[11].extend(['bell', 'shelf', 'necklace'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
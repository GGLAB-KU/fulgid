box = {
    0: ['tie', 'note', 'swimsuit', 'drum'],
    1: [],
    2: ['coin'],
    3: ['dolphin', 'polish', 'necklace', 'shoe'],
    4: ['motorcycle', 'seaweed', 'frame', 'beach'],
    5: ['coral', 'bracelet', 'fork'],
    6: ['jungle'],
    7: ['tree', 'paint', 'shoes'],
    8: ['dog', 'grass'],
    9: ['pan', 'grinder', 'cloud'],
    10: ['microwave', 'camera']
}

# Move the necklace and the shoe from Box 3 to Box 7
box[7].extend(box[3].pop(box[3].index('necklace')))
box[7].extend(box[3].pop(box[3].index('shoe')))

# Swap the note in Box 0 with the camera in Box 10
box[0].extend(box[10].pop(box[10].index('camera')))
box[10].extend(box[0].pop(box[0].index('note')))

# Swap the coin in Box 2 with the jungle in Box 6
box[2].extend(box[6].pop(box[6].index('jungle')))
box[6].extend(box[2].pop(box[2].index('coin')))

# Replace the coin with the river in Box 6
box[6].extend(box[6].pop(box[6].index('river')))
box[2].append('coin')

# Replace the drum and the tie and the swimsuit with the towel and the earring and the table in Box 0
box[0].extend(box[0].pop(box[0].index('drum')))
box[0].extend(box[0].pop(box[0].index('tie')))
box[0].extend(box[0].pop(box[0].index('swimsuit')))
box[0].extend(['towel', 'earring', 'table'])

# Replace the dolphin with the river in Box 3
box[3].extend(box[3].pop(box[3].index('dolphin')))
box[3].extend(['river'])

# Swap the dog in Box 8 with the seaweed in Box 4
box[8].extend(box[4].pop(box[4].index('seaweed')))
box[4].extend(box[8].pop(box[8].index('dog')))

# Move the polish from Box 3 to Box 2
box[2].extend(box[3].pop(box[3].index('polish')))

# Remove the shoe and the shoes and the tree from Box 7
box[7].remove('shoe')
box[7].remove('shoes')
box[7].remove('tree')

# Replace the polish with the lightning in Box 2
box[2].extend(box[2].pop(box[2].index('polish')))
box[2].append('lightning')

# Remove the microwave and the note from Box 10
box[10].remove('microwave')
box[10].remove('note')

# Move the river from Box 6 to Box 10
box[10].extend(box[6].pop(box[6].index('river')))

# Put the apple and the frame into Box 9
box[9].extend(['apple', 'frame'])

# Swap the fork in Box 5 with the river in Box 3
box[5].extend(box[3].pop(box[3].index('river')))
box[3].extend(box[5].pop(box[5].index('fork')))

# Move the camera and the towel from Box 0 to Box 8
box[8].extend(box[0].pop(box[0].index('camera')))
box[8].extend(box[0].pop(box[0].index('towel')))

# Remove the seaweed and the grass from Box 8
box[8].remove('seaweed')
box[8].remove('grass')

# Print the contents of each box
for i in range(11):
    print(f"Box {i}: {box[i]}")
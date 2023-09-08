# Initial state of boxes
boxes = {
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

# Move the necklace and the shoe from Box 3 to Box 7.
boxes[3].remove('necklace')
boxes[3].remove('shoe')
boxes[7].append('necklace')
boxes[7].append('shoe')

# Swap the note in Box 0 with the camera in Box 10.
boxes[0].remove('note')
boxes[10].remove('camera')
boxes[0].append('camera')
boxes[10].append('note')

# Swap the coin in Box 2 with the jungle in Box 6.
boxes[2].remove('coin')
boxes[6].remove('jungle')
boxes[2].append('jungle')
boxes[6].append('coin')

# Replace the coin with the river in Box 6.
boxes[6].remove('coin')
boxes[6].append('river')

# Replace the drum and the tie and the swimsuit with the towel and the earring and the table in Box 0.
boxes[0].remove('drum')
boxes[0].remove('tie')
boxes[0].remove('swimsuit')
boxes[0].append('towel')
boxes[0].append('earring')
boxes[0].append('table')

# Replace the dolphin with the river in Box 3.
boxes[3].remove('dolphin')
boxes[3].append('river')

# Swap the dog in Box 8 with the seaweed in Box 4.
boxes[8].remove('dog')
boxes[4].remove('seaweed')
boxes[8].append('seaweed')
boxes[4].append('dog')

# Move the polish from Box 3 to Box 2.
boxes[3].remove('polish')
boxes[2].append('polish')

# Remove the shoe and the shoes and the tree from Box 7.
boxes[7].remove('shoe')
boxes[7].remove('shoes')
boxes[7].remove('tree')

# Replace the polish with the lightning in Box 2.
boxes[2].remove('polish')
boxes[2].append('lightning')

# Remove the microwave and the note from Box 10.
boxes[10].remove('microwave')
boxes[10].remove('note')

# Move the river from Box 6 to Box 10.
boxes[6].remove('river')
boxes[10].append('river')

# Put the apple and the frame into Box 9.
boxes[9].append('apple')
boxes[9].append('frame')

# Swap the fork in Box 5 with the river in Box 3.
boxes[5].remove('fork')
boxes[3].remove('river')
boxes[5].append('river')
boxes[3].append('fork')

# Move the camera and the towel from Box 0 to Box 8.
boxes[0].remove('camera')
boxes[0].remove('towel')
boxes[8].append('camera')
boxes[8].append('towel')

# Remove the seaweed and the grass from Box 8.
boxes[8].remove('seaweed')
boxes[8].remove('grass')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
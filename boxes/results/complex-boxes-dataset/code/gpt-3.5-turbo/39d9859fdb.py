# Initial state of boxes
boxes = {
    0: ['camera'],
    1: ['thunder', 'car', 'dress'],
    2: ['swimsuit', 'flower', 'perfume', 'lipstick'],
    3: ['razor', 'bus'],
    4: ['jacket', 'sock'],
    5: [],
    6: ['glasses', 'tree', 'cup', 'lightning'],
    7: ['bicycle', 'mirror'],
    8: ['bear', 'brush'],
    9: ['flute', 'pillow', 'submarine', 'horn'],
    10: ['branch', 'sun'],
    11: [],
    12: ['planet', 'rocket', 'paint']
}

# Put the controller into Box 9.
boxes[9].append('controller')

# Replace the camera with the fish in Box 0.
boxes[0].remove('camera')
boxes[0].append('fish')

# Move the sock from Box 4 to Box 11.
boxes[4].remove('sock')
boxes[11].append('sock')

# Remove the paint from Box 12.
boxes[12].remove('paint')

# Remove the tree and the lightning from Box 6.
boxes[6].remove('tree')
boxes[6].remove('lightning')

# Move the flower from Box 2 to Box 12.
boxes[2].remove('flower')
boxes[12].append('flower')

# Remove the cup and the glasses from Box 6.
boxes[6].remove('cup')
boxes[6].remove('glasses')

# Move the razor from Box 3 to Box 8.
boxes[3].remove('razor')
boxes[8].append('razor')

# Move the bus from Box 3 to Box 5.
boxes[3].remove('bus')
boxes[5].append('bus')

# Replace the dress and the thunder with the planet and the soap in Box 1.
boxes[1].remove('dress')
boxes[1].remove('thunder')
boxes[1].append('planet')
boxes[1].append('soap')

# Move the bicycle and the mirror from Box 7 to Box 12.
boxes[7].remove('bicycle')
boxes[7].remove('mirror')
boxes[12].append('bicycle')
boxes[12].append('mirror')

# Replace the bicycle and the planet with the motorcycle and the game in Box 12.
boxes[12].remove('bicycle')
boxes[12].remove('planet')
boxes[12].append('motorcycle')
boxes[12].append('game')

# Empty Box 8.
boxes[8] = []

# Replace the bus with the table in Box 5.
boxes[5].remove('bus')
boxes[5].append('table')

# Replace the horn with the shampoo in Box 9.
boxes[9].remove('horn')
boxes[9].append('shampoo')

# Replace the branch with the dress in Box 10.
boxes[10].remove('branch')
boxes[10].append('dress')

# Replace the soap with the bus in Box 1.
boxes[1].remove('soap')
boxes[1].append('bus')

# Swap the jacket in Box 4 with the sock in Box 11.
boxes[4].remove('jacket')
boxes[11].remove('sock')
boxes[4].append('sock')
boxes[11].append('jacket')

# Put the lightning and the thunder and the horn into Box 5.
boxes[5].append('lightning')
boxes[5].append('thunder')
boxes[5].append('horn')

# Remove the fish from Box 0.
boxes[0].remove('fish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: ['dice', 'coat', 'bird', 'controller', 'helmet'],
    1: ['book', 'crown', 'coral', 'keyboard'],
    2: ['vase', 'skirt'],
    3: ['soap'],
    4: ['frame'],
    5: ['table', 'leaf'],
    6: []
}

# Remove the leaf from Box 5.
boxes[5].remove('leaf')

# Remove the keyboard and the coral from Box 1.
boxes[1].remove('keyboard')
boxes[1].remove('coral')

# Replace the skirt and the vase with the blanket and the dice in Box 2.
boxes[2].remove('skirt')
boxes[2].remove('vase')
boxes[2].append('blanket')
boxes[2].append('dice')

# Replace the frame with the scissors in Box 4.
boxes[4].remove('frame')
boxes[4].append('scissors')

# Remove the scissors from Box 4.
boxes[4].remove('scissors')

# Move the soap from Box 3 to Box 6.
boxes[3].remove('soap')
boxes[6].append('soap')

# Replace the bird and the coat and the controller with the oven and the camera and the cloud in Box 0.
boxes[0].remove('bird')
boxes[0].remove('coat')
boxes[0].remove('controller')
boxes[0].append('oven')
boxes[0].append('camera')
boxes[0].append('cloud')

# Replace the soap with the note in Box 6.
boxes[6].remove('soap')
boxes[6].append('note')

# Empty Box 5.
boxes[5] = []

# Move the crown from Box 1 to Box 5.
boxes[1].remove('crown')
boxes[5].append('crown')

# Swap the book in Box 1 with the note in Box 6.
boxes[1].remove('book')
boxes[6].remove('note')
boxes[1].append('note')
boxes[6].append('book')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
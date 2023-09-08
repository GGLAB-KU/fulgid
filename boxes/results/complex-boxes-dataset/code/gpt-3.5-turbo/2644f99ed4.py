# Initial state of boxes
boxes = {
    0: [],
    1: ['camera', 'meteor'],
    2: ['lock'],
    3: [],
    4: ['sandals', 'lion', 'horse'],
    5: ['soap', 'comet', 'microscope'],
    6: ['rain', 'earring', 'shoe', 'piano', 'bag'],
    7: [],
    8: ['ocean'],
    9: ['bowl', 'mask'],
    10: ['pillow']
}

# Remove the lock from Box 2.
boxes[2].remove('lock')

# Replace the earring and the bag with the shoes and the camera in Box 6.
boxes[6].remove('earring')
boxes[6].remove('bag')
boxes[6].append('shoes')
boxes[6].append('camera')

# Move the lion and the horse from Box 4 to Box 5.
boxes[4].remove('lion')
boxes[4].remove('horse')
boxes[5].append('lion')
boxes[5].append('horse')

# Replace the ocean with the battery in Box 8.
boxes[8].remove('ocean')
boxes[8].append('battery')

# Move the sandals from Box 4 to Box 8.
boxes[4].remove('sandals')
boxes[8].append('sandals')

# Swap the lion in Box 5 with the sandals in Box 8.
boxes[5].remove('lion')
boxes[8].remove('sandals')
boxes[5].append('sandals')
boxes[8].append('lion')

# Swap the soap in Box 5 with the camera in Box 1.
boxes[5].remove('soap')
boxes[1].remove('camera')
boxes[5].append('camera')
boxes[1].append('soap')

# Move the bowl from Box 9 to Box 5.
boxes[9].remove('bowl')
boxes[5].append('bowl')

# Move the piano and the shoe from Box 6 to Box 7.
boxes[6].remove('piano')
boxes[6].remove('shoe')
boxes[7].append('piano')
boxes[7].append('shoe')

# Put the cow and the fridge into Box 1.
boxes[1].append('cow')
boxes[1].append('fridge')

# Move the camera from Box 5 to Box 3.
boxes[5].remove('camera')
boxes[3].append('camera')

# Put the plate into Box 2.
boxes[2].append('plate')

# Put the fish and the elephant into Box 1.
boxes[1].append('fish')
boxes[1].append('elephant')

# Replace the cow and the fridge and the fish with the microscope and the cup and the coral in Box 1.
boxes[1].remove('cow')
boxes[1].remove('fridge')
boxes[1].remove('fish')
boxes[1].append('microscope')
boxes[1].append('cup')
boxes[1].append('coral')

# Remove the plate from Box 2.
boxes[2].remove('plate')

# Move the camera from Box 3 to Box 10.
boxes[3].remove('camera')
boxes[10].append('camera')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
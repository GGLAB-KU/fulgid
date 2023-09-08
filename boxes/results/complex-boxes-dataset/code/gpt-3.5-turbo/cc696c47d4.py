# Initial state of boxes
boxes = {
    0: ['bowl', 'seaweed', 'star', 'train', 'makeup'],
    1: ['camera', 'fridge', 'shorts', 'puzzle', 'pan'],
    2: [],
    3: ['note', 'sock', 'controller', 'book', 'table'],
    4: ['pen', 'apple', 'helmet', 'cup'],
    5: ['shoes', 'chair'],
    6: [],
    7: ['bracelet', 'tie', 'rain'],
    8: ['crown'],
    9: ['swimsuit'],
    10: ['branch', 'truck', 'lock'],
    11: ['toy', 'thread', 'sculpture', 'car'],
    12: ['umbrella', 'blender', 'button', 'river', 'gloves'],
    13: []
}

# Put the starfish and the sock and the snow into Box 12.
boxes[12].append('starfish')
boxes[12].append('sock')
boxes[12].append('snow')

# Remove the camera and the pan and the puzzle from Box 1.
boxes[1].remove('camera')
boxes[1].remove('pan')
boxes[1].remove('puzzle')

# Move the crown from Box 8 to Box 0.
boxes[8].remove('crown')
boxes[0].append('crown')

# Remove the snow and the button from Box 12.
boxes[12].remove('snow')
boxes[12].remove('button')

# Remove the cup and the pen from Box 4.
boxes[4].remove('cup')
boxes[4].remove('pen')

# Move the rain and the tie from Box 7 to Box 12.
boxes[7].remove('rain')
boxes[7].remove('tie')
boxes[12].append('rain')
boxes[12].append('tie')

# Swap the chair in Box 5 with the tie in Box 12.
boxes[5].remove('chair')
boxes[12].remove('tie')
boxes[5].append('tie')
boxes[12].append('chair')

# Swap the truck in Box 10 with the note in Box 3.
boxes[10].remove('truck')
boxes[3].remove('note')
boxes[10].append('note')
boxes[3].append('truck')

# Remove the helmet from Box 4.
boxes[4].remove('helmet')

# Put the pan into Box 4.
boxes[4].append('pan')

# Remove the swimsuit from Box 9.
boxes[9].remove('swimsuit')

# Move the sock and the gloves and the starfish from Box 12 to Box 6.
items_to_move = ['sock', 'gloves', 'starfish']
for item in items_to_move:
    boxes[12].remove(item)
    boxes[6].append(item)

# Remove the tie and the shoes from Box 5.
boxes[5].remove('tie')
boxes[5].remove('shoes')

# Move the umbrella from Box 12 to Box 13.
boxes[12].remove('umbrella')
boxes[13].append('umbrella')

# Swap the table in Box 3 with the umbrella in Box 13.
boxes[3].remove('table')
boxes[13].remove('umbrella')
boxes[3].append('umbrella')
boxes[13].append('table')

# Remove the makeup and the train and the star from Box 0.
boxes[0].remove('makeup')
boxes[0].remove('train')
boxes[0].remove('star')

# Remove the sculpture from Box 11.
boxes[11].remove('sculpture')

# Move the table from Box 13 to Box 12.
boxes[13].remove('table')
boxes[12].append('table')

# Remove the sock from Box 6.
boxes[6].remove('sock')

# Replace the apple and the pan with the mirror and the blanket in Box 4.
boxes[4].remove('apple')
boxes[4].remove('pan')
boxes[4].append('mirror')
boxes[4].append('blanket')

# Move the gloves and the starfish from Box 6 to Box 1.
boxes[6].remove('gloves')
boxes[6].remove('starfish')
boxes[1].append('gloves')
boxes[1].append('starfish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
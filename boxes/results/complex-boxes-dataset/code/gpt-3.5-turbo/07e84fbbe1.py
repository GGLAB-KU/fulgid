# Initial state of boxes
boxes = {
    0: ['sandals', 'lipstick', 'pan', 'cat'],
    1: ['ocean', 'elephant', 'laptop', 'meteor'],
    2: ['blanket'],
    3: ['bus', 'tie', 'train'],
    4: ['paint', 'whistle'],
    5: ['makeup', 'lion', 'towel', 'fridge', 'violin'],
    6: ['plane', 'sun', 'bowl'],
    7: [],
    8: ['dice'],
    9: [],
    10: ['razor', 'game', 'horn'],
    11: []
}

# Move the towel from Box 5 to Box 4.
boxes[5].remove('towel')
boxes[4].append('towel')

# Remove the dice from Box 8.
boxes[8].remove('dice')

# Remove the bus and the train and the tie from Box 3.
items_to_remove = ['bus', 'train', 'tie']
for item in items_to_remove:
    boxes[3].remove(item)

# Move the plane from Box 6 to Box 10.
boxes[6].remove('plane')
boxes[10].append('plane')

# Put the skirt and the spoon into Box 8.
boxes[8].append('skirt')
boxes[8].append('spoon')

# Put the towel and the grass into Box 5.
boxes[5].append('towel')
boxes[5].append('grass')

# Replace the cat and the sandals with the needle and the pot in Box 0.
boxes[0].remove('cat')
boxes[0].remove('sandals')
boxes[0].append('needle')
boxes[0].append('pot')

# Move the paint from Box 4 to Box 2.
boxes[4].remove('paint')
boxes[2].append('paint')

# Swap the whistle in Box 4 with the razor in Box 10.
boxes[4].remove('whistle')
boxes[10].remove('razor')
boxes[4].append('razor')
boxes[10].append('whistle')

# Put the thread into Box 0.
boxes[0].append('thread')

# Move the makeup and the towel and the lion from Box 5 to Box 4.
items_to_move = ['makeup', 'towel', 'lion']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Remove the elephant from Box 1.
boxes[1].remove('elephant')

# Swap the spoon in Box 8 with the meteor in Box 1.
boxes[8].remove('spoon')
boxes[1].remove('meteor')
boxes[8].append('meteor')
boxes[1].append('spoon')

# Remove the grass from Box 5.
boxes[5].remove('grass')

# Replace the blanket and the paint with the ring and the button in Box 2.
boxes[2].remove('blanket')
boxes[2].remove('paint')
boxes[2].append('ring')
boxes[2].append('button')

# Empty Box 10.
boxes[10] = []

# Remove the bowl and the sun from Box 6.
boxes[6].remove('bowl')
boxes[6].remove('sun')

# Move the skirt from Box 8 to Box 9.
boxes[8].remove('skirt')
boxes[9].append('skirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
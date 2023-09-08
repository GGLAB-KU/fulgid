# Initial state of boxes
boxes = {
    0: ['plane'],
    1: ['dress'],
    2: ['razor', 'oven', 'tiger', 'glasses'],
    3: ['bracelet'],
    4: [],
    5: ['horse', 'necklace', 'ship']
}

# Replace the bracelet with the sun in Box 3.
boxes[3].remove('bracelet')
boxes[3].append('sun')

# Move the sun from Box 3 to Box 4.
boxes[3].remove('sun')
boxes[4].append('sun')

# Replace the tiger and the razor and the oven with the umbrella and the ocean and the shoes in Box 2.
boxes[2].remove('tiger')
boxes[2].remove('razor')
boxes[2].remove('oven')
boxes[2].append('umbrella')
boxes[2].append('ocean')
boxes[2].append('shoes')

# Replace the sun with the clock in Box 4.
boxes[4].remove('sun')
boxes[4].append('clock')

# Replace the dress with the umbrella in Box 1.
boxes[1].remove('dress')
boxes[1].append('umbrella')

# Put the rocket and the tape into Box 5.
boxes[5].append('rocket')
boxes[5].append('tape')

# Move the plane from Box 0 to Box 1.
boxes[0].remove('plane')
boxes[1].append('plane')

# Replace the ocean and the umbrella and the shoes with the lock and the blanket and the bag in Box 2.
boxes[2].remove('ocean')
boxes[2].remove('umbrella')
boxes[2].remove('shoes')
boxes[2].append('lock')
boxes[2].append('blanket')
boxes[2].append('bag')

# Put the guitar and the swimsuit into Box 3.
boxes[3].append('guitar')
boxes[3].append('swimsuit')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
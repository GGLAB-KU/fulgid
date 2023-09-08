# Initial state of boxes
boxes = {
    0: ['hat', 'card'],
    1: ['button', 'seaweed', 'oven', 'table', 'river'],
    2: [],
    3: ['candle'],
    4: ['rock']
}

# Put the cat into Box 1.
boxes[1].append('cat')

# Put the bird and the planet and the moon into Box 3.
boxes[3].extend(['bird', 'planet', 'moon'])

# Empty Box 1.
boxes[1] = []

# Put the table into Box 4.
boxes[4].append('table')

# Move the table and the rock from Box 4 to Box 0.
items_to_move = ['table', 'rock']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Put the wire and the zipper into Box 2.
boxes[2].extend(['wire', 'zipper'])

# Swap the hat in Box 0 with the planet in Box 3.
boxes[0].remove('hat')
boxes[3].remove('planet')
boxes[0].append('planet')
boxes[3].append('hat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: ['chair', 'helmet', 'necklace', 'toy'],
    1: ['battery', 'boot'],
    2: [],
    3: ['spoon', 'star', 'keyboard', 'shorts', 'console'],
    4: ['plate']
}

# Remove the boot and the battery from Box 1.
boxes[1].remove('boot')
boxes[1].remove('battery')

# Replace the chair and the helmet with the lion and the forest in Box 0.
boxes[0].remove('chair')
boxes[0].remove('helmet')
boxes[0].append('lion')
boxes[0].append('forest')

# Remove the plate from Box 4.
boxes[4].remove('plate')

# Put the cup into Box 2.
boxes[2].append('cup')

# Move the keyboard and the console from Box 3 to Box 2.
items_to_move = ['keyboard', 'console']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[2].append(item)

# Move the forest and the necklace from Box 0 to Box 4.
items_to_move = ['forest', 'necklace']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Swap the toy in Box 0 with the keyboard in Box 2.
boxes[0].remove('toy')
boxes[2].remove('keyboard')
boxes[0].append('keyboard')
boxes[2].append('toy')

# Remove the keyboard and the lion from Box 0.
boxes[0].remove('keyboard')
boxes[0].remove('lion')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
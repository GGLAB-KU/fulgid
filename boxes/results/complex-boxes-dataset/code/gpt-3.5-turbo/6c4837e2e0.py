# Initial state of boxes
boxes = {
    0: ['flower'],
    1: ['meteor'],
    2: ['needle', 'freezer', 'lipstick', 'octopus', 'glove'],
    3: ['charger', 'table', 'comet'],
    4: ['fork'],
    5: ['camera', 'bracelet', 'car'],
    6: ['laptop']
}

# Move the meteor from Box 1 to Box 2.
boxes[1].remove('meteor')
boxes[2].append('meteor')

# Remove the meteor and the freezer and the lipstick from Box 2.
items_to_remove = ['meteor', 'freezer', 'lipstick']
for item in items_to_remove:
    boxes[2].remove(item)

# Replace the fork with the puzzle in Box 4.
boxes[4].remove('fork')
boxes[4].append('puzzle')

# Swap the camera in Box 5 with the table in Box 3.
boxes[5].remove('camera')
boxes[3].remove('table')
boxes[5].append('table')
boxes[3].append('camera')

# Move the flower from Box 0 to Box 1.
boxes[0].remove('flower')
boxes[1].append('flower')

# Put the shampoo into Box 2.
boxes[2].append('shampoo')

# Swap the glove in Box 2 with the flower in Box 1.
boxes[2].remove('glove')
boxes[1].remove('flower')
boxes[2].append('flower')
boxes[1].append('glove')

# Replace the glove with the skirt in Box 1.
boxes[1].remove('glove')
boxes[1].append('skirt')

# Move the charger and the comet from Box 3 to Box 0.
boxes[3].remove('charger')
boxes[3].remove('comet')
boxes[0].append('charger')
boxes[0].append('comet')

# Put the desert into Box 2.
boxes[2].append('desert')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
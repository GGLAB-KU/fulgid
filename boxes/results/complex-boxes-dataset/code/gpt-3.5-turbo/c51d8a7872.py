# Initial state of boxes
boxes = {
    0: ['crown', 'flute', 'bear', 'makeup', 'sculpture'],
    1: [],
    2: ['button', 'gloves'],
    3: ['drum', 'lightning', 'oven', 'magnet'],
    4: [],
    5: [],
    6: ['table', 'plane'],
    7: ['elephant', 'microwave'],
    8: ['violin', 'blender', 'glove', 'dolphin'],
    9: ['mixer', 'tiger'],
    10: ['umbrella', 'river', 'butterfly', 'seaweed'],
    11: ['note', 'mountain', 'rocket', 'card', 'zipper'],
    12: ['toothbrush', 'moon'],
    13: ['bird', 'shelf', 'shoe', 'jacket', 'shampoo']
}

# Replace the plane with the river in Box 6.
boxes[6].remove('plane')
boxes[6].append('river')

# Remove the table and the river from Box 6.
boxes[6].remove('table')
boxes[6].remove('river')

# Remove the shelf and the bird and the shampoo from Box 13.
items_to_remove = ['shelf', 'bird', 'shampoo']
for item in items_to_remove:
    boxes[13].remove(item)

# Move the note and the mountain from Box 11 to Box 1.
items_to_move = ['note', 'mountain']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[1].append(item)

# Swap the glove in Box 8 with the moon in Box 12.
boxes[8].remove('glove')
boxes[12].remove('moon')
boxes[8].append('moon')
boxes[12].append('glove')

# Replace the button and the gloves with the rock and the pen in Box 2.
boxes[2].remove('button')
boxes[2].remove('gloves')
boxes[2].append('rock')
boxes[2].append('pen')

# Empty Box 3.
boxes[3] = []

# Remove the seaweed and the umbrella and the river from Box 10.
items_to_remove = ['seaweed', 'umbrella', 'river']
for item in items_to_remove:
    boxes[10].remove(item)

# Remove the toothbrush and the glove from Box 12.
boxes[12].remove('toothbrush')
boxes[12].remove('glove')

# Put the zipper and the cloud and the dice into Box 3.
items_to_put = ['zipper', 'cloud', 'dice']
for item in items_to_put:
    boxes[3].append(item)

# Put the leaf and the belt and the frame into Box 11.
items_to_put = ['leaf', 'belt', 'frame']
for item in items_to_put:
    boxes[11].append(item)

# Move the dice and the zipper and the cloud from Box 3 to Box 6.
items_to_move = ['dice', 'zipper', 'cloud']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[6].append(item)

# Remove the jacket and the shoe from Box 13.
items_to_remove = ['jacket', 'shoe']
for item in items_to_remove:
    boxes[13].remove(item)

# Put the planet into Box 1.
boxes[1].append('planet')

# Move the violin and the dolphin from Box 8 to Box 9.
items_to_move = ['violin', 'dolphin']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[9].append(item)

# Put the beach and the storm and the pot into Box 2.
items_to_put = ['beach', 'storm', 'pot']
for item in items_to_put:
    boxes[2].append(item)

# Remove the butterfly from Box 10.
boxes[10].remove('butterfly')

# Replace the mixer with the shelf in Box 9.
boxes[9].remove('mixer')
boxes[9].append('shelf')

# Remove the note and the mountain and the planet from Box 1.
items_to_remove = ['note', 'mountain', 'planet']
for item in items_to_remove:
    boxes[1].remove(item)

# Remove the blender and the moon from Box 8.
boxes[8].remove('blender')
boxes[8].remove('moon')

# Swap the sculpture in Box 0 with the tiger in Box 9.
boxes[0].remove('sculpture')
boxes[9].remove('tiger')
boxes[0].append('tiger')
boxes[9].append('sculpture')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
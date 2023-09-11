# Initial state of boxes
boxes = {
    0: ['shoe', 'river', 'cat', 'flute'],
    1: ['vase', 'beach', 'truck', 'wig', 'mixer'],
    2: [],
    3: ['flower', 'scissors', 'camera', 'coat'],
    4: ['zipper', 'doll', 'dog', 'microscope'],
    5: [],
    6: []
}

# Put the laptop and the pen and the beach into Box 4.
items_to_put = ['laptop', 'pen', 'beach']
for item in items_to_put:
    boxes[4].append(item)

# Empty Box 3.
boxes[3] = []

# Put the motorcycle and the sandals into Box 0.
items_to_put = ['motorcycle', 'sandals']
for item in items_to_put:
    boxes[0].append(item)

# Put the mixer and the bird and the note into Box 0.
items_to_put = ['mixer', 'bird', 'note']
for item in items_to_put:
    boxes[0].append(item)

# Remove the flute from Box 0.
boxes[0].remove('flute')

# Put the lipstick and the rock into Box 1.
items_to_put = ['lipstick', 'rock']
for item in items_to_put:
    boxes[1].append(item)

# Remove the zipper and the pen from Box 4.
boxes[4].remove('zipper')
boxes[4].remove('pen')

# Replace the mixer and the wig with the flute and the keyboard in Box 1.
boxes[1].remove('mixer')
boxes[1].remove('wig')
boxes[1].append('flute')
boxes[1].append('keyboard')

# Replace the shoe with the clock in Box 0.
boxes[0].remove('shoe')
boxes[0].append('clock')

# Replace the river with the plate in Box 0.
boxes[0].remove('river')
boxes[0].append('plate')

# Remove the mixer and the cat and the note from Box 0.
items_to_remove = ['mixer', 'cat', 'note']
for item in items_to_remove:
    boxes[0].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
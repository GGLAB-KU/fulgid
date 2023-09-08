# Initial state of boxes
boxes = {
    0: ['dog', 'needle'],
    1: [],
    2: ['plate', 'wire'],
    3: ['truck', 'microwave', 'paint'],
    4: ['river', 'bicycle'],
    5: ['pants', 'octopus']
}

# Swap the dog in Box 0 with the wire in Box 2.
boxes[0].remove('dog')
boxes[2].remove('wire')
boxes[0].append('wire')
boxes[2].append('dog')

# Move the paint and the truck from Box 3 to Box 0.
items_to_move = ['paint', 'truck']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Replace the bicycle and the river with the frame and the bird in Box 4.
boxes[4].remove('river')
boxes[4].remove('bicycle')
boxes[4].append('frame')
boxes[4].append('bird')

# Remove the plate and the dog from Box 2.
boxes[2].remove('plate')
boxes[2].remove('dog')

# Swap the frame in Box 4 with the pants in Box 5.
boxes[4].remove('frame')
boxes[5].remove('pants')
boxes[4].append('pants')
boxes[5].append('frame')

# Put the headphone into Box 3.
boxes[3].append('headphone')

# Replace the octopus with the towel in Box 5.
boxes[5].remove('octopus')
boxes[5].append('towel')

# Move the bird and the pants from Box 4 to Box 3.
items_to_move = ['bird', 'pants']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Replace the needle with the cup in Box 0.
boxes[0].remove('needle')
boxes[0].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
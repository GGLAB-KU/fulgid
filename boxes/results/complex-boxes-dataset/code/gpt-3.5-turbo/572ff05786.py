# Initial state of boxes
boxes = {
    0: ['cloud', 'bicycle', 'umbrella'],
    1: ['comet', 'chair', 'pillow', 'speaker'],
    2: ['coat', 'shoes'],
    3: ['dress', 'storm', 'bag'],
    4: ['lock', 'sandals', 'note']
}

# Remove the umbrella and the cloud and the bicycle from Box 0.
items_to_remove = ['umbrella', 'cloud', 'bicycle']
for item in items_to_remove:
    boxes[0].remove(item)

# Swap the bag in Box 3 with the coat in Box 2.
boxes[2].remove('coat')
boxes[3].remove('bag')
boxes[2].append('bag')
boxes[3].append('coat')

# Put the plane and the scarf into Box 4.
boxes[4].append('plane')
boxes[4].append('scarf')

# Move the scarf and the lock from Box 4 to Box 3.
boxes[4].remove('scarf')
boxes[4].remove('lock')
boxes[3].append('scarf')
boxes[3].append('lock')

# Replace the sandals and the note with the coat and the vase in Box 4.
boxes[4].remove('sandals')
boxes[4].remove('note')
boxes[4].append('coat')
boxes[4].append('vase')

# Remove the vase and the coat from Box 4.
boxes[4].remove('vase')
boxes[4].remove('coat')

# Replace the plane with the gloves in Box 4.
boxes[4].remove('plane')
boxes[4].append('gloves')

# Put the elephant and the game into Box 0.
boxes[0].append('elephant')
boxes[0].append('game')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
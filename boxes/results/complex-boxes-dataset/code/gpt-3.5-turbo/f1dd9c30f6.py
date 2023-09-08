# Initial state of boxes
boxes = {
    0: ['plate', 'truck', 'wig'],
    1: ['tape', 'microwave', 'key', 'ring', 'cup'],
    2: [],
    3: ['ocean'],
    4: ['rain', 'toothpaste', 'bicycle', 'cow'],
    5: ['book', 'lipstick', 'whistle', 'coral'],
    6: ['fork', 'starfish', 'bird', 'violin', 'planet'],
    7: [],
    8: ['thread'],
    9: ['magnet', 'jacket', 'towel'],
    10: ['tiger', 'seaweed']
}

# Replace the fork and the starfish and the violin with the toaster and the forest and the dress in Box 6.
boxes[6].remove('fork')
boxes[6].remove('starfish')
boxes[6].remove('violin')
boxes[6].append('toaster')
boxes[6].append('forest')
boxes[6].append('dress')

# Move the plate from Box 0 to Box 5.
boxes[0].remove('plate')
boxes[5].append('plate')

# Put the shoes into Box 5.
boxes[5].append('shoes')

# Put the scissors and the sun and the bird into Box 9.
boxes[9].append('scissors')
boxes[9].append('sun')
boxes[9].append('bird')

# Remove the truck and the wig from Box 0.
boxes[0].remove('truck')
boxes[0].remove('wig')

# Move the seaweed from Box 10 to Box 9.
boxes[10].remove('seaweed')
boxes[9].append('seaweed')

# Put the leaf and the rocket and the sock into Box 8.
boxes[8].append('leaf')
boxes[8].append('rocket')
boxes[8].append('sock')

# Swap the shoes in Box 5 with the tiger in Box 10.
boxes[5].remove('shoes')
boxes[10].remove('tiger')
boxes[5].append('tiger')
boxes[10].append('shoes')

# Replace the cup and the key with the gloves and the tape in Box 1.
boxes[1].remove('cup')
boxes[1].remove('key')
boxes[1].append('gloves')
boxes[1].append('tape')

# Remove the microwave and the gloves from Box 1.
boxes[1].remove('microwave')
boxes[1].remove('gloves')

# Remove the tape from Box 1.
boxes[1].remove('tape')

# Empty Box 10.
boxes[10] = []

# Swap the toaster in Box 6 with the ocean in Box 3.
boxes[6].remove('toaster')
boxes[3].remove('ocean')
boxes[6].append('ocean')
boxes[3].append('toaster')

# Put the brush and the coin and the seaweed into Box 5.
boxes[5].append('brush')
boxes[5].append('coin')
boxes[5].append('seaweed')

# Move the book from Box 5 to Box 1.
boxes[5].remove('book')
boxes[1].append('book')

# Remove the rain and the toothpaste and the cow from Box 4.
boxes[4].remove('rain')
boxes[4].remove('toothpaste')
boxes[4].remove('cow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
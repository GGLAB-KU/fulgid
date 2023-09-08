# Initial state of boxes
boxes = {
    0: [],
    1: ['elephant', 'apple'],
    2: ['perfume'],
    3: ['submarine'],
    4: ['rock'],
    5: ['comb', 'pen'],
    6: ['needle', 'oven', 'seaweed', 'harmonica', 'moon'],
    7: ['cup', 'spoon', 'scarf', 'pot', 'wire'],
    8: ['plate', 'coin', 'wig', 'button']
}

# Empty Box 5
boxes[5] = []

# Swap the perfume in Box 2 with the elephant in Box 1.
boxes[1].remove('elephant')
boxes[2].remove('perfume')
boxes[1].append('perfume')
boxes[2].append('elephant')

# Replace the oven and the harmonica and the seaweed with the bag and the makeup and the clock in Box 6.
boxes[6].remove('oven')
boxes[6].remove('harmonica')
boxes[6].remove('seaweed')
boxes[6].append('bag')
boxes[6].append('makeup')
boxes[6].append('clock')

# Put the umbrella into Box 5.
boxes[5].append('umbrella')

# Remove the cup from Box 7.
boxes[7].remove('cup')

# Replace the makeup with the dog in Box 6.
boxes[6].remove('makeup')
boxes[6].append('dog')

# Replace the coin and the wig with the toaster and the key in Box 8.
boxes[8].remove('coin')
boxes[8].remove('wig')
boxes[8].append('toaster')
boxes[8].append('key')

# Put the cup into Box 1.
boxes[1].append('cup')

# Remove the rock from Box 4.
boxes[4].remove('rock')

# Move the submarine from Box 3 to Box 0.
boxes[0].append('submarine')
boxes[3].remove('submarine')

# Empty Box 7.
boxes[7] = []

# Move the elephant from Box 2 to Box 6.
boxes[6].append('elephant')
boxes[2].remove('elephant')

# Move the key and the plate and the toaster from Box 8 to Box 2.
items_to_move = ['key', 'plate', 'toaster']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
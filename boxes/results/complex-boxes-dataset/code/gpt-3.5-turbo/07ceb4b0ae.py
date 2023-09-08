# Initial state of boxes
boxes = {
    0: ['dog', 'fish', 'shelf'],
    1: ['shark', 'branch', 'sun'],
    2: ['truck', 'piano', 'chair'],
    3: [],
    4: ['bowl'],
    5: ['island', 'storm', 'basket', 'mirror'],
    6: ['dice', 'spoon', 'sock'],
    7: [],
    8: ['polish'],
    9: []
}

# Swap the sock in Box 6 with the piano in Box 2.
boxes[6].remove('sock')
boxes[2].remove('piano')
boxes[6].append('piano')
boxes[2].append('sock')

# Replace the polish with the frame in Box 8.
boxes[8].remove('polish')
boxes[8].append('frame')

# Replace the bowl with the fork in Box 4.
boxes[4].remove('bowl')
boxes[4].append('fork')

# Move the sock and the truck from Box 2 to Box 6.
items_to_move = ['sock', 'truck']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Put the lightning and the coral into Box 6.
boxes[6].append('lightning')
boxes[6].append('coral')

# Put the cat into Box 4.
boxes[4].append('cat')

# Remove the fish and the shelf from Box 0.
boxes[0].remove('fish')
boxes[0].remove('shelf')

# Remove the truck and the sock from Box 6.
boxes[6].remove('truck')
boxes[6].remove('sock')

# Remove the storm and the mirror from Box 5.
boxes[5].remove('storm')
boxes[5].remove('mirror')

# Replace the dog with the sun in Box 0.
boxes[0].remove('dog')
boxes[0].append('sun')

# Remove the sun and the shark from Box 1.
boxes[1].remove('sun')
boxes[1].remove('shark')

# Move the frame from Box 8 to Box 6.
boxes[8].remove('frame')
boxes[6].append('frame')

# Replace the sun with the umbrella in Box 0.
boxes[0].remove('sun')
boxes[0].append('umbrella')

# Remove the fork from Box 4.
boxes[4].remove('fork')

# Move the umbrella from Box 0 to Box 3.
boxes[0].remove('umbrella')
boxes[3].append('umbrella')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
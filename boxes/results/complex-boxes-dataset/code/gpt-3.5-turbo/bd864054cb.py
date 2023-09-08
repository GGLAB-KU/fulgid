# Initial state of boxes
boxes = {
    0: ['scarf', 'shampoo'],
    1: [],
    2: [],
    3: ['comet', 'shorts', 'blender'],
    4: ['rain', 'bracelet'],
    5: ['boot', 'microscope', 'bag', 'puzzle', 'coat'],
    6: ['vase', 'lightning', 'fish'],
    7: ['polish', 'toaster', 'tie', 'chair', 'laptop'],
    8: ['wallet', 'clock']
}

# Put the thread into Box 1.
boxes[1].append('thread')

# Swap the puzzle in Box 5 with the clock in Box 8.
boxes[5].remove('puzzle')
boxes[8].remove('clock')
boxes[5].append('clock')
boxes[8].append('puzzle')

# Remove the scarf and the shampoo from Box 0.
boxes[0].remove('scarf')
boxes[0].remove('shampoo')

# Swap the fish in Box 6 with the wallet in Box 8.
boxes[6].remove('fish')
boxes[8].remove('wallet')
boxes[6].append('wallet')
boxes[8].append('fish')

# Move the lightning and the wallet from Box 6 to Box 1.
boxes[6].remove('lightning')
boxes[6].remove('wallet')
boxes[1].append('lightning')
boxes[1].append('wallet')

# Move the puzzle from Box 8 to Box 0.
boxes[8].remove('puzzle')
boxes[0].append('puzzle')

# Swap the comet in Box 3 with the rain in Box 4.
boxes[3].remove('comet')
boxes[4].remove('rain')
boxes[3].append('rain')
boxes[4].append('comet')

# Replace the puzzle with the oven in Box 0.
boxes[0].remove('puzzle')
boxes[0].append('oven')

# Move the toaster and the laptop and the tie from Box 7 to Box 3.
items_to_move = ['toaster', 'laptop', 'tie']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[3].append(item)

# Move the comet from Box 4 to Box 3.
boxes[4].remove('comet')
boxes[3].append('comet')

# Put the polish into Box 5.
boxes[5].append('polish')

# Swap the fish in Box 8 with the shorts in Box 3.
boxes[8].remove('fish')
boxes[3].remove('shorts')
boxes[8].append('shorts')
boxes[3].append('fish')

# Swap the oven in Box 0 with the tie in Box 3.
boxes[0].remove('oven')
boxes[3].remove('tie')
boxes[0].append('tie')
boxes[3].append('oven')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
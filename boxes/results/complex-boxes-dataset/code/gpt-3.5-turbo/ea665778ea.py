# Initial state of boxes
boxes = {
    0: ['mask', 'shelf', 'lightning', 'thread'],
    1: ['jacket', 'coat', 'pen'],
    2: ['apple', 'hat', 'wire'],
    3: ['shark', 'headphone', 'dolphin'],
    4: ['coral'],
    5: ['island', 'tiger', 'usb', 'whistle', 'clock'],
    6: ['bracelet'],
    7: ['boot', 'octopus'],
    8: ['plane', 'bird']
}

# Remove the bird from Box 8.
boxes[8].remove('bird')

# Remove the thread and the lightning from Box 0.
boxes[0].remove('thread')
boxes[0].remove('lightning')

# Replace the shark with the mountain in Box 3.
boxes[3].remove('shark')
boxes[3].append('mountain')

# Swap the tiger in Box 5 with the coral in Box 4.
boxes[5].remove('tiger')
boxes[4].remove('coral')
boxes[5].append('coral')
boxes[4].append('tiger')

# Swap the boot in Box 7 with the shelf in Box 0.
boxes[7].remove('boot')
boxes[0].remove('shelf')
boxes[7].append('shelf')
boxes[0].append('boot')

# Empty Box 4.
boxes[4] = []

# Move the hat and the apple from Box 2 to Box 8.
items_to_move = ['hat', 'apple']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[8].append(item)

# Replace the mountain and the headphone and the dolphin with the cat and the console and the boat in Box 3.
boxes[3].remove('mountain')
boxes[3].remove('headphone')
boxes[3].remove('dolphin')
boxes[3].append('cat')
boxes[3].append('console')
boxes[3].append('boat')

# Swap the jacket in Box 1 with the octopus in Box 7.
boxes[1].remove('jacket')
boxes[7].remove('octopus')
boxes[1].append('octopus')
boxes[7].append('jacket')

# Replace the pen and the octopus with the piano and the magnet in Box 1.
boxes[1].remove('pen')
boxes[7].remove('octopus')
boxes[1].append('piano')
boxes[7].append('magnet')

# Empty Box 2.
boxes[2] = []

# Swap the coat in Box 1 with the boot in Box 0.
boxes[1].remove('coat')
boxes[0].remove('boot')
boxes[1].append('boot')
boxes[0].append('coat')

# Empty Box 5.
boxes[5] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
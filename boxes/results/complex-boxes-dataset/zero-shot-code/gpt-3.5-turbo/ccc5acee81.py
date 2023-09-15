boxes = {
    0: ['bear', 'rain'],
    1: ['shampoo', 'planet', 'needle', 'usb', 'dice'],
    2: ['vase'],
    3: ['tiger', 'frame', 'charger', 'dolphin'],
    4: [],
    5: ['seaweed'],
    6: []
}

def print_boxes():
    for box, items in boxes.items():
        print(f"Box {box}: {items}")

# Empty Box 0
boxes[0] = []

# Put the zipper and the dolphin and the book into Box 1
boxes[1].extend(['zipper', 'dolphin', 'book'])

# Put the bicycle and the moon into Box 3
boxes[3].extend(['bicycle', 'moon'])

# Empty Box 5
boxes[5] = []

# Put the fish and the drum into Box 6
boxes[6].extend(['fish', 'drum'])

# Put the comet into Box 6
boxes[6].append('comet')

# Put the phone into Box 6
boxes[6].append('phone')

# Swap the planet in Box 1 with the vase in Box 2
boxes[1].remove('planet')
boxes[2].remove('vase')
boxes[1].append('vase')
boxes[2].append('planet')

# Swap the planet in Box 2 with the drum in Box 6
boxes[2].remove('planet')
boxes[6].remove('drum')
boxes[2].append('drum')
boxes[6].append('planet')

# Swap the frame in Box 3 with the drum in Box 2
boxes[3].remove('frame')
boxes[2].remove('drum')
boxes[3].append('drum')
boxes[2].append('frame')

# Print the final state of the boxes
print_boxes()
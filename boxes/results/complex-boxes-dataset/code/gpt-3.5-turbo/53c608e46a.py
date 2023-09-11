# Initial state of boxes
boxes = {
    0: ['planet', 'guitar', 'tie'],
    1: ['harmonica', 'charger', 'whistle'],
    2: ['shampoo'],
    3: ['toaster', 'wig'],
    4: ['polish']
}

# Empty Box 4
boxes[4] = []

# Replace the shampoo with the boot in Box 2
boxes[2].remove('shampoo')
boxes[2].append('boot')

# Put the dolphin and the usb into Box 0
boxes[0].append('dolphin')
boxes[0].append('usb')

# Put the whistle into Box 1
boxes[1].append('whistle')

# Move the boot from Box 2 to Box 1
boxes[2].remove('boot')
boxes[1].append('boot')

# Swap the dolphin in Box 0 with the harmonica in Box 1
boxes[0].remove('dolphin')
boxes[1].remove('harmonica')
boxes[0].append('harmonica')
boxes[1].append('dolphin')

# Replace the harmonica with the spoon in Box 0
boxes[0].remove('harmonica')
boxes[0].append('spoon')

# Move the guitar and the usb from Box 0 to Box 4
boxes[0].remove('guitar')
boxes[0].remove('usb')
boxes[4].append('guitar')
boxes[4].append('usb')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
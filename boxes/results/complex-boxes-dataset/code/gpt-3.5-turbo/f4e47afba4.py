# Initial state of boxes
boxes = {
    0: [],
    1: ['harmonica'],
    2: ['belt', 'clock', 'bicycle', 'speaker'],
    3: ['lamp', 'watch', 'toaster', 'shelf'],
    4: ['comb', 'crown', 'sculpture', 'branch', 'coral'],
    5: ['soap', 'pot', 'tape', 'apple'],
    6: ['doll', 'tree', 'dress', 'shirt'],
    7: ['truck', 'usb', 'pants', 'motorcycle'],
    8: ['frame', 'umbrella', 'lightning', 'table'],
    9: ['guitar', 'pillow', 'island', 'controller'],
    10: ['bag', 'spoon', 'puzzle', 'glove', 'lipstick'],
    11: [],
    12: ['note']
}

# Swap the controller in Box 9 with the bicycle in Box 2.
boxes[2].remove('bicycle')
boxes[9].remove('controller')
boxes[2].append('controller')
boxes[9].append('bicycle')

# Remove the toaster and the watch and the shelf from Box 3.
items_to_remove = ['toaster', 'watch', 'shelf']
for item in items_to_remove:
    boxes[3].remove(item)

# Remove the clock from Box 2.
boxes[2].remove('clock')

# Swap the note in Box 12 with the umbrella in Box 8.
boxes[8].remove('umbrella')
boxes[12].remove('note')
boxes[8].append('note')
boxes[12].append('umbrella')

# Replace the truck with the belt in Box 7.
boxes[7].remove('truck')
boxes[7].append('belt')

# Swap the table in Box 8 with the spoon in Box 10.
boxes[8].remove('table')
boxes[10].remove('spoon')
boxes[8].append('spoon')
boxes[10].append('table')

# Swap the harmonica in Box 1 with the note in Box 8.
boxes[1].remove('harmonica')
boxes[8].remove('note')
boxes[1].append('note')
boxes[8].append('harmonica')

# Move the pants and the usb and the belt from Box 7 to Box 2.
items_to_move = ['pants', 'usb', 'belt']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[2].append(item)

# Replace the umbrella with the cat in Box 12.
boxes[12].remove('umbrella')
boxes[12].append('cat')

# Replace the coral and the branch and the sculpture with the dolphin and the gloves and the sun in Box 4.
boxes[4].remove('coral')
boxes[4].remove('branch')
boxes[4].remove('sculpture')
boxes[4].append('dolphin')
boxes[4].append('gloves')
boxes[4].append('sun')

# Put the violin and the battery and the usb into Box 7.
items_to_put = ['violin', 'battery', 'usb']
for item in items_to_put:
    boxes[7].append(item)

# Move the guitar from Box 9 to Box 4.
boxes[9].remove('guitar')
boxes[4].append('guitar')

# Put the shark and the pillow into Box 2.
boxes[2].append('shark')
boxes[2].append('pillow')

# Swap the violin in Box 7 with the tape in Box 5.
boxes[7].remove('violin')
boxes[5].remove('tape')
boxes[7].append('tape')
boxes[5].append('violin')

# Swap the lamp in Box 3 with the cat in Box 12.
boxes[3].remove('lamp')
boxes[12].remove('cat')
boxes[3].append('cat')
boxes[12].append('lamp')

# Replace the controller and the belt with the dog and the phone in Box 2.
boxes[2].remove('controller')
boxes[2].remove('belt')
boxes[2].append('dog')
boxes[2].append('phone')

# Put the pen into Box 10.
boxes[10].append('pen')

# Move the cat from Box 3 to Box 2.
boxes[3].remove('cat')
boxes[2].append('cat')

# Put the mountain into Box 4.
boxes[4].append('mountain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
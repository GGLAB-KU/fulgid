# Initial state of boxes
boxes = {
    0: ['paint', 'planet', 'lightning', 'toy', 'gloves'],
    1: ['shirt', 'toothbrush'],
    2: ['frame'],
    3: ['phone', 'skirt'],
    4: [],
    5: ['doll', 'moon', 'elephant'],
    6: ['table', 'pot', 'pan', 'shelf', 'vase']
}

# Remove the toothbrush from Box 1.
boxes[1].remove('toothbrush')

# Replace the paint and the planet with the microscope and the speaker in Box 0.
boxes[0].remove('paint')
boxes[0].remove('planet')
boxes[0].append('microscope')
boxes[0].append('speaker')

# Replace the frame with the flower in Box 2.
boxes[2].remove('frame')
boxes[2].append('flower')

# Swap the toy in Box 0 with the shirt in Box 1.
boxes[0].remove('toy')
boxes[1].remove('shirt')
boxes[0].append('shirt')
boxes[1].append('toy')

# Move the moon and the elephant and the doll from Box 5 to Box 3.
items_to_move = ['moon', 'elephant', 'doll']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Swap the speaker in Box 0 with the toy in Box 1.
boxes[0].remove('speaker')
boxes[1].remove('toy')
boxes[0].append('toy')
boxes[1].append('speaker')

# Put the controller into Box 1.
boxes[1].append('controller')

# Put the usb into Box 0.
boxes[0].append('usb')

# Swap the table in Box 6 with the usb in Box 0.
boxes[6].remove('table')
boxes[0].remove('usb')
boxes[6].append('usb')
boxes[0].append('table')

# Put the bear into Box 6.
boxes[6].append('bear')

# Swap the bear in Box 6 with the moon in Box 3.
boxes[6].remove('bear')
boxes[3].remove('moon')
boxes[6].append('moon')
boxes[3].append('bear')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: ['makeup', 'cup', 'usb', 'dog', 'button'],
    1: ['table', 'belt'],
    2: ['island', 'note', 'tiger', 'sculpture'],
    3: ['wig', 'coral', 'lock', 'tie'],
    4: ['butterfly', 'bird'],
    5: ['comb', 'boot'],
    6: [],
    7: ['mixer', 'phone', 'ocean', 'cat', 'swimsuit'],
    8: ['mask'],
    9: ['candle', 'needle', 'battery', 'fish'],
    10: ['soap', 'river', 'rocket', 'controller', 'starfish'],
    11: ['brush'],
    12: []
}

# Empty Box 9.
boxes[9] = []

# Remove the butterfly and the bird from Box 4.
boxes[4].remove('butterfly')
boxes[4].remove('bird')

# Put the guitar into Box 9.
boxes[9].append('guitar')

# Swap the swimsuit in Box 7 with the mask in Box 8.
boxes[7].remove('swimsuit')
boxes[8].remove('mask')
boxes[7].append('mask')
boxes[8].append('swimsuit')

# Swap the button in Box 0 with the note in Box 2.
boxes[0].remove('button')
boxes[2].remove('note')
boxes[0].append('note')
boxes[2].append('button')

# Replace the sculpture with the fork in Box 2.
boxes[2].remove('sculpture')
boxes[2].append('fork')

# Swap the coral in Box 3 with the usb in Box 0.
boxes[3].remove('coral')
boxes[0].remove('usb')
boxes[3].append('usb')
boxes[0].append('coral')

# Move the soap and the starfish and the controller from Box 10 to Box 4.
items_to_move = ['soap', 'starfish', 'controller']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[4].append(item)

# Remove the soap and the starfish from Box 4.
boxes[4].remove('soap')
boxes[4].remove('starfish')

# Move the swimsuit from Box 8 to Box 10.
boxes[8].remove('swimsuit')
boxes[10].append('swimsuit')

# Move the mask and the ocean from Box 7 to Box 3.
boxes[7].remove('mask')
boxes[7].remove('ocean')
boxes[3].append('mask')
boxes[3].append('ocean')

# Swap the fork in Box 2 with the guitar in Box 9.
boxes[2].remove('fork')
boxes[9].remove('guitar')
boxes[2].append('guitar')
boxes[9].append('fork')

# Move the controller from Box 4 to Box 5.
boxes[4].remove('controller')
boxes[5].append('controller')

# Move the makeup and the note from Box 0 to Box 1.
items_to_move = ['makeup', 'note']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Replace the phone and the mixer with the shoes and the guitar in Box 7.
boxes[7].remove('phone')
boxes[7].remove('mixer')
boxes[7].append('shoes')
boxes[7].append('guitar')

# Empty Box 3.
boxes[3] = []

# Swap the cat in Box 7 with the fork in Box 9.
boxes[7].remove('cat')
boxes[9].remove('fork')
boxes[7].append('fork')
boxes[9].append('cat')

# Empty Box 9.
boxes[9] = []

# Move the tiger and the island and the button from Box 2 to Box 12.
items_to_move = ['tiger', 'island', 'button']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[12].append(item)

# Remove the makeup and the belt and the table from Box 1.
items_to_remove = ['makeup', 'belt', 'table']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
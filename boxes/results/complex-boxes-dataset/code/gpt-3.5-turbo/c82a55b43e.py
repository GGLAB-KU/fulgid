# Initial state of boxes
boxes = {
    0: ['grass', 'necklace', 'puzzle', 'coat', 'meteor'],
    1: ['tree', 'umbrella', 'dolphin', 'bracelet', 'piano'],
    2: ['butterfly', 'wire', 'ocean', 'charger'],
    3: ['telescope'],
    4: ['mask'],
    5: ['boat', 'console', 'coral'],
    6: ['bear', 'laptop', 'speaker', 'pen']
}

# Move the puzzle from Box 0 to Box 6.
boxes[0].remove('puzzle')
boxes[6].append('puzzle')

# Remove the speaker from Box 6.
boxes[6].remove('speaker')

# Move the charger and the ocean and the butterfly from Box 2 to Box 6.
items_to_move = ['charger', 'ocean', 'butterfly']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Put the butterfly into Box 4.
boxes[4].append('butterfly')

# Move the mask from Box 4 to Box 0.
boxes[4].remove('mask')
boxes[0].append('mask')

# Put the chair and the magnet and the boat into Box 0.
items_to_move = ['chair', 'magnet', 'boat']
for item in items_to_move:
    boxes[0].append(item)

# Swap the ocean in Box 6 with the butterfly in Box 4.
boxes[6].remove('ocean')
boxes[4].remove('butterfly')
boxes[6].append('butterfly')
boxes[4].append('ocean')

# Move the wire from Box 2 to Box 3.
boxes[2].remove('wire')
boxes[3].append('wire')

# Replace the dolphin and the umbrella and the bracelet with the bowl and the shoes and the necklace in Box 1.
boxes[1].remove('dolphin')
boxes[1].remove('umbrella')
boxes[1].remove('bracelet')
boxes[1].append('bowl')
boxes[1].append('shoes')
boxes[1].append('necklace')

# Swap the console in Box 5 with the wire in Box 3.
boxes[5].remove('console')
boxes[3].remove('wire')
boxes[5].append('wire')
boxes[3].append('console')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
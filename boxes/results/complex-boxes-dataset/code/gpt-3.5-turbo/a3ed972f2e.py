# Initial state of boxes
boxes = {
    0: ['wallet', 'lock', 'dice', 'rocket', 'forest'],
    1: ['earring'],
    2: ['speaker'],
    3: ['pan', 'console'],
    4: [],
    5: ['spoon', 'horse'],
    6: ['belt', 'necklace', 'mountain', 'rock'],
    7: ['dress', 'glasses', 'phone', 'beach', 'clock']
}

# Move the phone and the dress and the glasses from Box 7 to Box 1.
items_to_move = ['phone', 'dress', 'glasses']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[1].append(item)

# Replace the console with the soap in Box 3.
boxes[3].remove('console')
boxes[3].append('soap')

# Empty Box 2.
boxes[2] = []

# Put the fridge and the makeup into Box 3.
boxes[3].extend(['fridge', 'makeup'])

# Swap the horse in Box 5 with the rock in Box 6.
boxes[5].remove('horse')
boxes[6].remove('rock')
boxes[5].append('rock')
boxes[6].append('horse')

# Remove the forest from Box 0.
boxes[0].remove('forest')

# Remove the spoon and the rock from Box 5.
boxes[5].remove('spoon')
boxes[5].remove('rock')

# Put the drum and the toaster and the note into Box 7.
boxes[7].extend(['drum', 'toaster', 'note'])

# Remove the belt and the mountain and the necklace from Box 6.
boxes[6].remove('belt')
boxes[6].remove('mountain')
boxes[6].remove('necklace')

# Put the phone and the jungle and the tie into Box 3.
boxes[3].extend(['phone', 'jungle', 'tie'])

# Move the fridge and the makeup from Box 3 to Box 7.
items_to_move = ['fridge', 'makeup']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[7].append(item)

# Remove the horse from Box 6.
boxes[6].remove('horse')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
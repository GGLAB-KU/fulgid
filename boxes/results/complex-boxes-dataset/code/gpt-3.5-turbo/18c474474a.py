# Initial state of boxes
boxes = {
    0: ['shoe', 'bracelet', 'phone'],
    1: ['umbrella', 'shirt', 'motorcycle', 'tiger'],
    2: ['beach', 'helmet', 'zipper', 'leaf', 'card'],
    3: ['pants', 'button', 'bowl', 'earring', 'game'],
    4: [],
    5: ['speaker']
}

# Replace the umbrella and the tiger with the belt and the desert in Box 1.
boxes[1].remove('umbrella')
boxes[1].remove('tiger')
boxes[1].append('belt')
boxes[1].append('desert')

# Replace the speaker with the oven in Box 5.
boxes[5].remove('speaker')
boxes[5].append('oven')

# Move the belt and the desert and the shirt from Box 1 to Box 5.
items_to_move = ['belt', 'desert', 'shirt']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[5].append(item)

# Remove the bowl from Box 3.
boxes[3].remove('bowl')

# Swap the phone in Box 0 with the motorcycle in Box 1.
boxes[0].remove('phone')
boxes[1].remove('motorcycle')
boxes[0].append('motorcycle')
boxes[1].append('phone')

# Replace the phone with the speaker in Box 1.
boxes[1].remove('phone')
boxes[1].append('speaker')

# Swap the button in Box 3 with the speaker in Box 1.
boxes[3].remove('button')
boxes[1].remove('speaker')
boxes[3].append('speaker')
boxes[1].append('button')

# Move the bracelet and the motorcycle from Box 0 to Box 5.
items_to_move = ['bracelet', 'motorcycle']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Remove the beach and the zipper and the card from Box 2.
items_to_remove = ['beach', 'zipper', 'card']
for item in items_to_remove:
    boxes[2].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
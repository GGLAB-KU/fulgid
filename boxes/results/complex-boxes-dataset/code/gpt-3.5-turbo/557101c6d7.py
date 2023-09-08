# Initial state of boxes
boxes = {
    0: ['pen', 'bell', 'lion', 'river', 'horse'],
    1: ['comet'],
    2: [],
    3: ['freezer', 'headphone', 'key', 'grinder'],
    4: ['beach', 'train', 'card']
}

# Replace the card and the beach and the train with the towel and the dog and the pot in Box 4.
boxes[4].remove('card')
boxes[4].remove('beach')
boxes[4].remove('train')
boxes[4].append('towel')
boxes[4].append('dog')
boxes[4].append('pot')

# Move the horse and the bell and the lion from Box 0 to Box 4.
items_to_move = ['horse', 'bell', 'lion']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Remove the comet from Box 1.
boxes[1].remove('comet')

# Replace the river with the button in Box 0.
boxes[0].remove('river')
boxes[0].append('button')

# Move the towel from Box 4 to Box 0.
boxes[4].remove('towel')
boxes[0].append('towel')

# Put the charger and the wig and the mountain into Box 2.
items_to_put = ['charger', 'wig', 'mountain']
for item in items_to_put:
    boxes[2].append(item)

# Remove the headphone and the grinder and the key from Box 3.
items_to_remove = ['headphone', 'grinder', 'key']
for item in items_to_remove:
    boxes[3].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: ['pillow'],
    1: ['whistle', 'bear', 'pot'],
    2: [],
    3: ['headphone', 'phone', 'seaweed', 'clock'],
    4: ['puzzle', 'truck', 'camera', 'hat', 'rain']
}

# Replace the clock and the seaweed and the headphone with the doll and the truck and the book in Box 3.
boxes[3].remove('clock')
boxes[3].remove('seaweed')
boxes[3].remove('headphone')
boxes[3].append('doll')
boxes[3].append('truck')
boxes[3].append('book')

# Remove the doll and the phone from Box 3.
boxes[3].remove('doll')
boxes[3].remove('phone')

# Put the glove and the card into Box 2.
boxes[2].append('glove')
boxes[2].append('card')

# Put the polish into Box 3.
boxes[3].append('polish')

# Empty Box 3.
boxes[3] = []

# Replace the pillow with the wig in Box 0.
boxes[0].remove('pillow')
boxes[0].append('wig')

# Move the card and the glove from Box 2 to Box 0.
items_to_move = ['card', 'glove']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
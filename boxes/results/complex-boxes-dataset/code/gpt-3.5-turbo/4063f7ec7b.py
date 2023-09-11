# Initial state of boxes
boxes = {
    0: ['doll', 'clock', 'helmet', 'zipper'],
    1: ['table'],
    2: ['note'],
    3: ['shelf', 'horse', 'fridge', 'ring'],
    4: ['scarf', 'forest'],
    5: ['dog', 'pillow'],
    6: ['bell', 'soap', 'boat', 'apple']
}

# Put the elephant and the frame into Box 4.
boxes[4].append('elephant')
boxes[4].append('frame')

# Move the helmet and the doll from Box 0 to Box 2.
boxes[0].remove('helmet')
boxes[0].remove('doll')
boxes[2].append('helmet')
boxes[2].append('doll')

# Replace the note and the doll and the helmet with the bracelet and the storm and the harmonica in Box 2.
boxes[2].remove('note')
boxes[2].remove('doll')
boxes[2].remove('helmet')
boxes[2].append('bracelet')
boxes[2].append('storm')
boxes[2].append('harmonica')

# Replace the horse and the ring and the shelf with the charger and the thunder and the ship in Box 3.
boxes[3].remove('horse')
boxes[3].remove('ring')
boxes[3].remove('shelf')
boxes[3].append('charger')
boxes[3].append('thunder')
boxes[3].append('ship')

# Replace the table with the spoon in Box 1.
boxes[1].remove('table')
boxes[1].append('spoon')

# Empty Box 5.
boxes[5] = []

# Replace the zipper with the key in Box 0.
boxes[0].remove('zipper')
boxes[0].append('key')

# Put the mirror and the glove and the button into Box 2.
boxes[2].append('mirror')
boxes[2].append('glove')
boxes[2].append('button')

# Remove the soap and the boat and the apple from Box 6.
boxes[6].remove('soap')
boxes[6].remove('boat')
boxes[6].remove('apple')

# Swap the bell in Box 6 with the storm in Box 2.
boxes[6].remove('bell')
boxes[2].remove('storm')
boxes[6].append('storm')
boxes[2].append('bell')

# Remove the ship from Box 3.
boxes[3].remove('ship')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
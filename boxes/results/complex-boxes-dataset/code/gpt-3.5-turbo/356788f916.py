# Initial state of boxes
boxes = {
    0: ['guitar', 'tape', 'car'],
    1: ['pan', 'battery', 'brush', 'comb', 'headphone'],
    2: ['dog', 'shampoo', 'flower', 'crown', 'phone'],
    3: ['plane', 'pen'],
    4: [],
    5: ['puzzle', 'pants', 'apple', 'violin'],
    6: ['bracelet', 'sculpture', 'drum'],
    7: ['note', 'snow'],
    8: ['moon'],
    9: []
}

# Swap the dog in Box 2 with the snow in Box 7.
boxes[2].remove('dog')
boxes[7].remove('snow')
boxes[2].append('snow')
boxes[7].append('dog')

# Replace the headphone and the brush with the shoe and the cat in Box 1.
boxes[1].remove('headphone')
boxes[1].remove('brush')
boxes[1].append('shoe')
boxes[1].append('cat')

# Remove the sculpture and the drum and the bracelet from Box 6.
boxes[6].remove('sculpture')
boxes[6].remove('drum')
boxes[6].remove('bracelet')

# Move the flower and the shampoo and the phone from Box 2 to Box 0.
items_to_move = ['flower', 'shampoo', 'phone']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[0].append(item)

# Move the pan and the comb from Box 1 to Box 0.
items_to_move = ['pan', 'comb']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[0].append(item)

# Swap the flower in Box 0 with the dog in Box 7.
boxes[0].remove('flower')
boxes[7].remove('dog')
boxes[0].append('dog')
boxes[7].append('flower')

# Move the pants and the puzzle from Box 5 to Box 4.
items_to_move = ['pants', 'puzzle']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Swap the pan in Box 0 with the apple in Box 5.
boxes[0].remove('pan')
boxes[5].remove('apple')
boxes[0].append('apple')
boxes[5].append('pan')

# Put the laptop into Box 9.
boxes[9].append('laptop')

# Replace the puzzle and the pants with the ocean and the frame in Box 4.
boxes[4].remove('puzzle')
boxes[4].remove('pants')
boxes[4].append('ocean')
boxes[4].append('frame')

# Swap the crown in Box 2 with the pen in Box 3.
boxes[2].remove('crown')
boxes[3].remove('pen')
boxes[2].append('pen')
boxes[3].append('crown')

# Remove the note from Box 7.
boxes[7].remove('note')

# Put the wire and the shoes and the harmonica into Box 7.
items_to_put = ['wire', 'shoes', 'harmonica']
for item in items_to_put:
    boxes[7].append(item)

# Swap the violin in Box 5 with the wire in Box 7.
boxes[5].remove('violin')
boxes[7].remove('wire')
boxes[5].append('wire')
boxes[7].append('violin')

# Remove the crown and the plane from Box 3.
boxes[3].remove('crown')
boxes[3].remove('plane')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
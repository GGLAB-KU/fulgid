# Initial state of boxes
boxes = {
    0: ['mirror', 'doll', 'puzzle', 'wire', 'oven'],
    1: ['brush', 'bicycle', 'dress', 'blanket'],
    2: ['phone', 'sock', 'basket'],
    3: ['cat'],
    4: ['mountain', 'note', 'glove', 'starfish', 'bag'],
    5: ['elephant', 'tiger', 'comb', 'lion', 'bracelet'],
    6: ['island'],
    7: ['whistle', 'plate', 'grinder', 'branch'],
    8: ['dice', 'octopus', 'sculpture', 'piano'],
    9: ['toothbrush', 'pillow'],
    10: ['comet', 'harmonica', 'rain', 'submarine']
}

# Replace the octopus and the piano and the sculpture with the dice and the zipper and the guitar in Box 8.
boxes[8].remove('octopus')
boxes[8].remove('piano')
boxes[8].remove('sculpture')
boxes[8].append('dice')
boxes[8].append('zipper')
boxes[8].append('guitar')

# Empty Box 10.
boxes[10] = []

# Replace the toothbrush with the glasses in Box 9.
boxes[9].remove('toothbrush')
boxes[9].append('glasses')

# Move the guitar and the dice and the dice from Box 8 to Box 10.
items_to_move = ['guitar', 'dice', 'dice']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[10].append(item)

# Remove the bicycle and the blanket from Box 1.
items_to_remove = ['bicycle', 'blanket']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the comb in Box 5 with the note in Box 4.
boxes[5].remove('comb')
boxes[4].remove('note')
boxes[5].append('note')
boxes[4].append('comb')

# Remove the doll from Box 0.
boxes[0].remove('doll')

# Swap the cat in Box 3 with the branch in Box 7.
boxes[3].remove('cat')
boxes[7].remove('branch')
boxes[3].append('branch')
boxes[7].append('cat')

# Remove the grinder from Box 7.
boxes[7].remove('grinder')

# Remove the guitar and the dice and the dice from Box 10.
items_to_remove = ['guitar', 'dice', 'dice']
for item in items_to_remove:
    boxes[10].remove(item)

# Move the comb and the glove from Box 4 to Box 6.
items_to_move = ['comb', 'glove']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[6].append(item)

# Put the meteor into Box 7.
boxes[7].append('meteor')

# Put the toothbrush and the button and the spoon into Box 5.
items_to_put = ['toothbrush', 'button', 'spoon']
for item in items_to_put:
    boxes[5].append(item)

# Put the bracelet into Box 10.
boxes[10].append('bracelet')

# Replace the brush and the dress with the scarf and the desert in Box 1.
boxes[1].remove('brush')
boxes[1].remove('dress')
boxes[1].append('scarf')
boxes[1].append('desert')

# Move the glasses and the pillow from Box 9 to Box 3.
items_to_move = ['glasses', 'pillow']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[3].append(item)

# Swap the desert in Box 1 with the basket in Box 2.
boxes[1].remove('desert')
boxes[2].remove('basket')
boxes[1].append('basket')
boxes[2].append('desert')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
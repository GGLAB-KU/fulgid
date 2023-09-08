# Initial state of boxes
boxes = {
    0: ['soap', 'mirror', 'seaweed', 'dog'],
    1: ['lightning', 'sun', 'island'],
    2: [],
    3: ['bus', 'harmonica', 'skirt', 'tiger'],
    4: ['planet', 'key', 'microscope'],
    5: [],
    6: ['train', 'snow', 'fridge'],
    7: ['ship', 'hat', 'butterfly', 'comet'],
    8: []
}

# Replace the skirt with the wire in Box 3.
boxes[3].remove('skirt')
boxes[3].append('wire')

# Swap the butterfly in Box 7 with the soap in Box 0.
boxes[0].remove('soap')
boxes[7].remove('butterfly')
boxes[0].append('butterfly')
boxes[7].append('soap')

# Move the butterfly and the mirror from Box 0 to Box 2.
items_to_move = ['butterfly', 'mirror']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Move the fridge from Box 6 to Box 7.
boxes[6].remove('fridge')
boxes[7].append('fridge')

# Remove the harmonica from Box 3.
boxes[3].remove('harmonica')

# Replace the bus with the brush in Box 3.
boxes[3].remove('bus')
boxes[3].append('brush')

# Swap the wire in Box 3 with the butterfly in Box 2.
boxes[3].remove('wire')
boxes[2].remove('butterfly')
boxes[3].append('butterfly')
boxes[2].append('wire')

# Move the mirror from Box 2 to Box 8.
boxes[2].remove('mirror')
boxes[8].append('mirror')

# Remove the train from Box 6.
boxes[6].remove('train')

# Empty Box 1.
boxes[1] = []

# Swap the butterfly in Box 3 with the snow in Box 6.
boxes[3].remove('butterfly')
boxes[6].remove('snow')
boxes[3].append('snow')
boxes[6].append('butterfly')

# Move the mirror from Box 8 to Box 3.
boxes[8].remove('mirror')
boxes[3].append('mirror')

# Put the lightning into Box 0.
boxes[0].append('lightning')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
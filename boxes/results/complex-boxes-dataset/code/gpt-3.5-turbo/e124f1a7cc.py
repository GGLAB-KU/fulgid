# Initial state of boxes
boxes = {
    0: ['belt', 'dog'],
    1: ['harmonica'],
    2: ['rocket', 'glove', 'mask', 'controller'],
    3: ['bracelet'],
    4: ['guitar', 'mirror'],
    5: ['candle', 'shirt', 'blanket', 'paint'],
    6: [],
    7: ['lamp', 'headphone'],
    8: ['river', 'umbrella', 'brush']
}

# Move the bracelet from Box 3 to Box 4.
boxes[3].remove('bracelet')
boxes[4].append('bracelet')

# Replace the glove and the rocket with the button and the planet in Box 2.
boxes[2].remove('glove')
boxes[2].remove('rocket')
boxes[2].append('button')
boxes[2].append('planet')

# Move the harmonica from Box 1 to Box 5.
boxes[1].remove('harmonica')
boxes[5].append('harmonica')

# Move the belt and the dog from Box 0 to Box 3.
boxes[0].remove('belt')
boxes[0].remove('dog')
boxes[3].append('belt')
boxes[3].append('dog')

# Put the lion and the sandals and the fish into Box 5.
items_to_move = ['lion', 'sandals', 'fish']
for item in items_to_move:
    boxes[5].append(item)

# Move the planet and the mask from Box 2 to Box 4.
boxes[2].remove('planet')
boxes[2].remove('mask')
boxes[4].append('planet')
boxes[4].append('mask')

# Remove the planet and the mask and the mirror from Box 4.
items_to_remove = ['planet', 'mask', 'mirror']
for item in items_to_remove:
    boxes[4].remove(item)

# Replace the belt and the dog with the bracelet and the coat in Box 3.
boxes[3].remove('belt')
boxes[3].remove('dog')
boxes[3].append('bracelet')
boxes[3].append('coat')

# Move the headphone from Box 7 to Box 0.
boxes[7].remove('headphone')
boxes[0].append('headphone')

# Put the hat and the lightning and the phone into Box 7.
items_to_move = ['hat', 'lightning', 'phone']
for item in items_to_move:
    boxes[7].append(item)

# Move the brush from Box 8 to Box 1.
boxes[8].remove('brush')
boxes[1].append('brush')

# Swap the shirt in Box 5 with the guitar in Box 4.
boxes[5].remove('shirt')
boxes[4].remove('guitar')
boxes[5].append('guitar')
boxes[4].append('shirt')

# Swap the headphone in Box 0 with the button in Box 2.
boxes[0].remove('headphone')
boxes[2].remove('button')
boxes[0].append('button')
boxes[2].append('headphone')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
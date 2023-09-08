# Initial state of boxes
boxes = {
    0: ['planet', 'paint'],
    1: ['earring', 'comet', 'puzzle'],
    2: ['leaf', 'needle'],
    3: ['pillow', 'shelf'],
    4: ['umbrella', 'wire', 'telescope', 'snow', 'speaker'],
    5: ['shoe', 'mask'],
    6: ['wallet', 'soap', 'scarf', 'watch', 'grass'],
    7: [],
    8: [],
    9: ['polish', 'lamp', 'car', 'bell'],
    10: ['button'],
    11: ['bear'],
    12: ['apple', 'microscope', 'rain', 'harmonica']
}

# Replace the planet with the perfume in Box 0.
boxes[0].remove('planet')
boxes[0].append('perfume')

# Remove the button from Box 10.
boxes[10].remove('button')

# Replace the bear with the scissors in Box 11.
boxes[11].remove('bear')
boxes[11].append('scissors')

# Empty Box 5.
boxes[5] = []

# Swap the perfume in Box 0 with the comet in Box 1.
boxes[0].remove('perfume')
boxes[1].remove('comet')
boxes[0].append('comet')
boxes[1].append('perfume')

# Remove the pillow from Box 3.
boxes[3].remove('pillow')

# Move the watch and the scarf from Box 6 to Box 7.
items_to_move = ['watch', 'scarf']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[7].append(item)

# Empty Box 2.
boxes[2] = []

# Move the shelf from Box 3 to Box 6.
boxes[3].remove('shelf')
boxes[6].append('shelf')

# Move the grass and the shelf and the wallet from Box 6 to Box 3.
items_to_move = ['grass', 'shelf', 'wallet']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[3].append(item)

# Replace the rain with the seaweed in Box 12.
boxes[12].remove('rain')
boxes[12].append('seaweed')

# Remove the wire and the snow and the umbrella from Box 4.
items_to_remove = ['wire', 'snow', 'umbrella']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the polish from Box 9 to Box 12.
boxes[9].remove('polish')
boxes[12].append('polish')

# Swap the scarf in Box 7 with the comet in Box 0.
boxes[7].remove('scarf')
boxes[0].remove('comet')
boxes[7].append('comet')
boxes[0].append('scarf')

# Replace the polish with the plate in Box 12.
boxes[12].remove('polish')
boxes[12].append('plate')

# Move the scissors from Box 11 to Box 12.
boxes[11].remove('scissors')
boxes[12].append('scissors')

# Put the basket into Box 4.
boxes[4].append('basket')

# Move the speaker from Box 4 to Box 7.
boxes[4].remove('speaker')
boxes[7].append('speaker')

# Remove the scarf from Box 0.
boxes[0].remove('scarf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
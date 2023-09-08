# Initial state of boxes
boxes = {
    0: ['wire'],
    1: ['perfume', 'toaster'],
    2: ['microscope'],
    3: ['belt'],
    4: ['swimsuit', 'rocket', 'puzzle', 'tie'],
    5: ['telescope', 'grass', 'spoon', 'starfish', 'glove'],
    6: ['book'],
    7: ['comet', 'guitar', 'cat', 'tiger'],
    8: [],
    9: ['comb', 'toy', 'pen'],
    10: ['scissors', 'coral'],
    11: [],
    12: ['butterfly']
}

# Replace the cat with the beach in Box 7.
boxes[7].remove('cat')
boxes[7].append('beach')

# Move the pen from Box 9 to Box 0.
boxes[9].remove('pen')
boxes[0].append('pen')

# Put the horn and the telescope and the glasses into Box 6.
items_to_move = ['horn', 'telescope', 'glasses']
for item in items_to_move:
    boxes[6].append(item)

# Replace the pen and the wire with the jungle and the boot in Box 0.
boxes[0].remove('pen')
boxes[0].remove('wire')
boxes[0].append('jungle')
boxes[0].append('boot')

# Put the telescope and the planet into Box 4.
items_to_move = ['telescope', 'planet']
for item in items_to_move:
    boxes[4].append(item)

# Move the perfume from Box 1 to Box 3.
boxes[1].remove('perfume')
boxes[3].append('perfume')

# Put the speaker and the glasses into Box 1.
items_to_move = ['speaker', 'glasses']
for item in items_to_move:
    boxes[1].append(item)

# Move the microscope from Box 2 to Box 11.
boxes[2].remove('microscope')
boxes[11].append('microscope')

# Move the toaster and the glasses and the speaker from Box 1 to Box 8.
items_to_move = ['toaster', 'glasses', 'speaker']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[8].append(item)

# Put the tape into Box 7.
boxes[7].append('tape')

# Move the comb and the toy from Box 9 to Box 1.
items_to_move = ['comb', 'toy']
for item in items_to_move:
    boxes[9].remove(item)
    boxes[1].append(item)

# Swap the scissors in Box 10 with the perfume in Box 3.
boxes[10].remove('scissors')
boxes[3].remove('perfume')
boxes[10].append('perfume')
boxes[3].append('scissors')

# Put the soap into Box 4.
boxes[4].append('soap')

# Swap the toy in Box 1 with the glasses in Box 6.
boxes[1].remove('toy')
boxes[6].remove('glasses')
boxes[1].append('glasses')
boxes[6].append('toy')

# Remove the jungle and the boot from Box 0.
boxes[0].remove('jungle')
boxes[0].remove('boot')

# Put the brush and the wig and the button into Box 7.
items_to_move = ['brush', 'wig', 'button']
for item in items_to_move:
    boxes[7].append(item)

# Swap the puzzle in Box 4 with the glasses in Box 8.
boxes[4].remove('puzzle')
boxes[8].remove('glasses')
boxes[4].append('glasses')
boxes[8].append('puzzle')

# Remove the comet and the brush from Box 7.
boxes[7].remove('comet')
boxes[7].remove('brush')

# Put the doll and the mixer and the game into Box 2.
items_to_move = ['doll', 'mixer', 'game']
for item in items_to_move:
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
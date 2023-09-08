# Initial state of boxes
boxes = {
    0: ['key'],
    1: ['fish', 'sculpture', 'microscope'],
    2: ['storm', 'car', 'coat', 'cat', 'hat'],
    3: ['shoes', 'button', 'submarine', 'pen'],
    4: ['toaster', 'glasses'],
    5: ['comb', 'bicycle', 'bowl', 'table'],
    6: ['drum'],
    7: ['leaf', 'comet'],
    8: ['lamp', 'zipper', 'bus', 'dolphin']
}

# Replace the comet with the keyboard in Box 7.
boxes[7].remove('comet')
boxes[7].append('keyboard')

# Empty Box 1.
boxes[1] = []

# Swap the bowl in Box 5 with the lamp in Box 8.
boxes[5].remove('bowl')
boxes[8].remove('lamp')
boxes[5].append('lamp')
boxes[8].append('bowl')

# Replace the glasses and the toaster with the rock and the mixer in Box 4.
boxes[4].remove('glasses')
boxes[4].remove('toaster')
boxes[4].append('rock')
boxes[4].append('mixer')

# Remove the leaf from Box 7.
boxes[7].remove('leaf')

# Remove the bicycle and the table from Box 5.
boxes[5].remove('bicycle')
boxes[5].remove('table')

# Replace the coat and the hat and the cat with the mountain and the shorts and the book in Box 2.
boxes[2].remove('coat')
boxes[2].remove('hat')
boxes[2].remove('cat')
boxes[2].append('mountain')
boxes[2].append('shorts')
boxes[2].append('book')

# Move the drum from Box 6 to Box 4.
boxes[6].remove('drum')
boxes[4].append('drum')

# Put the scissors and the shoes and the comb into Box 2.
items_to_move = ['scissors', 'shoes', 'comb']
for item in items_to_move:
    boxes[2].append(item)

# Remove the key from Box 0.
boxes[0].remove('key')

# Remove the mixer from Box 4.
boxes[4].remove('mixer')

# Move the rock from Box 4 to Box 3.
boxes[4].remove('rock')
boxes[3].append('rock')

# Replace the rock with the puzzle in Box 3.
boxes[3].remove('rock')
boxes[3].append('puzzle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
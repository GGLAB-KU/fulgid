# Initial state of boxes
boxes = {
    0: ['planet', 'controller', 'lion', 'coin'],
    1: ['laptop', 'bell'],
    2: ['bear', 'boot'],
    3: ['island', 'tie', 'beach', 'hat'],
    4: ['comet', 'microscope', 'seaweed', 'cat'],
    5: ['butterfly'],
    6: ['toaster'],
    7: ['flower', 'star', 'console', 'apple', 'telescope'],
    8: ['train', 'tape', 'mirror', 'drum'],
    9: ['bicycle', 'meteor', 'submarine', 'puzzle'],
    10: ['belt']
}

# Move the butterfly from Box 5 to Box 8.
boxes[5].remove('butterfly')
boxes[8].append('butterfly')

# Replace the toaster with the comb in Box 6.
boxes[6].remove('toaster')
boxes[6].append('comb')

# Replace the console with the bird in Box 7.
boxes[7].remove('console')
boxes[7].append('bird')

# Swap the belt in Box 10 with the bell in Box 1.
boxes[10].remove('belt')
boxes[1].remove('bell')
boxes[10].append('bell')
boxes[1].append('belt')

# Replace the tie and the island and the hat with the starfish and the mountain and the bus in Box 3.
boxes[3].remove('tie')
boxes[3].remove('island')
boxes[3].remove('hat')
boxes[3].append('starfish')
boxes[3].append('mountain')
boxes[3].append('bus')

# Put the wig and the dolphin and the speaker into Box 5.
items_to_move = ['wig', 'dolphin', 'speaker']
for item in items_to_move:
    boxes[5].append(item)

# Remove the bell from Box 10.
boxes[10].remove('bell')

# Swap the cat in Box 4 with the controller in Box 0.
boxes[4].remove('cat')
boxes[0].remove('controller')
boxes[4].append('controller')
boxes[0].append('cat')

# Move the puzzle from Box 9 to Box 4.
boxes[9].remove('puzzle')
boxes[4].append('puzzle')

# Move the comb from Box 6 to Box 1.
boxes[6].remove('comb')
boxes[1].append('comb')

# Put the spoon into Box 9.
boxes[9].append('spoon')

# Move the laptop and the comb and the belt from Box 1 to Box 4.
items_to_move = ['laptop', 'comb', 'belt']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Replace the star and the flower and the apple with the planet and the cow and the towel in Box 7.
boxes[7].remove('star')
boxes[7].remove('flower')
boxes[7].remove('apple')
boxes[7].append('planet')
boxes[7].append('cow')
boxes[7].append('towel')

# Replace the beach and the mountain and the starfish with the coin and the tree and the mask in Box 3.
boxes[3].remove('beach')
boxes[3].remove('mountain')
boxes[3].remove('starfish')
boxes[3].append('coin')
boxes[3].append('tree')
boxes[3].append('mask')

# Remove the planet and the coin from Box 0.
boxes[0].remove('planet')
boxes[0].remove('coin')

# Put the seaweed and the horn into Box 6.
boxes[6].append('seaweed')
boxes[6].append('horn')

# Replace the microscope and the puzzle with the fork and the truck in Box 4.
boxes[4].remove('microscope')
boxes[4].remove('puzzle')
boxes[4].append('fork')
boxes[4].append('truck')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
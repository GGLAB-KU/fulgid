# Initial state of boxes
boxes = {
    0: ['bus', 'submarine', 'piano', 'apple'],
    1: ['mirror', 'planet', 'necklace', 'jungle'],
    2: ['note', 'toothbrush', 'crown', 'comb'],
    3: ['microscope'],
    4: ['island', 'tree', 'game'],
    5: ['dice', 'bicycle'],
    6: ['pot', 'starfish', 'scissors', 'whistle'],
    7: ['octopus', 'makeup', 'coat'],
    8: [],
    9: ['pan', 'grinder', 'keyboard', 'toothpaste', 'boat'],
    10: ['thread', 'paint'],
    11: ['lion', 'candle'],
    12: ['tape', 'sock', 'star']
}

# Swap the toothbrush in Box 2 with the bicycle in Box 5.
boxes[2].remove('toothbrush')
boxes[5].remove('bicycle')
boxes[2].append('bicycle')
boxes[5].append('toothbrush')

# Move the microscope from Box 3 to Box 5.
boxes[3].remove('microscope')
boxes[5].append('microscope')

# Replace the whistle and the starfish with the doll and the shoes in Box 6.
boxes[6].remove('whistle')
boxes[6].remove('starfish')
boxes[6].append('doll')
boxes[6].append('shoes')

# Put the glasses into Box 0.
boxes[0].append('glasses')

# Empty Box 11.
boxes[11] = []

# Swap the piano in Box 0 with the planet in Box 1.
boxes[0].remove('piano')
boxes[1].remove('planet')
boxes[0].append('planet')
boxes[1].append('piano')

# Swap the grinder in Box 9 with the piano in Box 1.
boxes[9].remove('grinder')
boxes[1].remove('piano')
boxes[9].append('piano')
boxes[1].append('grinder')

# Swap the pot in Box 6 with the toothbrush in Box 5.
boxes[6].remove('pot')
boxes[5].remove('toothbrush')
boxes[6].append('toothbrush')
boxes[5].append('pot')

# Swap the pot in Box 5 with the paint in Box 10.
boxes[5].remove('pot')
boxes[10].remove('paint')
boxes[5].append('paint')
boxes[10].append('pot')

# Replace the scissors and the shoes with the rain and the razor in Box 6.
boxes[6].remove('scissors')
boxes[6].remove('shoes')
boxes[6].append('rain')
boxes[6].append('razor')

# Replace the necklace and the jungle and the grinder with the bear and the bird and the horse in Box 1.
boxes[1].remove('necklace')
boxes[1].remove('jungle')
boxes[9].remove('grinder')
boxes[1].append('bear')
boxes[1].append('bird')
boxes[1].append('horse')

# Swap the boat in Box 9 with the doll in Box 6.
boxes[9].remove('boat')
boxes[6].remove('doll')
boxes[9].append('doll')
boxes[6].append('boat')

# Remove the pot and the thread from Box 10.
boxes[10].remove('pot')
boxes[10].remove('thread')

# Move the dice from Box 5 to Box 3.
boxes[5].remove('dice')
boxes[3].append('dice')

# Remove the makeup and the coat from Box 7.
boxes[7].remove('makeup')
boxes[7].remove('coat')

# Move the apple from Box 0 to Box 2.
boxes[0].remove('apple')
boxes[2].append('apple')

# Swap the bear in Box 1 with the crown in Box 2.
boxes[1].remove('bear')
boxes[2].remove('crown')
boxes[1].append('crown')
boxes[2].append('bear')

# Move the doll from Box 9 to Box 7.
boxes[9].remove('doll')
boxes[7].append('doll')

# Move the tape from Box 12 to Box 1.
boxes[12].remove('tape')
boxes[1].append('tape')

# Swap the tree in Box 4 with the dice in Box 3.
boxes[4].remove('tree')
boxes[3].remove('dice')
boxes[4].append('dice')
boxes[3].append('tree')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
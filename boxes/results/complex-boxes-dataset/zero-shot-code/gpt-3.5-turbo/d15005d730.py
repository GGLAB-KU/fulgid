box = {
    0: ['snow', 'chair'],
    1: ['dice'],
    2: ['doll'],
    3: ['lipstick', 'elephant'],
    4: [],
    5: ['boat', 'usb', 'shirt'],
    6: ['battery', 'paint', 'dog', 'controller', 'blender'],
    7: ['earring', 'guitar', 'comet', 'thread'],
    8: ['planet'],
    9: [],
    10: ['basket'],
    11: ['shelf']
}

def print_boxes():
    for i in range(12):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Put the storm into Box 6
box[6].append('storm')

# Put the swimsuit and the jungle and the pot into Box 1
box[1].extend(['swimsuit', 'jungle', 'pot'])

# Remove the chair from Box 0
box[0].remove('chair')

# Replace the doll with the earring in Box 2
box[2].remove('doll')
box[2].append('earring')

# Replace the planet with the lamp in Box 8
box[8].remove('planet')
box[8].append('lamp')

# Replace the earring with the bicycle in Box 2
box[2].remove('earring')
box[2].append('bicycle')

# Move the comet and the thread and the earring from Box 7 to Box 0
box[0].extend(['comet', 'thread', 'earring'])
box[7].remove('comet')
box[7].remove('thread')
box[7].remove('earring')

# Put the scissors and the thunder into Box 0
box[0].extend(['scissors', 'thunder'])

# Remove the storm from Box 6
box[6].remove('storm')

# Swap the basket in Box 10 with the snow in Box 0
box[0].remove('snow')
box[10].remove('basket')
box[0].append('basket')
box[10].append('snow')

# Put the dice into Box 9
box[9].append('dice')

# Move the thunder from Box 0 to Box 5
box[5].append('thunder')
box[0].remove('thunder')

# Move the elephant from Box 3 to Box 10
box[10].append('elephant')
box[3].remove('elephant')

# Remove the lipstick from Box 3
box[3].remove('lipstick')

# Move the jungle and the dice and the pot from Box 1 to Box 6
box[6].extend(['jungle', 'dice', 'pot'])
box[1].remove('jungle')
box[1].remove('dice')
box[1].remove('pot')

# Swap the lamp in Box 8 with the elephant in Box 10
box[10].remove('elephant')
box[8].remove('lamp')
box[10].append('lamp')
box[8].append('elephant')

# Swap the shelf in Box 11 with the swimsuit in Box 1
box[1].remove('swimsuit')
box[11].remove('shelf')
box[1].append('shelf')
box[11].append('swimsuit')

# Move the swimsuit from Box 11 to Box 10
box[10].append('swimsuit')
box[11].remove('swimsuit')

# Print the boxes
print_boxes()
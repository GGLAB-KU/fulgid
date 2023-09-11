# Initial state of boxes
boxes = {
    0: ['lipstick', 'sock', 'needle'],
    1: ['soap', 'scissors'],
    2: ['cup', 'doll', 'whistle', 'swimsuit'],
    3: ['vase', 'drum', 'toy'],
    4: ['zipper', 'lock', 'ship', 'jungle'],
    5: ['meteor', 'keyboard'],
    6: ['thunder'],
    7: ['octopus', 'watch'],
    8: ['seaweed', 'umbrella'],
    9: ['snow', 'bird', 'horn'],
    10: ['table', 'jacket']
}

# Put the comet into Box 10.
boxes[10].append('comet')

# Swap the soap in Box 1 with the toy in Box 3.
boxes[1].remove('soap')
boxes[3].remove('toy')
boxes[1].append('toy')
boxes[3].append('soap')

# Remove the meteor and the keyboard from Box 5.
boxes[5].remove('meteor')
boxes[5].remove('keyboard')

# Replace the ship with the beach in Box 4.
boxes[4].remove('ship')
boxes[4].append('beach')

# Swap the needle in Box 0 with the jacket in Box 10.
boxes[0].remove('needle')
boxes[10].remove('jacket')
boxes[0].append('jacket')
boxes[10].append('needle')

# Swap the sock in Box 0 with the umbrella in Box 8.
boxes[0].remove('sock')
boxes[8].remove('umbrella')
boxes[0].append('umbrella')
boxes[8].append('sock')

# Swap the bird in Box 9 with the seaweed in Box 8.
boxes[9].remove('bird')
boxes[8].remove('seaweed')
boxes[9].append('seaweed')
boxes[8].append('bird')

# Swap the toy in Box 1 with the drum in Box 3.
boxes[1].remove('toy')
boxes[3].remove('drum')
boxes[1].append('drum')
boxes[3].append('toy')

# Swap the table in Box 10 with the octopus in Box 7.
boxes[10].remove('table')
boxes[7].remove('octopus')
boxes[10].append('octopus')
boxes[7].append('table')

# Empty Box 2.
boxes[2] = []

# Empty Box 10.
boxes[10] = []

# Move the sock and the bird from Box 8 to Box 4.
items_to_move = ['sock', 'bird']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[4].append(item)

# Put the helmet into Box 7.
boxes[7].append('helmet')

# Swap the horn in Box 9 with the drum in Box 1.
boxes[9].remove('horn')
boxes[1].remove('drum')
boxes[9].append('drum')
boxes[1].append('horn')

# Swap the seaweed in Box 9 with the lipstick in Box 0.
boxes[9].remove('seaweed')
boxes[0].remove('lipstick')
boxes[9].append('lipstick')
boxes[0].append('seaweed')

# Swap the table in Box 7 with the umbrella in Box 0.
boxes[7].remove('table')
boxes[0].remove('umbrella')
boxes[7].append('umbrella')
boxes[0].append('table')

# Move the toy from Box 3 to Box 6.
boxes[3].remove('toy')
boxes[6].append('toy')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
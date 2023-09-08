# Initial state of boxes
boxes = {
    0: ['sock', 'lion', 'wire', 'tiger', 'towel'],
    1: ['bird', 'shark'],
    2: ['watch', 'paint', 'horse'],
    3: ['lightning', 'drum', 'toaster', 'crown', 'bus'],
    4: ['needle'],
    5: ['shirt', 'meteor', 'rain', 'glove'],
    6: ['jacket', 'dog', 'basket'],
    7: ['phone', 'wallet', 'ocean']
}

# Put the wire and the razor and the horse into Box 0.
boxes[0].append('wire')
boxes[0].append('razor')
boxes[0].append('horse')

# Remove the watch and the paint and the horse from Box 2.
boxes[2].remove('watch')
boxes[2].remove('paint')
boxes[2].remove('horse')

# Remove the bird from Box 1.
boxes[1].remove('bird')

# Swap the shirt in Box 5 with the phone in Box 7.
boxes[5].remove('shirt')
boxes[7].remove('phone')
boxes[5].append('phone')
boxes[7].append('shirt')

# Replace the shark with the cow in Box 1.
boxes[1].remove('shark')
boxes[1].append('cow')

# Move the needle from Box 4 to Box 0.
boxes[4].remove('needle')
boxes[0].append('needle')

# Move the toaster and the lightning from Box 3 to Box 4.
boxes[3].remove('toaster')
boxes[3].remove('lightning')
boxes[4].append('toaster')
boxes[4].append('lightning')

# Remove the crown and the bus and the drum from Box 3.
boxes[3].remove('crown')
boxes[3].remove('bus')
boxes[3].remove('drum')

# Put the oven into Box 7.
boxes[7].append('oven')

# Swap the dog in Box 6 with the phone in Box 5.
boxes[6].remove('dog')
boxes[5].remove('phone')
boxes[6].append('phone')
boxes[5].append('dog')

# Replace the meteor and the rain with the sandals and the button in Box 5.
boxes[5].remove('meteor')
boxes[5].remove('rain')
boxes[5].append('sandals')
boxes[5].append('button')

# Remove the cow from Box 1.
boxes[1].remove('cow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
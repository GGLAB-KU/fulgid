# Initial state of boxes
boxes = {
    0: ['phone', 'oven', 'keyboard', 'pan'],
    1: ['controller'],
    2: ['brush'],
    3: ['necklace', 'table', 'lipstick'],
    4: ['bicycle'],
    5: ['grinder', 'plane', 'butterfly', 'forest', 'motorcycle'],
    6: ['laptop'],
    7: ['ship'],
    8: ['toaster', 'submarine']
}

# Replace the lipstick with the mask in Box 3.
boxes[3].remove('lipstick')
boxes[3].append('mask')

# Replace the toaster with the coat in Box 8.
boxes[8].remove('toaster')
boxes[8].append('coat')

# Swap the pan in Box 0 with the motorcycle in Box 5.
boxes[0].remove('pan')
boxes[5].remove('motorcycle')
boxes[0].append('motorcycle')
boxes[5].append('pan')

# Replace the oven and the motorcycle and the keyboard with the horse and the tiger and the lion in Box 0.
boxes[0].remove('oven')
boxes[0].remove('motorcycle')
boxes[0].remove('keyboard')
boxes[0].append('horse')
boxes[0].append('tiger')
boxes[0].append('lion')

# Move the brush from Box 2 to Box 1.
boxes[2].remove('brush')
boxes[1].append('brush')

# Remove the brush from Box 1.
boxes[1].remove('brush')

# Put the octopus and the sock and the spoon into Box 7.
items_to_move = ['octopus', 'sock', 'spoon']
for item in items_to_move:
    boxes[7].append(item)

# Replace the tiger with the ocean in Box 0.
boxes[0].remove('tiger')
boxes[0].append('ocean')

# Put the lightning and the lock into Box 6.
items_to_move = ['lightning', 'lock']
for item in items_to_move:
    boxes[6].append(item)

# Replace the mask and the necklace with the book and the dog in Box 3.
boxes[3].remove('mask')
boxes[3].remove('necklace')
boxes[3].append('book')
boxes[3].append('dog')

# Put the shorts and the headphone into Box 6.
items_to_move = ['shorts', 'headphone']
for item in items_to_move:
    boxes[6].append(item)

# Put the basket into Box 8.
boxes[8].append('basket')

# Swap the controller in Box 1 with the octopus in Box 7.
boxes[1].remove('controller')
boxes[7].remove('octopus')
boxes[1].append('octopus')
boxes[7].append('controller')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
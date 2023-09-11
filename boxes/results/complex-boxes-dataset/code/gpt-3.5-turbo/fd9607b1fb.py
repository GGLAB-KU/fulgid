# Initial state of boxes
boxes = {
    0: ['pot', 'oven'],
    1: ['bowl'],
    2: ['forest', 'harmonica', 'soap'],
    3: ['towel', 'sculpture', 'toothbrush', 'mirror'],
    4: ['grinder', 'toaster', 'ring', 'frame'],
    5: ['magnet'],
    6: ['octopus', 'lipstick', 'planet'],
    7: ['crown', 'lock', 'motorcycle', 'wallet'],
    8: ['usb'],
    9: ['keyboard', 'pen', 'shelf'],
    10: ['jacket', 'island', 'whistle', 'comb']
}

# Remove the oven from Box 0.
boxes[0].remove('oven')

# Swap the bowl in Box 1 with the toothbrush in Box 3.
boxes[1].remove('bowl')
boxes[3].remove('toothbrush')
boxes[1].append('toothbrush')
boxes[3].append('bowl')

# Move the grinder from Box 4 to Box 1.
boxes[4].remove('grinder')
boxes[1].append('grinder')

# Replace the octopus with the lamp in Box 6.
boxes[6].remove('octopus')
boxes[6].append('lamp')

# Move the harmonica and the soap and the forest from Box 2 to Box 10.
items_to_move = ['harmonica', 'soap', 'forest']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[10].append(item)

# Put the horse into Box 1.
boxes[1].append('horse')

# Put the apple and the toothbrush into Box 8.
boxes[8].append('apple')
boxes[8].append('toothbrush')

# Put the microwave and the wire into Box 10.
boxes[10].append('microwave')
boxes[10].append('wire')

# Swap the planet in Box 6 with the apple in Box 8.
boxes[6].remove('planet')
boxes[8].remove('apple')
boxes[6].append('apple')
boxes[8].append('planet')

# Replace the lamp and the apple with the ring and the game in Box 6.
boxes[6].remove('lamp')
boxes[6].remove('apple')
boxes[6].append('ring')
boxes[6].append('game')

# Move the magnet from Box 5 to Box 1.
boxes[5].remove('magnet')
boxes[1].append('magnet')

# Put the shoes and the horse and the shampoo into Box 6.
boxes[6].append('shoes')
boxes[6].append('horse')
boxes[6].append('shampoo')

# Put the ocean into Box 9.
boxes[9].append('ocean')

# Swap the usb in Box 8 with the game in Box 6.
boxes[8].remove('usb')
boxes[6].remove('game')
boxes[8].append('game')
boxes[6].append('usb')

# Move the crown and the motorcycle and the lock from Box 7 to Box 9.
items_to_move = ['crown', 'motorcycle', 'lock']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[9].append(item)

# Put the octopus and the perfume and the microwave into Box 4.
boxes[4].append('octopus')
boxes[4].append('perfume')
boxes[4].append('microwave')

# Remove the wallet from Box 7.
boxes[7].remove('wallet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
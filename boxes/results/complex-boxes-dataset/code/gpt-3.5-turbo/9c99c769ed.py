# Initial state of boxes
boxes = {
    0: [],
    1: ['microwave', 'game', 'harmonica', 'cow'],
    2: ['toothbrush'],
    3: ['shoe', 'doll', 'candle', 'forest', 'sock'],
    4: ['bag', 'chair', 'polish', 'branch', 'scarf'],
    5: ['plane', 'boot'],
    6: ['butterfly', 'zipper', 'headphone', 'skirt'],
    7: [],
    8: ['wallet', 'beach', 'ship'],
    9: ['shoes', 'battery'],
    10: ['jungle', 'clock', 'telescope', 'console', 'spoon']
}

# Remove the boot from Box 5.
boxes[5].remove('boot')

# Move the toothbrush from Box 2 to Box 9.
boxes[2].remove('toothbrush')
boxes[9].append('toothbrush')

# Move the candle and the shoe from Box 3 to Box 8.
items_to_move = ['candle', 'shoe']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[8].append(item)

# Replace the cow and the microwave and the harmonica with the horse and the tree and the soap in Box 1.
boxes[1].remove('cow')
boxes[1].remove('microwave')
boxes[1].remove('harmonica')
boxes[1].append('horse')
boxes[1].append('tree')
boxes[1].append('soap')

# Swap the doll in Box 3 with the plane in Box 5.
boxes[3].remove('doll')
boxes[5].remove('plane')
boxes[3].append('plane')
boxes[5].append('doll')

# Swap the sock in Box 3 with the doll in Box 5.
boxes[3].remove('sock')
boxes[5].remove('doll')
boxes[3].append('doll')
boxes[5].append('sock')

# Replace the soap and the game with the belt and the helmet in Box 1.
boxes[1].remove('soap')
boxes[1].remove('game')
boxes[1].append('belt')
boxes[1].append('helmet')

# Replace the zipper with the puzzle in Box 6.
boxes[6].remove('zipper')
boxes[6].append('puzzle')

# Swap the skirt in Box 6 with the sock in Box 5.
boxes[6].remove('skirt')
boxes[5].remove('sock')
boxes[6].append('sock')
boxes[5].append('skirt')

# Put the magnet into Box 0.
boxes[0].append('magnet')

# Replace the puzzle and the headphone and the sock with the swimsuit and the usb and the bus in Box 6.
boxes[6].remove('puzzle')
boxes[6].remove('headphone')
boxes[6].remove('sock')
boxes[6].append('swimsuit')
boxes[6].append('usb')
boxes[6].append('bus')

# Put the wire and the sandals and the toy into Box 8.
items_to_move = ['wire', 'sandals', 'toy']
for item in items_to_move:
    boxes[8].append(item)

# Put the horn into Box 7.
boxes[7].append('horn')

# Remove the horn from Box 7.
boxes[7].remove('horn')

# Put the wire and the perfume into Box 6.
boxes[6].append('wire')
boxes[6].append('perfume')

# Remove the skirt from Box 5.
boxes[5].remove('skirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: ['ring', 'keyboard', 'tape'],
    1: ['freezer', 'controller', 'frame'],
    2: ['mask', 'charger'],
    3: ['guitar', 'blender', 'forest', 'magnet'],
    4: ['sock', 'book', 'watch', 'wig'],
    5: ['blanket', 'lightning', 'necklace'],
    6: ['wallet', 'river', 'branch', 'tiger'],
    7: ['helmet'],
    8: ['toaster', 'microwave', 'doll', 'starfish']
}

# Swap the wig in Box 4 with the guitar in Box 3.
boxes[4].remove('wig')
boxes[3].remove('guitar')
boxes[4].append('guitar')
boxes[3].append('wig')

# Replace the charger with the jungle in Box 2.
boxes[2].remove('charger')
boxes[2].append('jungle')

# Put the plate and the pot and the towel into Box 1.
items_to_move = ['plate', 'pot', 'towel']
for item in items_to_move:
    boxes[1].append(item)

# Put the wig and the harmonica and the shorts into Box 6.
items_to_move = ['wig', 'harmonica', 'shorts']
for item in items_to_move:
    boxes[6].append(item)

# Move the helmet from Box 7 to Box 1.
boxes[7].remove('helmet')
boxes[1].append('helmet')

# Swap the jungle in Box 2 with the doll in Box 8.
boxes[2].remove('jungle')
boxes[8].remove('doll')
boxes[2].append('doll')
boxes[8].append('jungle')

# Remove the sock from Box 4.
boxes[4].remove('sock')

# Swap the frame in Box 1 with the wallet in Box 6.
boxes[1].remove('frame')
boxes[6].remove('wallet')
boxes[1].append('wallet')
boxes[6].append('frame')

# Move the watch and the guitar from Box 4 to Box 7.
items_to_move = ['watch', 'guitar']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[7].append(item)

# Swap the helmet in Box 1 with the mask in Box 2.
boxes[1].remove('helmet')
boxes[2].remove('mask')
boxes[1].append('mask')
boxes[2].append('helmet')

# Remove the book from Box 4.
boxes[4].remove('book')

# Put the plate and the polish and the fork into Box 3.
items_to_move = ['plate', 'polish', 'fork']
for item in items_to_move:
    boxes[3].append(item)

# Swap the plate in Box 3 with the blanket in Box 5.
boxes[3].remove('plate')
boxes[5].remove('blanket')
boxes[3].append('blanket')
boxes[5].append('plate')

# Empty Box 8.
boxes[8] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
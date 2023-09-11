# Initial state of boxes
boxes = {
    0: ['sandals', 'watch', 'frame', 'pot'],
    1: ['microwave', 'bicycle', 'starfish'],
    2: ['boot'],
    3: [],
    4: ['bracelet'],
    5: ['grinder', 'camera', 'plane'],
    6: ['tree', 'shoes', 'table', 'skirt'],
    7: ['ship', 'ring', 'scarf', 'desert', 'jacket'],
    8: ['helmet', 'controller']
}

# Move the helmet and the controller from Box 8 to Box 6.
items_to_move = ['helmet', 'controller']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[6].append(item)

# Remove the desert and the ship and the scarf from Box 7.
items_to_remove = ['desert', 'ship', 'scarf']
for item in items_to_remove:
    boxes[7].remove(item)

# Replace the bracelet with the gloves in Box 4.
boxes[4].remove('bracelet')
boxes[4].append('gloves')

# Swap the pot in Box 0 with the plane in Box 5.
boxes[0].remove('pot')
boxes[5].remove('plane')
boxes[0].append('plane')
boxes[5].append('pot')

# Put the fish into Box 5.
boxes[5].append('fish')

# Move the grinder from Box 5 to Box 6.
boxes[5].remove('grinder')
boxes[6].append('grinder')

# Remove the jacket from Box 7.
boxes[7].remove('jacket')

# Empty Box 1.
boxes[1] = []

# Swap the gloves in Box 4 with the tree in Box 6.
boxes[4].remove('gloves')
boxes[6].remove('tree')
boxes[4].append('tree')
boxes[6].append('gloves')

# Put the belt into Box 5.
boxes[5].append('belt')

# Replace the watch and the plane and the sandals with the shirt and the gloves and the sock in Box 0.
boxes[0].remove('watch')
boxes[0].remove('plane')
boxes[0].remove('sandals')
boxes[0].append('shirt')
boxes[0].append('gloves')
boxes[0].append('sock')

# Move the frame and the shirt from Box 0 to Box 6.
boxes[0].remove('frame')
boxes[0].remove('shirt')
boxes[6].append('frame')
boxes[6].append('shirt')

# Replace the fish and the pot with the necklace and the wig in Box 5.
boxes[5].remove('fish')
boxes[5].remove('pot')
boxes[5].append('necklace')
boxes[5].append('wig')

# Swap the sock in Box 0 with the ring in Box 7.
boxes[0].remove('sock')
boxes[7].remove('ring')
boxes[0].append('ring')
boxes[7].append('sock')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
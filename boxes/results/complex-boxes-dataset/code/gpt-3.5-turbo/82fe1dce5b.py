# Initial state of boxes
boxes = {
    0: ['charger', 'brush', 'star', 'wig', 'wire'],
    1: ['speaker', 'pen', 'harmonica'],
    2: ['jacket', 'grinder'],
    3: ['snow', 'glasses', 'seaweed', 'sandals', 'shelf'],
    4: ['earring', 'clock', 'towel', 'battery'],
    5: ['crown'],
    6: [],
    7: ['mask', 'zipper', 'rain', 'river'],
    8: ['gloves', 'thread', 'headphone']
}

# Remove the mask and the river and the zipper from Box 7.
items_to_remove = ['mask', 'river', 'zipper']
for item in items_to_remove:
    boxes[7].remove(item)

# Put the bowl and the microwave and the ring into Box 1.
items_to_add = ['bowl', 'microwave', 'ring']
for item in items_to_add:
    boxes[1].append(item)

# Swap the microwave in Box 1 with the grinder in Box 2.
boxes[1].remove('microwave')
boxes[2].remove('grinder')
boxes[1].append('grinder')
boxes[2].append('microwave')

# Swap the glasses in Box 3 with the ring in Box 1.
boxes[3].remove('glasses')
boxes[1].remove('ring')
boxes[3].append('ring')
boxes[1].append('glasses')

# Remove the headphone and the gloves from Box 8.
boxes[8].remove('headphone')
boxes[8].remove('gloves')

# Move the speaker from Box 1 to Box 6.
boxes[1].remove('speaker')
boxes[6].append('speaker')

# Remove the wire and the brush and the wig from Box 0.
items_to_remove = ['wire', 'brush', 'wig']
for item in items_to_remove:
    boxes[0].remove(item)

# Put the bracelet and the pen and the pot into Box 6.
items_to_add = ['bracelet', 'pen', 'pot']
for item in items_to_add:
    boxes[6].append(item)

# Put the drum and the horse and the ship into Box 7.
items_to_add = ['drum', 'horse', 'ship']
for item in items_to_add:
    boxes[7].append(item)

# Replace the horse and the rain with the sock and the shampoo in Box 7.
boxes[7].remove('horse')
boxes[7].remove('rain')
boxes[7].append('sock')
boxes[7].append('shampoo')

# Remove the ship and the drum and the shampoo from Box 7.
items_to_remove = ['ship', 'drum', 'shampoo']
for item in items_to_remove:
    boxes[7].remove(item)

# Put the candle into Box 6.
boxes[6].append('candle')

# Remove the grinder and the pen and the glasses from Box 1.
items_to_remove = ['grinder', 'pen', 'glasses']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the jacket in Box 2 with the charger in Box 0.
boxes[2].remove('jacket')
boxes[0].remove('charger')
boxes[2].append('charger')
boxes[0].append('jacket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
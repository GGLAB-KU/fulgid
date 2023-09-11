# Initial state of boxes
boxes = {
    0: ['thread', 'bus', 'train', 'meteor', 'flute'],
    1: ['coral'],
    2: ['sock', 'toothpaste', 'bell'],
    3: ['vase', 'scarf', 'moon'],
    4: ['jacket'],
    5: [],
    6: ['truck', 'bag', 'river', 'dice'],
    7: ['thunder', 'fork', 'fridge', 'harmonica', 'frame'],
    8: ['toothbrush'],
    9: ['blanket', 'wallet', 'shorts', 'wire', 'soap'],
    10: [],
    11: ['tiger', 'lamp', 'skirt', 'wig', 'bowl'],
    12: ['rock', 'plate']
}

# Remove the river from Box 6.
boxes[6].remove('river')

# Replace the plate with the drum in Box 12.
boxes[12].remove('plate')
boxes[12].append('drum')

# Remove the drum from Box 12.
boxes[12].remove('drum')

# Move the vase and the scarf from Box 3 to Box 5.
items_to_move = ['vase', 'scarf']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[5].append(item)

# Move the train and the thread and the meteor from Box 0 to Box 2.
items_to_move = ['train', 'thread', 'meteor']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Put the laptop and the chair and the mountain into Box 1.
items_to_put = ['laptop', 'chair', 'mountain']
for item in items_to_put:
    boxes[1].append(item)

# Replace the harmonica and the frame with the shoes and the soap in Box 7.
boxes[7].remove('harmonica')
boxes[7].remove('frame')
boxes[7].append('shoes')
boxes[7].append('soap')

# Move the bus from Box 0 to Box 4.
boxes[0].remove('bus')
boxes[4].append('bus')

# Remove the vase and the scarf from Box 5.
boxes[5].remove('vase')
boxes[5].remove('scarf')

# Remove the jacket from Box 4.
boxes[4].remove('jacket')

# Remove the tiger from Box 11.
boxes[11].remove('tiger')

# Replace the wallet and the soap and the blanket with the boot and the rocket and the button in Box 9.
boxes[9].remove('wallet')
boxes[9].remove('soap')
boxes[9].remove('blanket')
boxes[9].append('boot')
boxes[9].append('rocket')
boxes[9].append('button')

# Remove the laptop from Box 1.
boxes[1].remove('laptop')

# Replace the soap with the bag in Box 7.
boxes[7].remove('soap')
boxes[7].append('bag')

# Put the cup and the shampoo into Box 9.
items_to_put = ['cup', 'shampoo']
for item in items_to_put:
    boxes[9].append(item)

# Replace the skirt and the lamp with the plate and the horn in Box 11.
boxes[11].remove('skirt')
boxes[11].remove('lamp')
boxes[11].append('plate')
boxes[11].append('horn')

# Replace the bus with the submarine in Box 4.
boxes[4].remove('bus')
boxes[4].append('submarine')

# Remove the submarine from Box 4.
boxes[4].remove('submarine')

# Move the rock from Box 12 to Box 7.
boxes[12].remove('rock')
boxes[7].append('rock')

# Move the toothpaste and the meteor from Box 2 to Box 1.
items_to_move = ['toothpaste', 'meteor']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
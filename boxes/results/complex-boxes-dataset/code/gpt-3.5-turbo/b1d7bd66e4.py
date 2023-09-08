# Initial state of boxes
boxes = {
    0: [],
    1: ['train'],
    2: ['toaster', 'bracelet', 'storm', 'fridge'],
    3: ['usb', 'fish', 'note', 'coral'],
    4: ['thunder', 'lightning'],
    5: ['doll', 'pillow'],
    6: ['wig'],
    7: ['earring', 'thread', 'mountain', 'coin', 'game'],
    8: ['dress', 'mask', 'dice'],
    9: ['guitar', 'jungle', 'puzzle', 'flute', 'microscope'],
    10: [],
    11: ['comet', 'jacket', 'star', 'basket'],
    12: ['island', 'pants', 'sun', 'grinder'],
    13: ['ship', 'blender', 'controller', 'leaf'],
    14: ['spoon', 'scissors', 'horn', 'horse']
}

# Put the scissors and the polish and the rocket into Box 2.
boxes[2].extend(['scissors', 'polish', 'rocket'])

# Remove the dice and the mask and the dress from Box 8.
items_to_remove = ['dice', 'mask', 'dress']
for item in items_to_remove:
    boxes[8].remove(item)

# Replace the note and the fish with the bag and the bicycle in Box 3.
boxes[3].remove('note')
boxes[3].remove('fish')
boxes[3].append('bag')
boxes[3].append('bicycle')

# Replace the pillow with the rocket in Box 5.
boxes[5].remove('pillow')
boxes[5].append('rocket')

# Remove the horse and the horn and the spoon from Box 14.
items_to_remove = ['horse', 'horn', 'spoon']
for item in items_to_remove:
    boxes[14].remove(item)

# Move the train from Box 1 to Box 11.
boxes[1].remove('train')
boxes[11].append('train')

# Remove the ship from Box 13.
boxes[13].remove('ship')

# Replace the bicycle and the coral with the ring and the bag in Box 3.
boxes[3].remove('bicycle')
boxes[3].remove('coral')
boxes[3].append('ring')
boxes[3].append('bag')

# Replace the doll and the rocket with the grass and the boot in Box 5.
boxes[5].remove('doll')
boxes[5].remove('rocket')
boxes[5].append('grass')
boxes[5].append('boot')

# Empty Box 2.
boxes[2] = []

# Put the truck into Box 10.
boxes[10].append('truck')

# Replace the grass with the star in Box 5.
boxes[5].remove('grass')
boxes[5].append('star')

# Put the leaf and the pen and the whistle into Box 13.
boxes[13].extend(['leaf', 'pen', 'whistle'])

# Remove the truck from Box 10.
boxes[10].remove('truck')

# Swap the wig in Box 6 with the flute in Box 9.
boxes[6], boxes[9] = boxes[9], boxes[6]

# Move the jungle from Box 9 to Box 7.
boxes[9].remove('jungle')
boxes[7].append('jungle')

# Move the bag and the bag from Box 3 to Box 7.
boxes[3].remove('bag')
boxes[3].remove('bag')
boxes[7].extend(['bag', 'bag'])

# Put the river into Box 8.
boxes[8].append('river')

# Put the pants into Box 6.
boxes[6].append('pants')

# Empty Box 7.
boxes[7] = []

# Remove the river from Box 8.
boxes[8].remove('river')

# Replace the usb with the tie in Box 3.
boxes[3].remove('usb')
boxes[3].append('tie')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
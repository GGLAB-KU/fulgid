# Initial state of boxes
boxes = {
    0: ['plane', 'usb', 'wire', 'star'],
    1: ['gloves'],
    2: ['submarine', 'speaker', 'shoe', 'pillow'],
    3: ['camera', 'leaf'],
    4: ['violin', 'cow', 'pants', 'lion', 'paint'],
    5: ['necklace', 'boot'],
    6: ['oven', 'lock', 'piano', 'phone'],
    7: [],
    8: [],
    9: ['perfume', 'charger', 'plate'],
    10: ['scissors'],
    11: ['button', 'harmonica', 'planet', 'guitar', 'shampoo'],
    12: ['towel', 'puzzle', 'scarf'],
    13: ['game', 'fork', 'doll'],
    14: ['dice', 'hat']
}

# Remove the cow from Box 4.
boxes[4].remove('cow')

# Put the boot and the ship into Box 3.
boxes[3].append('boot')
boxes[3].append('ship')

# Move the lion and the paint from Box 4 to Box 13.
boxes[4].remove('lion')
boxes[4].remove('paint')
boxes[13].append('lion')
boxes[13].append('paint')

# Move the puzzle and the scarf from Box 12 to Box 6.
boxes[12].remove('puzzle')
boxes[12].remove('scarf')
boxes[6].append('puzzle')
boxes[6].append('scarf')

# Put the cow and the bag and the bracelet into Box 11.
boxes[11].append('cow')
boxes[11].append('bag')
boxes[11].append('bracelet')

# Swap the towel in Box 12 with the star in Box 0.
boxes[12].remove('towel')
boxes[0].remove('star')
boxes[12].append('star')
boxes[0].append('towel')

# Remove the fork and the lion and the paint from Box 13.
boxes[13].remove('fork')
boxes[13].remove('lion')
boxes[13].remove('paint')

# Empty Box 5.
boxes[5] = []

# Swap the scissors in Box 10 with the pillow in Box 2.
boxes[10].remove('scissors')
boxes[2].remove('pillow')
boxes[10].append('pillow')
boxes[2].append('scissors')

# Move the pants from Box 4 to Box 0.
boxes[4].remove('pants')
boxes[0].append('pants')

# Put the perfume into Box 1.
boxes[1].append('perfume')

# Move the plane and the pants and the wire from Box 0 to Box 14.
items_to_move = ['plane', 'pants', 'wire']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[14].append(item)

# Swap the violin in Box 4 with the shoe in Box 2.
boxes[4].remove('violin')
boxes[2].remove('shoe')
boxes[4].append('shoe')
boxes[2].append('violin')

# Move the hat from Box 14 to Box 11.
boxes[14].remove('hat')
boxes[11].append('hat')

# Swap the phone in Box 6 with the game in Box 13.
boxes[6].remove('phone')
boxes[13].remove('game')
boxes[6].append('game')
boxes[13].append('phone')

# Replace the violin with the sculpture in Box 2.
boxes[2].remove('violin')
boxes[2].append('sculpture')

# Swap the charger in Box 9 with the pillow in Box 10.
boxes[9].remove('charger')
boxes[10].remove('pillow')
boxes[9].append('pillow')
boxes[10].append('charger')

# Empty Box 2.
boxes[2] = []

# Remove the charger from Box 10.
boxes[10].remove('charger')

# Move the towel and the usb from Box 0 to Box 1.
boxes[0].remove('towel')
boxes[0].remove('usb')
boxes[1].append('towel')
boxes[1].append('usb')

# Move the star from Box 12 to Box 13.
boxes[12].remove('star')
boxes[13].append('star')

# Put the zipper and the pillow into Box 9.
boxes[9].append('zipper')
boxes[9].append('pillow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
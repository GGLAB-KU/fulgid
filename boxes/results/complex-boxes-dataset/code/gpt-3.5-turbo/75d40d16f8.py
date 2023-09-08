# Initial state of boxes
boxes = {
    0: [],
    1: ['sculpture', 'sock', 'game'],
    2: ['zipper', 'boot', 'scissors', 'butterfly', 'freezer'],
    3: ['lion', 'car', 'thread', 'soap'],
    4: ['usb', 'toothpaste', 'coral', 'comet', 'necklace'],
    5: ['submarine', 'skirt', 'headphone', 'cat', 'umbrella'],
    6: [],
    7: ['sandals', 'shorts', 'gloves', 'snow'],
    8: ['tape'],
    9: ['key', 'lipstick'],
    10: ['shelf', 'motorcycle'],
    11: ['seaweed', 'magnet']
}

# Put the hat and the mirror and the lamp into Box 5.
items_to_put = ['hat', 'mirror', 'lamp']
for item in items_to_put:
    boxes[5].append(item)

# Swap the sock in Box 1 with the usb in Box 4.
boxes[1].remove('sock')
boxes[4].remove('usb')
boxes[1].append('usb')
boxes[4].append('sock')

# Swap the key in Box 9 with the scissors in Box 2.
boxes[9].remove('key')
boxes[2].remove('scissors')
boxes[9].append('scissors')
boxes[2].append('key')

# Replace the car with the sculpture in Box 3.
boxes[3].remove('car')
boxes[3].append('sculpture')

# Replace the tape with the pot in Box 8.
boxes[8].remove('tape')
boxes[8].append('pot')

# Remove the seaweed and the magnet from Box 11.
boxes[11].remove('seaweed')
boxes[11].remove('magnet')

# Replace the butterfly and the freezer and the key with the blender and the belt and the toothpaste in Box 2.
boxes[2].remove('butterfly')
boxes[2].remove('freezer')
boxes[2].remove('key')
boxes[2].append('blender')
boxes[2].append('belt')
boxes[2].append('toothpaste')

# Put the shelf and the sun into Box 0.
boxes[0].append('shelf')
boxes[0].append('sun')

# Remove the scissors and the lipstick from Box 9.
boxes[9].remove('scissors')
boxes[9].remove('lipstick')

# Put the wallet and the rocket and the book into Box 2.
items_to_put = ['wallet', 'rocket', 'book']
for item in items_to_put:
    boxes[2].append(item)

# Move the game and the sculpture and the usb from Box 1 to Box 4.
items_to_move = ['game', 'sculpture', 'usb']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Move the pot from Box 8 to Box 3.
boxes[8].remove('pot')
boxes[3].append('pot')

# Replace the wallet and the toothpaste with the towel and the swimsuit in Box 2.
boxes[2].remove('wallet')
boxes[2].remove('toothpaste')
boxes[2].append('towel')
boxes[2].append('swimsuit')

# Replace the shorts and the sandals with the lock and the vase in Box 7.
boxes[7].remove('shorts')
boxes[7].remove('sandals')
boxes[7].append('lock')
boxes[7].append('vase')

# Put the bracelet into Box 6.
boxes[6].append('bracelet')

# Replace the shelf and the sun with the boot and the violin in Box 0.
boxes[0].remove('shelf')
boxes[0].remove('sun')
boxes[0].append('boot')
boxes[0].append('violin')

# Replace the motorcycle and the shelf with the starfish and the butterfly in Box 10.
boxes[10].remove('motorcycle')
boxes[10].remove('shelf')
boxes[10].append('starfish')
boxes[10].append('butterfly')

# Remove the bracelet from Box 6.
boxes[6].remove('bracelet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
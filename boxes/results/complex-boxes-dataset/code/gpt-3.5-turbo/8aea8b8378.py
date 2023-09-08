# Initial state of boxes
boxes = {
    0: ['console', 'button', 'whistle', 'controller'],
    1: ['plane', 'note', 'key', 'game', 'cloud'],
    2: [],
    3: ['scissors', 'book', 'razor', 'cow'],
    4: ['pillow', 'mixer', 'oven', 'doll'],
    5: ['horn', 'motorcycle', 'earring'],
    6: ['card', 'rocket', 'desert', 'bicycle', 'telescope'],
    7: ['charger'],
    8: ['bell', 'helmet', 'chair'],
    9: ['battery'],
    10: ['shoes', 'cup', 'dice', 'violin', 'mirror'],
    11: ['cat', 'sock', 'table', 'microscope', 'needle'],
    12: []
}

# Move the plane from Box 1 to Box 9.
boxes[1].remove('plane')
boxes[9].append('plane')

# Remove the cat and the needle and the sock from Box 11.
items_to_remove = ['cat', 'needle', 'sock']
for item in items_to_remove:
    boxes[11].remove(item)

# Put the snow and the tie into Box 12.
boxes[12].append('snow')
boxes[12].append('tie')

# Swap the table in Box 11 with the controller in Box 0.
boxes[11].remove('table')
boxes[0].remove('controller')
boxes[11].append('controller')
boxes[0].append('table')

# Swap the book in Box 3 with the bicycle in Box 6.
boxes[3].remove('book')
boxes[6].remove('bicycle')
boxes[3].append('bicycle')
boxes[6].append('book')

# Put the lion and the planet and the sculpture into Box 6.
boxes[6].append('lion')
boxes[6].append('planet')
boxes[6].append('sculpture')

# Move the key from Box 1 to Box 6.
boxes[1].remove('key')
boxes[6].append('key')

# Remove the cloud from Box 1.
boxes[1].remove('cloud')

# Replace the horn and the earring and the motorcycle with the usb and the coral and the bus in Box 5.
boxes[5].remove('horn')
boxes[5].remove('earring')
boxes[5].remove('motorcycle')
boxes[5].append('usb')
boxes[5].append('coral')
boxes[5].append('bus')

# Remove the snow from Box 12.
boxes[12].remove('snow')

# Replace the coral and the usb and the bus with the shirt and the toy and the rain in Box 5.
boxes[5].remove('coral')
boxes[5].remove('usb')
boxes[5].remove('bus')
boxes[5].append('shirt')
boxes[5].append('toy')
boxes[5].append('rain')

# Put the key into Box 11.
boxes[11].append('key')

# Replace the whistle and the table with the shoe and the truck in Box 0.
boxes[0].remove('whistle')
boxes[0].remove('table')
boxes[0].append('shoe')
boxes[0].append('truck')

# Move the toy and the shirt and the rain from Box 5 to Box 2.
items_to_move = ['toy', 'shirt', 'rain']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Put the shark and the lipstick and the thunder into Box 7.
boxes[7].append('shark')
boxes[7].append('lipstick')
boxes[7].append('thunder')

# Remove the sculpture and the key and the planet from Box 6.
items_to_remove = ['sculpture', 'key', 'planet']
for item in items_to_remove:
    boxes[6].remove(item)

# Empty Box 12.
boxes[12] = []

# Put the shoe into Box 4.
boxes[4].append('shoe')

# Move the oven and the doll from Box 4 to Box 3.
boxes[4].remove('oven')
boxes[4].remove('doll')
boxes[3].append('oven')
boxes[3].append('doll')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
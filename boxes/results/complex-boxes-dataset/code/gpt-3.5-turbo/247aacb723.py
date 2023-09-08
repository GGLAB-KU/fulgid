# Initial state of boxes
boxes = {
    0: [],
    1: ['bus'],
    2: ['brush', 'toothbrush'],
    3: ['dog', 'skirt', 'card', 'dice', 'truck'],
    4: ['wire', 'lion'],
    5: ['grass', 'horn', 'ocean'],
    6: [],
    7: ['shirt', 'chair'],
    8: ['tiger', 'charger'],
    9: ['phone', 'puzzle', 'shelf', 'rain', 'blender'],
    10: ['sock', 'lamp', 'cup', 'pot', 'coin'],
    11: ['rocket', 'coat', 'plane', 'thunder'],
    12: ['seaweed', 'boat'],
    13: ['game'],
    14: ['elephant', 'shorts', 'cat', 'storm', 'towel']
}

# Replace the tiger with the soap in Box 8.
boxes[8].remove('tiger')
boxes[8].append('soap')

# Replace the pot and the cup and the lamp with the seaweed and the controller and the thunder in Box 10.
boxes[10].remove('pot')
boxes[10].remove('cup')
boxes[10].remove('lamp')
boxes[10].append('seaweed')
boxes[10].append('controller')
boxes[10].append('thunder')

# Move the towel and the cat and the storm from Box 14 to Box 13.
items_to_move = ['towel', 'cat', 'storm']
for item in items_to_move:
    boxes[14].remove(item)
    boxes[13].append(item)

# Empty Box 1.
boxes[1] = []

# Remove the controller from Box 10.
boxes[10].remove('controller')

# Put the magnet into Box 2.
boxes[2].append('magnet')

# Replace the shorts and the elephant with the bowl and the toothbrush in Box 14.
boxes[14].remove('shorts')
boxes[14].remove('elephant')
boxes[14].append('bowl')
boxes[14].append('toothbrush')

# Empty Box 11.
boxes[11] = []

# Remove the boat and the seaweed from Box 12.
boxes[12].remove('boat')
boxes[12].remove('seaweed')

# Remove the ocean from Box 5.
boxes[5].remove('ocean')

# Swap the card in Box 3 with the phone in Box 9.
boxes[3].remove('card')
boxes[9].remove('phone')
boxes[3].append('phone')
boxes[9].append('card')

# Replace the dice and the phone with the pillow and the usb in Box 3.
boxes[3].remove('dice')
boxes[3].remove('phone')
boxes[3].append('pillow')
boxes[3].append('usb')

# Move the bowl and the toothbrush from Box 14 to Box 6.
boxes[14].remove('bowl')
boxes[14].remove('toothbrush')
boxes[6].append('bowl')
boxes[6].append('toothbrush')

# Replace the truck with the river in Box 3.
boxes[3].remove('truck')
boxes[3].append('river')

# Swap the seaweed in Box 10 with the river in Box 3.
boxes[10].remove('seaweed')
boxes[3].remove('river')
boxes[10].append('river')
boxes[3].append('seaweed')

# Move the usb from Box 3 to Box 11.
boxes[3].remove('usb')
boxes[11].append('usb')

# Remove the charger and the soap from Box 8.
boxes[8].remove('charger')
boxes[8].remove('soap')

# Replace the cat and the storm with the shelf and the sculpture in Box 13.
boxes[13].remove('cat')
boxes[13].remove('storm')
boxes[13].append('shelf')
boxes[13].append('sculpture')

# Swap the horn in Box 5 with the shelf in Box 9.
boxes[5].remove('horn')
boxes[9].remove('shelf')
boxes[5].append('shelf')
boxes[9].append('horn')

# Move the usb from Box 11 to Box 8.
boxes[11].remove('usb')
boxes[8].append('usb')

# Put the meteor and the harmonica into Box 8.
boxes[8].append('meteor')
boxes[8].append('harmonica')

# Move the bowl from Box 6 to Box 7.
boxes[6].remove('bowl')
boxes[7].append('bowl')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
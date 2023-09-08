# Initial state of boxes
boxes = {
    0: ['car', 'bowl', 'sun'],
    1: ['key', 'usb', 'bag'],
    2: ['oven', 'button'],
    3: ['jacket', 'toaster', 'tape'],
    4: ['boat', 'shorts', 'glasses', 'bicycle', 'train'],
    5: ['ring', 'swimsuit'],
    6: ['coin', 'rock'],
    7: [],
    8: ['telescope', 'mountain', 'lamp', 'bracelet', 'shampoo'],
    9: ['rain', 'toy', 'pants']
}

# Put the ocean and the towel and the candle into Box 4.
boxes[4].append('ocean')
boxes[4].append('towel')
boxes[4].append('candle')

# Replace the jacket with the storm in Box 3.
boxes[3].remove('jacket')
boxes[3].append('storm')

# Move the mountain and the lamp and the shampoo from Box 8 to Box 9.
items_to_move = ['mountain', 'lamp', 'shampoo']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[9].append(item)

# Remove the bag and the usb and the key from Box 1.
items_to_remove = ['bag', 'usb', 'key']
for item in items_to_remove:
    boxes[1].remove(item)

# Move the lamp from Box 9 to Box 6.
boxes[9].remove('lamp')
boxes[6].append('lamp')

# Move the oven and the button from Box 2 to Box 5.
boxes[2].remove('oven')
boxes[2].remove('button')
boxes[5].append('oven')
boxes[5].append('button')

# Empty Box 8.
boxes[8] = []

# Swap the shampoo in Box 9 with the lamp in Box 6.
boxes[9].remove('shampoo')
boxes[6].remove('lamp')
boxes[9].append('lamp')
boxes[6].append('shampoo')

# Remove the coin and the rock from Box 6.
boxes[6].remove('coin')
boxes[6].remove('rock')

# Remove the bicycle and the shorts from Box 4.
boxes[4].remove('bicycle')
boxes[4].remove('shorts')

# Move the car and the bowl from Box 0 to Box 1.
boxes[0].remove('car')
boxes[0].remove('bowl')
boxes[1].append('car')
boxes[1].append('bowl')

# Replace the towel and the ocean with the sculpture and the drum in Box 4.
boxes[4].remove('towel')
boxes[4].remove('ocean')
boxes[4].append('sculpture')
boxes[4].append('drum')

# Put the cloud and the truck and the wig into Box 7.
boxes[7].append('cloud')
boxes[7].append('truck')
boxes[7].append('wig')

# Swap the bowl in Box 1 with the toy in Box 9.
boxes[1].remove('bowl')
boxes[9].remove('toy')
boxes[1].append('toy')
boxes[9].append('bowl')

# Remove the pants from Box 9.
boxes[9].remove('pants')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
# Initial state of boxes
boxes = {
    0: ['spoon', 'headphone', 'fork', 'tree'],
    1: ['toothbrush', 'tie', 'toaster', 'key', 'soap'],
    2: ['scarf', 'paint'],
    3: [],
    4: ['piano', 'dice', 'charger', 'jacket'],
    5: ['clock', 'elephant', 'frame', 'wire', 'comb'],
    6: ['dolphin', 'table'],
    7: ['hat', 'keyboard', 'freezer', 'candle'],
    8: ['flute', 'watch', 'usb'],
    9: ['butterfly', 'lock', 'dog', 'snow'],
    10: ['whistle', 'plane', 'cat'],
    11: ['shampoo', 'basket', 'storm', 'horse', 'telescope'],
    12: ['belt', 'pen'],
    13: ['seaweed', 'car'],
    14: ['mountain']
}

# Remove the cat and the plane from Box 10.
boxes[10].remove('cat')
boxes[10].remove('plane')

# Move the mountain from Box 14 to Box 11.
boxes[14].remove('mountain')
boxes[11].append('mountain')

# Replace the belt with the laptop in Box 12.
boxes[12].remove('belt')
boxes[12].append('laptop')

# Put the wire and the phone and the game into Box 7.
items_to_move = ['wire', 'phone', 'game']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[7].append(item)

# Move the scarf and the paint from Box 2 to Box 14.
items_to_move = ['scarf', 'paint']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[14].append(item)

# Move the headphone from Box 0 to Box 5.
boxes[0].remove('headphone')
boxes[5].append('headphone')

# Move the seaweed from Box 13 to Box 3.
boxes[13].remove('seaweed')
boxes[3].append('seaweed')

# Replace the storm with the river in Box 11.
boxes[11].remove('storm')
boxes[11].append('river')

# Remove the key and the toaster from Box 1.
boxes[1].remove('key')
boxes[1].remove('toaster')

# Put the shoes and the spoon and the bird into Box 2.
items_to_move = ['shoes', 'spoon', 'bird']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Move the telescope and the river and the horse from Box 11 to Box 5.
items_to_move = ['telescope', 'river', 'horse']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[5].append(item)

# Remove the shoes and the spoon from Box 2.
boxes[2].remove('shoes')
boxes[2].remove('spoon')

# Swap the car in Box 13 with the lock in Box 9.
boxes[13].remove('car')
boxes[9].remove('lock')
boxes[13].append('lock')
boxes[9].append('car')

# Swap the clock in Box 5 with the seaweed in Box 3.
boxes[5].remove('clock')
boxes[3].remove('seaweed')
boxes[5].append('seaweed')
boxes[3].append('clock')

# Put the helmet and the table into Box 8.
items_to_move = ['helmet', 'table']
for item in items_to_move:
    boxes[8].append(item)

# Put the lipstick and the vase and the pants into Box 14.
items_to_move = ['lipstick', 'vase', 'pants']
for item in items_to_move:
    boxes[14].append(item)

# Swap the laptop in Box 12 with the scarf in Box 14.
boxes[12].remove('laptop')
boxes[14].remove('scarf')
boxes[12].append('scarf')
boxes[14].append('laptop')

# Move the dice from Box 4 to Box 6.
boxes[4].remove('dice')
boxes[6].append('dice')

# Move the bird from Box 2 to Box 0.
boxes[2].remove('bird')
boxes[0].append('bird')

# Move the piano and the charger from Box 4 to Box 5.
boxes[4].remove('piano')
boxes[4].remove('charger')
boxes[5].append('piano')
boxes[5].append('charger')

# Swap the game in Box 7 with the elephant in Box 5.
boxes[7].remove('game')
boxes[5].remove('elephant')
boxes[7].append('elephant')
boxes[5].append('game')

# Remove the scarf from Box 12.
boxes[12].remove('scarf')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")
box_0 = ['spoon', 'headphone', 'fork', 'tree']
box_1 = ['toothbrush', 'tie', 'toaster', 'key', 'soap']
box_2 = ['scarf', 'paint']
box_3 = []
box_4 = ['piano', 'dice', 'charger', 'jacket']
box_5 = ['clock', 'elephant', 'frame', 'wire', 'comb']
box_6 = ['dolphin', 'table']
box_7 = ['hat', 'keyboard', 'freezer', 'candle']
box_8 = ['flute', 'watch', 'usb']
box_9 = ['butterfly', 'lock', 'dog', 'snow']
box_10 = ['whistle', 'plane']
box_11 = ['shampoo', 'basket', 'storm', 'horse', 'telescope']
box_12 = ['belt', 'pen']
box_13 = ['seaweed', 'car']
box_14 = ['mountain']

def print_boxes():
    for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12, box_13, box_14]):
        print(f"Box {i}: {box}")

# Initial state
print_boxes()

# Remove the cat and the plane from Box 10
box_10.remove('cat')
box_10.remove('plane')

# Move the mountain from Box 14 to Box 11
box_11.append(box_14.pop())

# Replace the belt with the laptop in Box 12
box_12.remove('belt')
box_12.append('laptop')

# Put the wire and the phone and the game into Box 7
box_7.extend(['wire', 'phone', 'game'])

# Move the scarf and the paint from Box 2 to Box 14
box_14.extend(box_2)
box_2.clear()

# Move the headphone from Box 0 to Box 5
box_5.append(box_0.pop(box_0.index('headphone')))

# Move the seaweed from Box 13 to Box 3
box_3.append(box_13.pop())

# Replace the storm with the river in Box 11
box_11.remove('storm')
box_11.append('river')

# Remove the key and the toaster from Box 1
box_1.remove('key')
box_1.remove('toaster')

# Put the shoes and the spoon and the bird into Box 2
box_2.extend(['shoes', 'spoon', 'bird'])

# Move the telescope and the river and the horse from Box 11 to Box 5
box_5.extend([box_11.pop(box_11.index('telescope')), box_11.pop(box_11.index('river')), box_11.pop(box_11.index('horse'))])

# Remove the shoes and the spoon from Box 2
box_2.remove('shoes')
box_2.remove('spoon')

# Swap the car in Box 13 with the lock in Box 9
box_13.remove('car')
box_13.append('lock')
box_9.remove('lock')
box_9.append('car')

# Swap the clock in Box 5 with the seaweed in Box 3
box_5.remove('clock')
box_5.append('seaweed')
box_3.remove('seaweed')
box_3.append('clock')

# Put the helmet and the table into Box 8
box_8.extend(['helmet', 'table'])

# Put the lipstick and the vase and the pants into Box 14
box_14.extend(['lipstick', 'vase', 'pants'])

# Swap the laptop in Box 12 with the scarf in Box 14
box_12.remove('laptop')
box_12.append('scarf')
box_14.remove('scarf')
box_14.append('laptop')

# Move the dice from Box 4 to Box 6
box_6.append(box_4.pop(box_4.index('dice')))

# Move the bird from Box 2 to Box 0
box_0.append(box_2.pop(box_2.index('bird')))

# Move the piano and the charger from Box 4 to Box 5
box_5.extend([box_4.pop(box_4.index('piano')), box_4.pop(box_4.index('charger'))])

# Swap the game in Box 7 with the elephant in Box 5
box_7.remove('game')
box_7.append('elephant')
box_5.remove('elephant')
box_5.append('game')

# Remove the scarf from Box 12
box_12.remove('scarf')

# Final state
print_boxes()
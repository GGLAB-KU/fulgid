box_0 = ['forest']
box_1 = ['shorts']
box_2 = ['microscope', 'mirror', 'earring', 'horse']
box_3 = ['key']
box_4 = ['usb', 'makeup']
box_5 = ['doll']
box_6 = ['basket']
box_7 = ['button', 'plate', 'pot', 'violin']
box_8 = ['flower', 'comet']
box_9 = ['puzzle', 'horn', 'beach']
box_10 = ['controller', 'console']
box_11 = ['headphone']
box_12 = ['mountain', 'note', 'storm']
box_13 = ['planet']
box_14 = ['towel', 'charger', 'table', 'coin', 'thread']

def print_box(box_name, box):
    print(f"Box {box_name}: {box}")

# Put the cow and the horn and the umbrella into Box 4
box_4.extend(['cow', 'horn', 'umbrella'])
print_box(4, box_4)

# Replace the rain with the key in Box 3
box_3 = ['key']
print_box(3, box_3)

# Move the horn and the cow from Box 4 to Box 5
box_5.extend(box_4.pop(box_4.index('horn')))
box_5.extend(box_4.pop(box_4.index('cow')))
print_box(4, box_4)
print_box(5, box_5)

# Swap the key in Box 3 with the basket in Box 6
box_3, box_6 = box_6, box_3
print_box(3, box_3)
print_box(6, box_6)

# Swap the key in Box 6 with the storm in Box 12
box_6, box_12 = box_12, box_6
print_box(6, box_6)
print_box(12, box_12)

# Swap the planet in Box 13 with the thread in Box 14
box_13, box_14 = box_14, box_13
print_box(13, box_13)
print_box(14, box_14)

# Put the wallet into Box 11
box_11.append('wallet')
print_box(11, box_11)

# Put the microwave into Box 10
box_10.append('microwave')
print_box(10, box_10)

# Remove the note and the key and the mountain from Box 12
box_12.remove('note')
box_12.remove('key')
box_12.remove('mountain')
print_box(12, box_12)

# Replace the doll and the cow with the shorts and the helmet in Box 5
box_5.remove('doll')
box_5.remove('cow')
box_5.extend(['shorts', 'helmet'])
print_box(5, box_5)

# Replace the storm with the wire in Box 6
box_6.remove('storm')
box_6.append('wire')
print_box(6, box_6)

# Remove the coin from Box 14
box_14.remove('coin')
print_box(14, box_14)

# Swap the usb in Box 4 with the basket in Box 3
box_4, box_3 = box_3, box_4
print_box(3, box_3)
print_box(4, box_4)

# Put the bear and the flute and the button into Box 7
box_7.extend(['bear', 'flute', 'button'])
print_box(7, box_7)

# Put the fridge and the key and the book into Box 2
box_2.extend(['fridge', 'key', 'book'])
print_box(2, box_2)

# Swap the wallet in Box 11 with the basket in Box 4
box_11, box_4 = box_4, box_11
print_box(4, box_4)
print_box(11, box_11)

# Move the planet from Box 14 to Box 2
box_2.append(box_14.pop(box_14.index('planet')))
print_box(2, box_2)
print_box(14, box_14)

# Move the horn and the shorts from Box 5 to Box 14
box_14.extend(box_5.pop(box_5.index('horn')))
box_14.extend(box_5.pop(box_5.index('shorts')))
print_box(5, box_5)
print_box(14, box_14)

# Remove the wire from Box 6
box_6.remove('wire')
print_box(6, box_6)

# Put the thunder and the necklace and the boat into Box 7
box_7.extend(['thunder', 'necklace', 'boat'])
print_box(7, box_7)

# Swap the beach in Box 9 with the helmet in Box 5
box_9, box_5 = box_5, box_9
print_box(5, box_5)
print_box(9, box_9)

# Swap the horn in Box 9 with the headphone in Box 11
box_9, box_11 = box_11, box_9
print_box(9, box_9)
print_box(11, box_11)
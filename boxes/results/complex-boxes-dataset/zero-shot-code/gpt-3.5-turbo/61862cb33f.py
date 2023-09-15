box_0 = ['vase', 'wallet']
box_1 = ['coin', 'puzzle', 'ship', 'bell', 'keyboard']
box_2 = ['console', 'scarf']
box_3 = []
box_4 = ['cup']
box_5 = []
box_6 = ['thread', 'dice', 'flute', 'grinder', 'leaf']
box_7 = ['grass', 'cat', 'gloves', 'comb', 'mirror']
box_8 = ['fish']
box_9 = []
box_10 = ['horn', 'magnet', 'usb', 'comet', 'crown']

def print_boxes():
    print("Box 0:", box_0)
    print("Box 1:", box_1)
    print("Box 2:", box_2)
    print("Box 3:", box_3)
    print("Box 4:", box_4)
    print("Box 5:", box_5)
    print("Box 6:", box_6)
    print("Box 7:", box_7)
    print("Box 8:", box_8)
    print("Box 9:", box_9)
    print("Box 10:", box_10)

# Move the console from Box 2 to Box 4
box_4.append(box_2.pop(box_2.index('console')))

# Move the fish from Box 8 to Box 2
box_2.append(box_8.pop(box_8.index('fish')))

# Remove the scarf and the fish from Box 2
box_2.remove('scarf')
box_2.remove('fish')

# Put the speaker and the ring into Box 5
box_5.extend(['speaker', 'ring'])

# Replace the ship and the puzzle and the coin with the desert and the lamp and the lipstick in Box 1
box_1.remove('ship')
box_1.remove('puzzle')
box_1.remove('coin')
box_1.extend(['desert', 'lamp', 'lipstick'])

# Move the ring and the speaker from Box 5 to Box 10
box_10.extend(box_5.pop(box_5.index('ring')))
box_10.extend(box_5.pop(box_5.index('speaker')))

# Put the pants into Box 0
box_0.append('pants')

# Swap the console in Box 4 with the magnet in Box 10
box_4.append(box_10.pop(box_10.index('magnet')))
box_10.append(box_4.pop(box_4.index('console')))

# Replace the gloves with the jacket in Box 7
box_7.remove('gloves')
box_7.append('jacket')

# Move the leaf and the grinder from Box 6 to Box 8
box_8.extend(box_6.pop(box_6.index('leaf')))
box_8.extend(box_6.pop(box_6.index('grinder')))

# Swap the horn in Box 10 with the leaf in Box 8
box_10.append(box_8.pop(box_8.index('leaf')))
box_8.append(box_10.pop(box_10.index('horn')))

# Put the violin into Box 5
box_5.append('violin')

# Swap the pants in Box 0 with the grass in Box 7
box_0.append(box_7.pop(box_7.index('grass')))
box_7.append('pants')

# Move the lamp from Box 1 to Box 8
box_8.append(box_1.pop(box_1.index('lamp')))

# Remove the violin from Box 5
box_5.remove('violin')

# Replace the wallet and the grass and the vase with the charger and the usb and the toothpaste in Box 0
box_0.remove('wallet')
box_0.remove('vase')
box_0.extend(['charger', 'usb', 'toothpaste'])

# Print the final state of the boxes
print_boxes()
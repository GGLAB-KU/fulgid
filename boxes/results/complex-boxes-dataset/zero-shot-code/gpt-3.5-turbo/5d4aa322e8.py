box_0 = ['blanket', 'glove', 'wire', 'motorcycle', 'boot']
box_1 = ['glasses', 'skirt', 'cat']
box_2 = ['thread', 'battery', 'fish', 'storm', 'sock']
box_3 = ['card', 'helmet', 'comet']
box_4 = ['key', 'starfish']
box_5 = ['toothbrush']
box_6 = ['star', 'lock', 'shelf', 'shampoo']
box_7 = []
box_8 = ['plate']
box_9 = ['bracelet', 'dolphin']
box_10 = ['oven']

print("Initial state:")
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

# Move the dolphin and the bracelet from Box 9 to Box 7
box_7.extend([box_9.pop(box_9.index('dolphin')), box_9.pop(box_9.index('bracelet'))])

# Remove the oven from Box 10
box_10.remove('oven')

# Move the comet and the helmet and the card from Box 3 to Box 4
box_4.extend([box_3.pop(box_3.index('comet')), box_3.pop(box_3.index('helmet')), box_3.pop(box_3.index('card'))])

# Put the pants and the thunder into Box 7
box_7.extend(['pants', 'thunder'])

# Empty Box 4
box_4 = []

# Move the plate from Box 8 to Box 6
box_6.append(box_8.pop(box_8.index('plate')))

# Move the bracelet from Box 7 to Box 1
box_1.append(box_7.pop(box_7.index('bracelet')))

# Remove the glasses and the bracelet and the skirt from Box 1
box_1.remove('glasses')
box_1.remove('skirt')
box_1.remove('bracelet')

# Put the telescope and the magnet and the earring into Box 2
box_2.extend(['telescope', 'magnet', 'earring'])

# Move the toothbrush from Box 5 to Box 4
box_4.append(box_5.pop(box_5.index('toothbrush')))

# Replace the toothbrush with the bell in Box 4
box_4.remove('toothbrush')
box_4.append('bell')

# Put the clock and the pot and the thread into Box 2
box_2.extend(['clock', 'pot', 'thread'])

# Move the pants and the thunder from Box 7 to Box 5
box_5.extend([box_7.pop(box_7.index('pants')), box_7.pop(box_7.index('thunder'))])

# Replace the bell with the towel in Box 4
box_4.remove('bell')
box_4.append('towel')

# Swap the dolphin in Box 7 with the towel in Box 4
box_7.append(box_4.pop(box_4.index('towel')))
box_4.append(box_7.pop(box_7.index('dolphin')))

# Replace the cat with the boot in Box 1
box_1.remove('cat')
box_1.append('boot')

# Replace the storm and the telescope and the clock with the sculpture and the tape and the horn in Box 2
box_2.remove('storm')
box_2.remove('telescope')
box_2.remove('clock')
box_2.extend(['sculpture', 'tape', 'horn'])

print("\nFinal state:")
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
box_0 = ['toy', 'rain', 'cow', 'pan', 'butterfly']
box_1 = ['perfume', 'necklace']
box_2 = ['shoes', 'brush', 'drum']
box_3 = ['plate']
box_4 = []
box_5 = ['moon', 'dog', 'boot', 'lion', 'mask']
box_6 = []
box_7 = ['belt', 'oven', 'coin', 'scissors', 'submarine']
box_8 = ['octopus', 'dolphin']

# Swap the cow in Box 0 with the drum in Box 2
box_0[box_0.index('cow')], box_2[box_2.index('drum')] = box_2[box_2.index('drum')], box_0[box_0.index('cow')]

# Replace the moon and the lion with the doll and the lightning in Box 5
box_5[box_5.index('moon')] = 'doll'
box_5[box_5.index('lion')] = 'lightning'

# Swap the perfume in Box 1 with the dog in Box 5
box_1[box_1.index('perfume')], box_5[box_5.index('dog')] = box_5[box_5.index('dog')], box_1[box_1.index('perfume')]

# Swap the brush in Box 2 with the necklace in Box 1
box_2[box_2.index('brush')], box_1[box_1.index('necklace')] = box_1[box_1.index('necklace')], box_2[box_2.index('brush')]

# Replace the submarine with the plane in Box 7
box_7[box_7.index('submarine')] = 'plane'

# Move the necklace and the shoes from Box 2 to Box 5
box_5.append(box_2.pop(box_2.index('necklace')))
box_5.append(box_2.pop(box_2.index('shoes')))

# Empty Box 7
box_7 = []

# Swap the boot in Box 5 with the plate in Box 3
box_5[box_5.index('boot')], box_3[box_3.index('plate')] = box_3[box_3.index('plate')], box_5[box_5.index('boot')]

# Move the cow from Box 2 to Box 7
box_7.append(box_2.pop(box_2.index('cow')))

# Move the dolphin and the octopus from Box 8 to Box 2
box_2.append(box_8.pop(box_8.index('dolphin')))
box_2.append(box_8.pop(box_8.index('octopus')))

# Remove the toy and the drum and the pan from Box 0
box_0.remove('toy')
box_0.remove('drum')
box_0.remove('pan')

# Empty Box 7
box_7 = []

# Move the brush from Box 1 to Box 0
box_0.append(box_1.pop(box_1.index('brush')))

# Move the boot from Box 3 to Box 7
box_7.append(box_3.pop(box_3.index('boot')))

# Print the final state of the boxes
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
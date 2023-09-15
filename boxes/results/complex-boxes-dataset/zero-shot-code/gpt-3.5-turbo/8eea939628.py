box_0 = ['basket', 'submarine', 'thunder', 'puzzle', 'rain']
box_1 = []
box_2 = ['umbrella', 'car', 'thread', 'drum']
box_3 = ['grinder']
box_4 = ['dolphin', 'perfume']
box_5 = ['soap', 'chair', 'toothbrush', 'motorcycle']
box_6 = ['helmet', 'tree', 'grass', 'shirt']
box_7 = []
box_8 = ['frame', 'bird', 'fridge']
box_9 = ['crown']
box_10 = ['sandals', 'note', 'mask', 'lamp']
box_11 = ['necklace', 'moon']
box_12 = ['shoe', 'vase', 'jungle']
box_13 = ['glove', 'pan', 'flower', 'ocean']
box_14 = ['island', 'pen', 'sculpture', 'bus', 'jacket']

# Put the cow into Box 12
box_12.append('cow')

# Replace the frame and the bird and the fridge with the rocket and the shark and the branch in Box 8
box_8 = ['rocket', 'shark', 'branch']

# Put the tie into Box 8
box_8.append('tie')

# Replace the perfume with the tie in Box 4
box_4.remove('perfume')
box_4.append('tie')

# Swap the drum in Box 2 with the crown in Box 9
box_2.remove('drum')
box_2.append('crown')
box_9.remove('crown')
box_9.append('drum')

# Move the sculpture from Box 14 to Box 8
box_14.remove('sculpture')
box_8.append('sculpture')

# Replace the necklace with the oven in Box 11
box_11.remove('necklace')
box_11.append('oven')

# Put the sun into Box 1
box_1.append('sun')

# Put the mask and the snow and the lock into Box 10
box_10.extend(['mask', 'snow', 'lock'])

# Put the ocean and the dress and the bowl into Box 14
box_14.extend(['ocean', 'dress', 'bowl'])

# Replace the helmet and the tree with the freezer and the bracelet in Box 6
box_6.remove('helmet')
box_6.remove('tree')
box_6.extend(['freezer', 'bracelet'])

# Swap the soap in Box 5 with the shelf in Box 1
box_5.remove('soap')
box_1.remove('shelf')
box_5.append('shelf')
box_1.append('soap')

# Swap the ocean in Box 14 with the grinder in Box 3
box_14.remove('ocean')
box_3.remove('grinder')
box_14.append('grinder')
box_3.append('ocean')

# Swap the vase in Box 12 with the ocean in Box 3
box_12.remove('vase')
box_3.remove('ocean')
box_12.append('ocean')
box_3.append('vase')

# Replace the oven with the speaker in Box 11
box_11.remove('oven')
box_11.append('speaker')

# Replace the drum with the star in Box 9
box_9.remove('drum')
box_9.append('star')

# Replace the chair and the toothbrush and the shelf with the makeup and the plate and the bicycle in Box 5
box_5.remove('chair')
box_5.remove('toothbrush')
box_1.remove('shelf')
box_5.extend(['makeup', 'plate', 'bicycle'])
box_1.extend(['chair', 'toothbrush', 'shelf'])

# Swap the moon in Box 11 with the shark in Box 8
box_11.remove('moon')
box_8.remove('shark')
box_11.append('shark')
box_8.append('moon')

# Replace the grass and the bracelet and the freezer with the plane and the table and the boat in Box 6
box_6.remove('grass')
box_6.remove('bracelet')
box_6.remove('freezer')
box_6.extend(['plane', 'table', 'boat'])

# Replace the motorcycle with the ship in Box 5
box_5.remove('motorcycle')
box_5.append('ship')

# Swap the car in Box 2 with the grinder in Box 14
box_2.remove('car')
box_14.remove('grinder')
box_2.append('grinder')
box_14.append('car')

# Swap the sun in Box 1 with the plate in Box 5
box_1.remove('sun')
box_5.remove('plate')
box_1.append('plate')
box_5.append('sun')

# Print the contents of each box
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
print("Box 11:", box_11)
print("Box 12:", box_12)
print("Box 13:", box_13)
print("Box 14:", box_14)
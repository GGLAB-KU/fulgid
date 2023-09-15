box_0 = ['pan', 'blender', 'candle', 'tree']
box_1 = ['meteor']
box_2 = ['telescope', 'comet', 'sun']
box_3 = ['ship', 'soap']
box_4 = ['swimsuit', 'frame', 'oven', 'shampoo']
box_5 = ['boot', 'clock', 'moon']
box_6 = ['plate', 'coat']
box_7 = ['brush']
box_8 = ['belt', 'lamp']
box_9 = ['flower']

# Remove the sun from Box 2
box_2.remove('sun')

# Swap the flower in Box 9 with the brush in Box 7
box_9.remove('flower')
box_7.remove('brush')
box_9.append('brush')
box_7.append('flower')

# Remove the meteor from Box 1
box_1.remove('meteor')

# Replace the clock with the shirt in Box 5
box_5.remove('clock')
box_5.append('shirt')

# Remove the plate from Box 6
box_6.remove('plate')

# Remove the ship from Box 3
box_3.remove('ship')

# Remove the oven and the shampoo from Box 4
box_4.remove('oven')
box_4.remove('shampoo')

# Move the brush from Box 9 to Box 1
box_9.remove('brush')
box_1.append('brush')

# Put the shark and the flute into Box 3
box_3.extend(['shark', 'flute'])

# Remove the shirt from Box 5
box_5.remove('shirt')

# Swap the moon in Box 5 with the coat in Box 6
box_5.remove('moon')
box_6.remove('coat')
box_5.append('coat')
box_6.append('moon')

# Swap the blender in Box 0 with the telescope in Box 2
box_0.remove('blender')
box_2.remove('telescope')
box_0.append('telescope')
box_2.append('blender')

# Put the elephant and the bowl into Box 1
box_1.extend(['elephant', 'bowl'])

# Swap the boot in Box 5 with the belt in Box 8
box_5.remove('boot')
box_8.remove('belt')
box_5.append('belt')
box_8.append('boot')

# Move the boot and the lamp from Box 8 to Box 1
box_8.remove('boot')
box_8.remove('lamp')
box_1.extend(['boot', 'lamp'])

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
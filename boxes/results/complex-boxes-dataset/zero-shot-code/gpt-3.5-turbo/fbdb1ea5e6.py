box_0 = ['speaker']
box_1 = ['coral', 'flower']
box_2 = ['tie', 'lipstick', 'battery', 'helmet', 'glasses']
box_3 = ['jacket', 'rocket']
box_4 = []
box_5 = []
box_6 = ['meteor', 'telescope', 'lock', 'pan']
box_7 = ['table', 'lightning']
box_8 = []
box_9 = ['crown', 'key', 'camera']
box_10 = ['pillow', 'snow']
box_11 = ['blanket', 'toaster', 'tiger', 'storm', 'plate']
box_12 = []

# Swap lightning in Box 7 with pan in Box 6
box_6.remove('pan')
box_7.remove('lightning')
box_6.append('lightning')
box_7.append('pan')

# Put controller into Box 10
box_10.append('controller')

# Put umbrella and glasses into Box 11
box_11.append('umbrella')
box_11.append('glasses')

# Swap table in Box 7 with storm in Box 11
box_7.remove('table')
box_11.remove('storm')
box_7.append('storm')
box_11.append('table')

# Empty Box 7
box_7 = []

# Replace crown, camera, and key with apple, train, and sun in Box 9
box_9.remove('crown')
box_9.remove('key')
box_9.remove('camera')
box_9.append('apple')
box_9.append('train')
box_9.append('sun')

# Swap flower in Box 1 with blanket in Box 11
box_1.remove('flower')
box_11.remove('blanket')
box_1.append('blanket')
box_11.append('flower')

# Move speaker from Box 0 to Box 7
box_0.remove('speaker')
box_7.append('speaker')

# Put gloves, drum, and tiger into Box 2
box_2.append('gloves')
box_2.append('drum')
box_2.append('tiger')

# Replace jacket and rocket with plane and cow in Box 3
box_3.remove('jacket')
box_3.remove('rocket')
box_3.append('plane')
box_3.append('cow')

# Replace plane with butterfly in Box 3
box_3.remove('plane')
box_3.append('butterfly')

# Move toaster from Box 11 to Box 4
box_11.remove('toaster')
box_4.append('toaster')

# Swap toaster in Box 4 with lipstick in Box 2
box_2.remove('lipstick')
box_4.remove('toaster')
box_2.append('toaster')
box_4.append('lipstick')

# Remove speaker from Box 7
box_7.remove('speaker')

# Put ship and tape into Box 12
box_12.append('ship')
box_12.append('tape')

# Put fork into Box 0
box_0.append('fork')

# Replace telescope and lock with pot and mirror in Box 6
box_6.remove('telescope')
box_6.remove('lock')
box_6.append('pot')
box_6.append('mirror')

# Remove sun and train from Box 9
box_9.remove('sun')
box_9.remove('train')

# Swap plate in Box 11 with ship in Box 12
box_11.remove('plate')
box_12.remove('ship')
box_11.append('ship')
box_12.append('plate')

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
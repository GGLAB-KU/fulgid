box_0 = ['umbrella', 'cup', 'grinder']
box_1 = ['toy', 'camera', 'toothpaste']
box_2 = ['puzzle', 'paint', 'lion', 'microwave']
box_3 = ['guitar', 'sun', 'brush']
box_4 = []
box_5 = ['frame', 'doll', 'earring', 'necklace']
box_6 = ['lock', 'table', 'bus', 'rocket']
box_7 = ['blender', 'makeup']
box_8 = ['console', 'lightning', 'tape', 'wig', 'sandals']

# Swap camera in Box 1 with bus in Box 6
box_1.remove('camera')
box_6.remove('bus')
box_1.append('bus')
box_6.append('camera')

# Remove brush, sun, and guitar from Box 3
box_3.remove('brush')
box_3.remove('sun')
box_3.remove('guitar')

# Remove lock, rocket, and table from Box 6
box_6.remove('lock')
box_6.remove('rocket')
box_6.remove('table')

# Replace paint and puzzle with belt and needle in Box 2
box_2.remove('paint')
box_2.remove('puzzle')
box_2.append('belt')
box_2.append('needle')

# Replace grinder with bus in Box 0
box_0.remove('grinder')
box_0.append('bus')

# Swap necklace in Box 5 with toy in Box 1
box_5.remove('necklace')
box_1.remove('toy')
box_5.append('toy')
box_1.append('necklace')

# Put elephant and bird into Box 0
box_0.append('elephant')
box_0.append('bird')

# Replace necklace, toothpaste, and bus with ship, console, and plane in Box 1
box_5.remove('necklace')
box_1.remove('toothpaste')
box_1.remove('bus')
box_5.append('ship')
box_1.append('console')
box_1.append('plane')

# Replace camera with bell in Box 6
box_6.remove('camera')
box_6.append('bell')

# Remove wig from Box 8
box_8.remove('wig')

# Put doll into Box 3
box_3.append('doll')

# Replace bird with lamp in Box 0
box_0.remove('bird')
box_0.append('lamp')

# Replace cup with button in Box 0
box_0.remove('cup')
box_0.append('button')

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
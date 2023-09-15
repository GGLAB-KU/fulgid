box_0 = ['river', 'mask']
box_1 = ['necklace', 'drum', 'hat']
box_2 = []
box_3 = ['crown', 'needle']
box_4 = ['boat', 'toaster', 'lamp', 'speaker']
box_5 = ['oven', 'plane', 'car']
box_6 = ['coat', 'camera', 'seaweed', 'leaf']
box_7 = ['shelf', 'sculpture', 'makeup', 'earring', 'spoon']
box_8 = []
box_9 = []
box_10 = []
box_11 = ['guitar', 'jacket']
box_12 = ['pants', 'snow']

# Remove necklace, drum, and hat from Box 1
box_1.remove('necklace')
box_1.remove('drum')
box_1.remove('hat')

# Replace crown and needle with lightning and basket in Box 3
box_3.remove('crown')
box_3.remove('needle')
box_3.append('lightning')
box_3.append('basket')

# Swap sculpture in Box 7 with pants in Box 12
box_7.remove('sculpture')
box_12.remove('pants')
box_7.append('pants')
box_12.append('sculpture')

# Swap earring in Box 7 with mask in Box 0
box_7.remove('earring')
box_0.remove('mask')
box_7.append('mask')
box_0.append('earring')

# Remove jacket and guitar from Box 11
box_11.remove('jacket')
box_11.remove('guitar')

# Swap speaker in Box 4 with lightning in Box 3
box_4.remove('speaker')
box_3.remove('lightning')
box_4.append('lightning')
box_3.append('speaker')

# Remove sculpture and snow from Box 12
box_12.remove('sculpture')
box_12.remove('snow')

# Remove seaweed from Box 6
box_6.remove('seaweed')

# Move pants, spoon, and makeup from Box 7 to Box 2
box_7.remove('pants')
box_7.remove('spoon')
box_7.remove('makeup')
box_2.append('pants')
box_2.append('spoon')
box_2.append('makeup')

# Move pants and spoon from Box 2 to Box 7
box_2.remove('pants')
box_2.remove('spoon')
box_7.append('pants')
box_7.append('spoon')

# Swap earring in Box 0 with mask in Box 7
box_0.remove('earring')
box_7.remove('mask')
box_0.append('mask')
box_7.append('earring')

# Move plane and oven from Box 5 to Box 8
box_5.remove('plane')
box_5.remove('oven')
box_8.append('plane')
box_8.append('oven')

# Put book into Box 6
box_6.append('book')

# Swap car in Box 5 with plane in Box 8
box_5.remove('car')
box_8.remove('plane')
box_5.append('plane')
box_8.append('car')

# Move boat and toaster from Box 4 to Box 3
box_4.remove('boat')
box_4.remove('toaster')
box_3.append('boat')
box_3.append('toaster')

# Move leaf from Box 6 to Box 7
box_6.remove('leaf')
box_7.append('leaf')

# Remove earring and spoon from Box 7
box_7.remove('earring')
box_7.remove('spoon')

# Put violin, gloves, and fork into Box 9
box_9.append('violin')
box_9.append('gloves')
box_9.append('fork')

# Replace book with shirt in Box 6
box_6.remove('book')
box_6.append('shirt')

# Replace coat and camera with swimsuit and pillow in Box 6
box_6.remove('coat')
box_6.remove('camera')
box_6.append('swimsuit')
box_6.append('pillow')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")
box_0 = []
box_1 = ['elephant', 'flute', 'boat']
box_2 = ['umbrella', 'lock', 'book']
box_3 = ['shoes', 'flower', 'train', 'grinder', 'desert']
box_4 = ['dog', 'headphone']
box_5 = []
box_6 = ['violin']
box_7 = ['swimsuit', 'crown', 'sandals']
box_8 = ['branch']
box_9 = ['tape', 'laptop', 'camera']

# Swap branch in Box 8 with dog in Box 4
box_8, box_4 = box_4, box_8

# Remove violin from Box 6
box_6 = []

# Put wallet and coat into Box 8
box_8.extend(['wallet', 'coat'])

# Put shoe and seaweed into Box 0
box_0.extend(['shoe', 'seaweed'])

# Remove tape from Box 9
box_9.remove('tape')

# Remove crown and swimsuit from Box 7
box_7.remove('crown')
box_7.remove('swimsuit')

# Replace desert and shoes with camera and blender in Box 3
box_3.remove('desert')
box_3.remove('shoes')
box_3.extend(['camera', 'blender'])

# Remove wallet, coat, and dog from Box 8
box_8.remove('wallet')
box_8.remove('coat')
box_8.remove('dog')

# Move boat, elephant, and flute from Box 1 to Box 2
box_2.extend(['boat', 'elephant', 'flute'])
box_1 = []

# Swap seaweed in Box 0 with camera in Box 9
box_0, box_9 = box_9, box_0

# Replace camera and blender with necklace and sun in Box 3
box_3.remove('camera')
box_3.remove('blender')
box_3.extend(['necklace', 'sun'])

# Put blender into Box 4
box_4.append('blender')

# Swap headphone in Box 4 with flute in Box 2
box_4, box_2 = box_2, box_4

# Remove sandals from Box 7
box_7.remove('sandals')

# Move blender, flute, and branch from Box 4 to Box 7
box_7.extend(['blender', 'flute', 'branch'])

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
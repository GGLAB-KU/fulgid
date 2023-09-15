box = {
    0: ['needle', 'key', 'shoe'],
    1: ['lamp'],
    2: [],
    3: [],
    4: ['pot', 'microwave', 'rain', 'cup', 'polish'],
    5: [],
    6: ['blender', 'toothbrush', 'guitar', 'wire', 'necklace'],
    7: ['coral', 'horn', 'razor'],
    8: ['starfish']
}

# Replace key, needle, and shoe with vase, pen, and sun in Box 0
box[0] = ['vase', 'pen', 'sun']

# Put thread into Box 2
box[2] = ['thread']

# Replace guitar with planet in Box 6
box[6].remove('guitar')
box[6].append('planet')

# Put toothpaste, dolphin, and hat into Box 1
box[1] += ['toothpaste', 'dolphin', 'hat']

# Move razor, coral, and horn from Box 7 to Box 6
box[6] += box[7]
box[7] = []

# Put toothpaste and phone into Box 0
box[0] += ['toothpaste', 'phone']

# Remove necklace from Box 6
box[6].remove('necklace')

# Swap vase in Box 0 with cup in Box 4
box[0], box[4] = box[4], box[0]
box[0].remove('vase')
box[4].remove('cup')
box[0].append('cup')
box[4].append('vase')

# Remove dolphin and lamp from Box 1
box[1].remove('dolphin')
box[1].remove('lamp')

# Move microwave and polish from Box 4 to Box 0
box[0] += ['microwave', 'polish']
box[4].remove('microwave')
box[4].remove('polish')

# Move pot from Box 4 to Box 1
box[1].append('pot')
box[4].remove('pot')

# Swap cup in Box 0 with starfish in Box 8
box[0], box[8] = box[8], box[0]
box[0].remove('cup')
box[8].remove('starfish')
box[0].append('starfish')
box[8].append('cup')

# Move rain and vase from Box 4 to Box 3
box[3] += ['rain', 'vase']
box[4].remove('rain')
box[4].remove('vase')

# Move wire, toothbrush, and blender from Box 6 to Box 4
box[4] += box[6]
box[6] = []

# Print the contents of each box
for i in range(9):
    print(f"Box {i}: {box[i]}")
box = {
    0: [],
    1: [],
    2: [],
    3: ['shorts', 'lock', 'swimsuit', 'flower', 'shelf'],
    4: ['basket', 'umbrella', 'flute'],
    5: ['helmet', 'truck'],
    6: [],
    7: ['bear', 'comet', 'wig'],
    8: ['pan'],
    9: ['horn', 'clock', 'game', 'seaweed'],
    10: ['razor', 'harmonica', 'coin'],
    11: ['phone', 'mixer'],
    12: []
}

# Remove harmonica, razor, and coin from Box 10
box[10].remove('harmonica')
box[10].remove('razor')
box[10].remove('coin')

# Put octopus, sandals, and horse into Box 0
box[0].extend(['octopus', 'sandals', 'horse'])

# Swap basket in Box 4 with flower in Box 3
box[4].remove('basket')
box[3].remove('flower')
box[4].append('flower')
box[3].append('basket')

# Move clock, seaweed, and horn from Box 9 to Box 5
box[5].extend(['clock', 'seaweed', 'horn'])
box[9].remove('clock')
box[9].remove('seaweed')
box[9].remove('horn')

# Empty Box 11
box[11] = []

# Put boot and phone into Box 4
box[4].extend(['boot', 'phone'])

# Move wig, comet, and bear from Box 7 to Box 9
box[9].extend(['wig', 'comet', 'bear'])
box[7].remove('wig')
box[7].remove('comet')
box[7].remove('bear')

# Swap game in Box 9 with basket in Box 3
box[9].remove('game')
box[3].remove('basket')
box[9].append('basket')
box[3].append('game')

# Put table into Box 12
box[12].append('table')

# Replace truck with sock in Box 5
box[5].remove('truck')
box[5].append('sock')

# Swap pan in Box 8 with wig in Box 9
box[8].remove('pan')
box[9].remove('wig')
box[8].append('wig')
box[9].append('pan')

# Move table from Box 12 to Box 0
box[0].append('table')
box[12].remove('table')

# Remove horn from Box 5
box[5].remove('horn')

# Move horse from Box 0 to Box 6
box[6].append('horse')
box[0].remove('horse')

# Move swimsuit, game, and shelf from Box 3 to Box 4
box[4].extend(['swimsuit', 'game', 'shelf'])
box[3].remove('swimsuit')
box[3].remove('game')
box[3].remove('shelf')

# Empty Box 8
box[8] = []

# Put elephant and tiger into Box 6
box[6].extend(['elephant', 'tiger'])

# Replace swimsuit with boat in Box 4
box[4].remove('swimsuit')
box[4].append('boat')

# Replace game and flute with horse and razor in Box 4
box[4].remove('game')
box[4].remove('flute')
box[4].append('horse')
box[4].append('razor')

# Put telescope into Box 4
box[4].append('telescope')

# Print the contents of each box
for i in range(13):
    print(f"Box {i}: {box[i]}")
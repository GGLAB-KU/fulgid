box = {
    0: ['storm', 'train', 'magnet', 'ring', 'bracelet'],
    1: [],
    2: ['plate', 'razor', 'pen', 'flower', 'shelf'],
    3: ['game', 'lipstick'],
    4: [],
    5: [],
    6: ['jungle', 'grinder', 'frame', 'table'],
    7: ['piano'],
    8: ['harmonica', 'blender', 'shoe', 'dog'],
    9: ['whistle', 'thunder'],
    10: [],
    11: ['camera', 'bell', 'speaker', 'pants', 'rain']
}

# Remove the shoe from Box 8
box[8].remove('shoe')

# Remove the dog and the harmonica and the blender from Box 8
box[8].remove('dog')
box[8].remove('harmonica')
box[8].remove('blender')

# Swap the plate in Box 2 with the table in Box 6
box[2].remove('plate')
box[6].remove('table')
box[2].append('table')
box[6].append('plate')

# Remove the rain from Box 11
box[11].remove('rain')

# Swap the piano in Box 7 with the razor in Box 2
box[7].remove('piano')
box[2].remove('razor')
box[7].append('razor')
box[2].append('piano')

# Replace the ring and the bracelet and the magnet with the branch and the blanket and the boot in Box 0
box[0].remove('ring')
box[0].remove('bracelet')
box[0].remove('magnet')
box[0].append('branch')
box[0].append('blanket')
box[0].append('boot')

# Swap the game in Box 3 with the pen in Box 2
box[3].remove('game')
box[2].remove('pen')
box[3].append('pen')
box[2].append('game')

# Move the lipstick and the pen from Box 3 to Box 9
box[3].remove('lipstick')
box[9].append('lipstick')
box[2].remove('pen')
box[9].append('pen')

# Move the jungle from Box 6 to Box 7
box[6].remove('jungle')
box[7].append('jungle')

# Move the plate and the grinder and the frame from Box 6 to Box 10
box[6].remove('plate')
box[6].remove('grinder')
box[6].remove('frame')
box[10].append('plate')
box[10].append('grinder')
box[10].append('frame')

# Move the jungle and the razor from Box 7 to Box 9
box[7].remove('jungle')
box[9].append('jungle')
box[2].remove('razor')
box[9].append('razor')

# Put the train into Box 3
box[3].append('train')

# Put the guitar and the phone and the desert into Box 10
box[10].append('guitar')
box[10].append('phone')
box[10].append('desert')

# Put the console and the frame and the bowl into Box 8
box[8].append('console')
box[8].append('frame')
box[8].append('bowl')

# Remove the pants and the camera from Box 11
box[11].remove('pants')
box[11].remove('camera')

# Put the coral and the lipstick and the grass into Box 0
box[0].append('coral')
box[0].append('lipstick')
box[0].append('grass')

# Remove the pen and the lipstick from Box 9
box[9].remove('pen')
box[9].remove('lipstick')

# Replace the whistle and the razor and the thunder with the controller and the pants and the crown in Box 9
box[9].remove('whistle')
box[9].remove('razor')
box[9].remove('thunder')
box[9].append('controller')
box[9].append('pants')
box[9].append('crown')

# Print the contents of each box
for i in range(12):
    print(f"Box {i}: {box[i]}")
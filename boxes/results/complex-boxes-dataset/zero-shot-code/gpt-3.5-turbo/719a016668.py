box_0 = ['lamp', 'shelf', 'motorcycle']
box_1 = ['soap']
box_2 = ['game', 'toy', 'wig']
box_3 = []
box_4 = ['moon', 'glasses', 'earring']
box_5 = ['needle', 'dog', 'paint', 'blender', 'freezer']
box_6 = ['keyboard', 'horse']
box_7 = ['magnet', 'coral', 'whistle', 'wire', 'guitar']
box_8 = ['seaweed', 'flower']
box_9 = []
box_10 = ['hat', 'cup', 'shoe', 'mask']

def print_boxes():
    boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]
    for i, box in enumerate(boxes):
        print(f"Box {i}: {box}")

# Swap the soap in Box 1 with the keyboard in Box 6
box_1.remove('soap')
box_6.remove('keyboard')
box_1.append('keyboard')
box_6.append('soap')

# Remove the blender and the paint and the freezer from Box 5
box_5.remove('blender')
box_5.remove('paint')
box_5.remove('freezer')

# Move the flower and the seaweed from Box 8 to Box 5
box_8.remove('flower')
box_8.remove('seaweed')
box_5.append('flower')
box_5.append('seaweed')

# Swap the soap in Box 6 with the cup in Box 10
box_6.remove('soap')
box_10.remove('cup')
box_6.append('cup')
box_10.append('soap')

# Put the ring into Box 8
box_8.append('ring')

# Swap the game in Box 2 with the keyboard in Box 1
box_2.remove('game')
box_1.remove('keyboard')
box_2.append('keyboard')
box_1.append('game')

# Swap the soap in Box 10 with the dog in Box 5
box_10.remove('soap')
box_5.remove('dog')
box_10.append('dog')
box_5.append('soap')

# Swap the ring in Box 8 with the toy in Box 2
box_8.remove('ring')
box_2.remove('toy')
box_8.append('toy')
box_2.append('ring')

# Swap the ring in Box 2 with the hat in Box 10
box_2.remove('ring')
box_10.remove('hat')
box_2.append('hat')
box_10.append('ring')

# Replace the soap and the flower and the needle with the mirror and the earring and the doll in Box 5
box_5.remove('soap')
box_5.remove('flower')
box_5.remove('needle')
box_5.append('mirror')
box_5.append('earring')
box_5.append('doll')

# Swap the toy in Box 8 with the cup in Box 6
box_8.remove('toy')
box_6.remove('cup')
box_8.append('cup')
box_6.append('toy')

# Swap the dog in Box 10 with the seaweed in Box 5
box_10.remove('dog')
box_5.remove('seaweed')
box_10.append('seaweed')
box_5.append('dog')

# Put the fridge into Box 10
box_10.append('fridge')

# Replace the whistle and the guitar with the jungle and the piano in Box 7
box_7.remove('whistle')
box_7.remove('guitar')
box_7.append('jungle')
box_7.append('piano')

# Replace the fridge and the mask and the ring with the scarf and the drum and the tree in Box 10
box_10.remove('fridge')
box_10.remove('mask')
box_10.remove('ring')
box_10.append('scarf')
box_10.append('drum')
box_10.append('tree')

# Move the lamp and the motorcycle from Box 0 to Box 2
box_0.remove('lamp')
box_0.remove('motorcycle')
box_2.append('lamp')
box_2.append('motorcycle')

print_boxes()
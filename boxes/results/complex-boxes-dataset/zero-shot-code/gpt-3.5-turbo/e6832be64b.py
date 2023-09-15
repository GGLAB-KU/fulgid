box_0 = []
box_1 = ['mask', 'desert', 'violin', 'rock', 'scarf']
box_2 = ['sandals', 'dog', 'coin']
box_3 = ['mixer', 'plate', 'cloud', 'dolphin', 'bowl']
box_4 = ['pants', 'thunder']
box_5 = ['boat']
box_6 = ['comb', 'comet']
box_7 = ['island', 'toy', 'chair']
box_8 = []
box_9 = ['seaweed', 'ocean', 'moon', 'storm']

# Swap the violin in Box 1 with the moon in Box 9
box_1.remove('violin')
box_9.remove('moon')
box_1.append('moon')
box_9.append('violin')

# Swap the island in Box 7 with the rock in Box 1
box_7.remove('island')
box_1.remove('rock')
box_7.append('rock')
box_1.append('island')

# Swap the mixer in Box 3 with the moon in Box 1
box_3.remove('mixer')
box_1.remove('moon')
box_3.append('moon')
box_1.append('mixer')

# Empty Box 2
box_2 = []

# Empty Box 1
box_1 = []

# Move the violin and the ocean from Box 9 to Box 8
box_9.remove('violin')
box_9.remove('ocean')
box_8 = ['violin', 'ocean']

# Remove the toy and the chair and the rock from Box 7
box_7.remove('toy')
box_7.remove('chair')
box_7.remove('rock')

# Empty Box 4
box_4 = []

# Move the boat from Box 5 to Box 2
box_5.remove('boat')
box_2.append('boat')

# Replace the boat with the headphone in Box 2
box_2.remove('boat')
box_2.append('headphone')

# Put the gloves into Box 6
box_6.append('gloves')

# Put the submarine and the thunder into Box 0
box_0 = ['submarine', 'thunder']

# Put the lion and the bus and the comb into Box 0
box_0.append('lion')
box_0.append('bus')
box_0.append('comb')

# Replace the lion and the submarine and the thunder with the tape and the lamp and the bracelet in Box 0
box_0.remove('lion')
box_0.remove('submarine')
box_0.remove('thunder')
box_0.append('tape')
box_0.append('lamp')
box_0.append('bracelet')

# Remove the dolphin and the moon and the cloud from Box 3
box_3.remove('dolphin')
box_3.remove('moon')
box_3.remove('cloud')

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
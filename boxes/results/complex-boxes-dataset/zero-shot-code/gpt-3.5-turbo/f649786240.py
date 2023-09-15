box_0 = ['comb', 'jungle']
box_1 = ['island', 'starfish', 'camera', 'branch']
box_2 = ['flower', 'boot', 'comet']
box_3 = ['skirt']
box_4 = ['polish', 'coat']
box_5 = ['shirt', 'guitar', 'pen', 'spoon']
box_6 = ['rock', 'bus', 'laptop']
box_7 = ['soap', 'umbrella', 'frame', 'charger', 'shelf']

# Swap bus in Box 6 with comb in Box 0
box_0.remove('comb')
box_6.remove('bus')
box_0.append('bus')
box_6.append('comb')

# Put dice into Box 0
box_0.append('dice')

# Put oven into Box 5
box_5.append('oven')

# Put charger, planet, and moon into Box 1
box_1.extend(['charger', 'planet', 'moon'])

# Move coat from Box 4 to Box 7
box_4.remove('coat')
box_7.append('coat')

# Move jungle, dice, and bus from Box 0 to Box 4
box_0.remove('jungle')
box_0.remove('dice')
box_4.extend(['jungle', 'dice', 'bus'])

# Replace skirt with note in Box 3
box_3.remove('skirt')
box_3.append('note')

# Put key, flute, and tape into Box 6
box_6.extend(['key', 'flute', 'tape'])

# Put shirt and lock into Box 4
box_4.extend(['shirt', 'lock'])

# Put wallet, bicycle, and headphone into Box 6
box_6.extend(['wallet', 'bicycle', 'headphone'])

# Swap note in Box 3 with moon in Box 1
box_1.remove('moon')
box_3.remove('note')
box_1.append('note')
box_3.append('moon')

# Put harmonica into Box 7
box_7.append('harmonica')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
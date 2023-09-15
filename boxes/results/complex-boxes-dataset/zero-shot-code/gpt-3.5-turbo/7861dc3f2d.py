box_0 = ['violin', 'watch', 'bird', 'magnet', 'drum']
box_1 = []
box_2 = ['horn', 'shark', 'dolphin', 'brush']
box_3 = ['hat', 'mixer', 'snow', 'fish', 'beach']
box_4 = ['lamp', 'whistle', 'blanket']
box_5 = ['boat', 'piano', 'helmet', 'bicycle']
box_6 = []
box_7 = ['shelf', 'vase', 'swimsuit', 'pillow']
box_8 = ['river', 'shoes', 'branch', 'submarine']
box_9 = ['pan', 'plate']
box_10 = ['motorcycle']

# Swap the shark in Box 2 with the mixer in Box 3
box_2.remove('shark')
box_3.remove('mixer')
box_2.append('mixer')
box_3.append('shark')

# Swap the pillow in Box 7 with the river in Box 8
box_7.remove('pillow')
box_8.remove('river')
box_7.append('river')
box_8.append('pillow')

# Move the hat and the snow from Box 3 to Box 0
box_3.remove('hat')
box_3.remove('snow')
box_0.append('hat')
box_0.append('snow')

# Move the bicycle and the piano and the helmet from Box 5 to Box 8
box_5.remove('bicycle')
box_5.remove('piano')
box_5.remove('helmet')
box_8.append('bicycle')
box_8.append('piano')
box_8.append('helmet')

# Swap the bird in Box 0 with the beach in Box 3
box_0.remove('bird')
box_3.remove('beach')
box_0.append('beach')
box_3.append('bird')

# Remove the pillow and the branch from Box 8
box_8.remove('pillow')
box_8.remove('branch')

# Move the vase and the river from Box 7 to Box 10
box_7.remove('vase')
box_8.remove('river')
box_10.append('vase')
box_10.append('river')

# Move the fish and the shark and the bird from Box 3 to Box 0
box_3.remove('fish')
box_3.remove('shark')
box_3.remove('bird')
box_0.append('fish')
box_0.append('shark')
box_0.append('bird')

# Put the dice and the coat and the fridge into Box 2
box_2.append('dice')
box_2.append('coat')
box_2.append('fridge')

# Swap the shelf in Box 7 with the dolphin in Box 2
box_7.remove('shelf')
box_2.remove('dolphin')
box_7.append('dolphin')
box_2.append('shelf')

# Remove the pan and the plate from Box 9
box_9.remove('pan')
box_9.remove('plate')

# Remove the dolphin from Box 7
box_7.remove('dolphin')

# Swap the brush in Box 2 with the lamp in Box 4
box_2.remove('brush')
box_4.remove('lamp')
box_2.append('lamp')
box_4.append('brush')

# Move the motorcycle from Box 10 to Box 8
box_10.remove('motorcycle')
box_8.append('motorcycle')

# Remove the mixer and the coat and the horn from Box 2
box_2.remove('mixer')
box_2.remove('coat')
box_2.remove('horn')

# Remove the whistle from Box 4
box_4.remove('whistle')

# Move the boat from Box 5 to Box 4
box_5.remove('boat')
box_4.append('boat')

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
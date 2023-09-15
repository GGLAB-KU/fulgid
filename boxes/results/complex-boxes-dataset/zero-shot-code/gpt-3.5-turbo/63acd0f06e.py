box_0 = ['lipstick', 'sock', 'needle']
box_1 = ['soap', 'scissors']
box_2 = ['cup', 'doll', 'whistle', 'swimsuit']
box_3 = ['vase', 'drum', 'toy']
box_4 = ['zipper', 'lock', 'ship', 'jungle']
box_5 = ['meteor', 'keyboard']
box_6 = ['thunder']
box_7 = ['octopus', 'watch']
box_8 = ['seaweed', 'umbrella']
box_9 = ['snow', 'bird', 'horn']
box_10 = ['table', 'jacket']

def print_boxes():
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

# Put the comet into Box 10
box_10.append('comet')

# Swap the soap in Box 1 with the toy in Box 3
box_1.remove('soap')
box_3.remove('toy')
box_1.append('toy')
box_3.append('soap')

# Remove the meteor and the keyboard from Box 5
box_5.remove('meteor')
box_5.remove('keyboard')

# Replace the ship with the beach in Box 4
box_4.remove('ship')
box_4.append('beach')

# Swap the needle in Box 0 with the jacket in Box 10
box_0.remove('needle')
box_10.remove('jacket')
box_0.append('jacket')
box_10.append('needle')

# Swap the sock in Box 0 with the umbrella in Box 8
box_0.remove('sock')
box_8.remove('umbrella')
box_0.append('umbrella')
box_8.append('sock')

# Swap the bird in Box 9 with the seaweed in Box 8
box_9.remove('bird')
box_8.remove('seaweed')
box_9.append('seaweed')
box_8.append('bird')

# Swap the toy in Box 1 with the drum in Box 3
box_1.remove('toy')
box_3.remove('drum')
box_1.append('drum')
box_3.append('toy')

# Swap the table in Box 10 with the octopus in Box 7
box_10.remove('table')
box_7.remove('octopus')
box_10.append('octopus')
box_7.append('table')

# Empty Box 2
box_2 = []

# Empty Box 10
box_10 = []

# Move the sock and the bird from Box 8 to Box 4
box_8.remove('sock')
box_8.remove('bird')
box_4.append('sock')
box_4.append('bird')

# Put the helmet into Box 7
box_7.append('helmet')

# Swap the horn in Box 9 with the drum in Box 1
box_9.remove('horn')
box_1.remove('drum')
box_9.append('drum')
box_1.append('horn')

# Swap the seaweed in Box 9 with the lipstick in Box 0
box_9.remove('seaweed')
box_0.remove('lipstick')
box_9.append('lipstick')
box_0.append('seaweed')

# Swap the table in Box 7 with the umbrella in Box 0
box_7.remove('table')
box_0.remove('umbrella')
box_7.append('umbrella')
box_0.append('table')

# Move the toy from Box 3 to Box 6
box_3.remove('toy')
box_6.append('toy')

print_boxes()
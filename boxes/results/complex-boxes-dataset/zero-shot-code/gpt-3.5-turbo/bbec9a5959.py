box_0 = []
box_1 = ['snow', 'cat', 'star']
box_2 = ['flute']
box_3 = ['whistle', 'horse', 'sandals']
box_4 = []
box_5 = ['lightning', 'magnet', 'shoes', 'seaweed', 'island']
box_6 = ['table']
box_7 = ['toothpaste', 'lion']
box_8 = ['headphone']
box_9 = ['shoe', 'leaf']
box_10 = ['cup', 'key', 'doll', 'lock']
box_11 = ['battery', 'charger', 'candle', 'necklace']
box_12 = ['bag', 'butterfly', 'horn']

# Swap the thread in Box 2 with the cup in Box 10
box_2.remove('thread')
box_10.append('thread')
box_10.remove('cup')
box_2.append('cup')

# Put the ring into Box 11
box_11.append('ring')

# Put the basket and the train and the river into Box 12
box_12.extend(['basket', 'train', 'river'])

# Put the paint into Box 11
box_11.append('paint')

# Swap the leaf in Box 9 with the key in Box 10
box_9.remove('leaf')
box_10.append('leaf')
box_10.remove('key')
box_9.append('key')

# Remove the lightning and the island and the shoes from Box 5
box_5.remove('lightning')
box_5.remove('island')
box_5.remove('shoes')

# Move the horse and the sandals and the whistle from Box 3 to Box 1
box_3.remove('horse')
box_1.append('horse')
box_3.remove('sandals')
box_1.append('sandals')
box_3.remove('whistle')
box_1.append('whistle')

# Swap the charger in Box 11 with the river in Box 12
box_11.remove('charger')
box_12.append('charger')
box_12.remove('river')
box_11.append('river')

# Remove the lock from Box 10
box_10.remove('lock')

# Move the cup from Box 2 to Box 11
box_2.remove('cup')
box_11.append('cup')

# Swap the flute in Box 2 with the headphone in Box 8
box_2.remove('flute')
box_8.append('flute')
box_8.remove('headphone')
box_2.append('headphone')

# Remove the basket and the butterfly from Box 12
box_12.remove('basket')
box_12.remove('butterfly')

# Swap the whistle in Box 1 with the seaweed in Box 5
box_1.remove('whistle')
box_5.append('whistle')
box_5.remove('seaweed')
box_1.append('seaweed')

# Remove the table from Box 6
box_6.remove('table')

# Move the whistle and the magnet from Box 5 to Box 0
box_5.remove('whistle')
box_0.append('whistle')
box_5.remove('magnet')
box_0.append('magnet')

# Put the skirt and the polish and the snow into Box 11
box_11.extend(['skirt', 'polish', 'snow'])

# Move the leaf and the thread and the doll from Box 10 to Box 12
box_10.remove('leaf')
box_12.append('leaf')
box_10.remove('thread')
box_12.append('thread')
box_10.remove('doll')
box_12.append('doll')

# Remove the toothpaste and the lion from Box 7
box_7.remove('toothpaste')
box_7.remove('lion')

# Swap the flute in Box 8 with the shoe in Box 9
box_8.remove('flute')
box_9.append('flute')
box_9.remove('shoe')
box_8.append('shoe')

# Put the hat and the star into Box 0
box_0.extend(['hat', 'star'])

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
print("Box 11:", box_11)
print("Box 12:", box_12)
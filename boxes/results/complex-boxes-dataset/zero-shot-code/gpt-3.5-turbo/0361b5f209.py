box_0 = ['lightning', 'lipstick', 'harmonica', 'cup']
box_1 = ['submarine', 'jungle', 'train', 'comet', 'microwave']
box_2 = ['shorts', 'doll']
box_3 = ['gloves', 'tie', 'sun']
box_4 = ['toothbrush', 'vase', 'sculpture']
box_5 = ['laptop', 'crown', 'moon', 'bell']
box_6 = ['watch', 'book', 'snow', 'cat', 'storm']
box_7 = ['blender']
box_8 = ['starfish', 'basket', 'skirt', 'camera']
box_9 = ['button', 'fork', 'bear', 'horn', 'tape']
box_10 = ['paint', 'cow', 'river', 'battery']

# Remove gloves, tie, and sun from Box 3
box_3.remove('gloves')
box_3.remove('tie')
box_3.remove('sun')

# Put oven and island into Box 2
box_2.append('oven')
box_2.append('island')

# Replace lightning with train in Box 0
box_0.remove('lightning')
box_0.append('train')

# Move river, paint, and cow from Box 10 to Box 8
box_8.extend(['river', 'paint', 'cow'])
box_10.remove('river')
box_10.remove('paint')
box_10.remove('cow')

# Remove blender from Box 7
box_7.remove('blender')

# Swap cup in Box 0 with paint in Box 8
box_0.remove('cup')
box_8.remove('paint')
box_0.append('paint')
box_8.append('cup')

# Swap horn in Box 9 with paint in Box 0
box_9.remove('horn')
box_0.remove('paint')
box_9.append('paint')
box_0.append('horn')

# Put telescope into Box 0
box_0.append('telescope')

# Put doll into Box 9
box_9.append('doll')

# Put boot and butterfly into Box 0
box_0.extend(['boot', 'butterfly'])

# Put toaster into Box 0
box_0.append('toaster')

# Put chair and comb into Box 8
box_8.extend(['chair', 'comb'])

# Put leaf and bowl into Box 9
box_9.extend(['leaf', 'bowl'])

# Replace bell, crown, and laptop with thread, razor, and train in Box 5
box_5.remove('bell')
box_5.remove('crown')
box_5.remove('laptop')
box_5.extend(['thread', 'razor', 'train'])

# Swap doll in Box 2 with toothbrush in Box 4
box_2.remove('doll')
box_4.remove('toothbrush')
box_2.append('toothbrush')
box_4.append('doll')

# Move watch and book from Box 6 to Box 3
box_6.remove('watch')
box_6.remove('book')
box_3.extend(['watch', 'book'])

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
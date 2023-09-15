box_0 = ['apple', 'watch', 'frame', 'pan', 'key']
box_1 = ['doll', 'tape', 'polish', 'cup']
box_2 = ['pen', 'toy']
box_3 = []
box_4 = ['console']
box_5 = ['rain']
box_6 = ['oven', 'phone']
box_7 = ['controller', 'bicycle', 'thread', 'pillow']
box_8 = ['shoes', 'scissors', 'rocket', 'butterfly']
box_9 = ['makeup', 'belt', 'charger']
box_10 = ['laptop', 'ocean', 'ring']
box_11 = []
box_12 = ['comet', 'moon']
box_13 = ['tiger', 'cloud', 'meteor', 'fridge', 'mountain']

box_9.remove('charger')
box_2.remove('pen')
box_2.remove('toy')
box_10[box_10.index('ocean')] = 'belt'
box_9.extend(['paint', 'pillow', 'table'])
box_10[box_10.index('belt')] = 'fridge'
box_10[box_10.index('laptop')] = 'dog'
box_10[box_10.index('ring')] = 'comb'
box_4.append('polish')
box_13.remove('fridge')
box_13.remove('mountain')
box_0.extend(['fridge', 'mountain'])
box_7.extend(['speaker', 'umbrella'])
box_6.append('harmonica')
box_8.append('boat')
box_4.remove('polish')
box_4.remove('console')
box_3.append('console')
box_3[box_3.index('console')] = 'butterfly'
box_9[box_9.index('ocean')] = 'shoes'
box_9[box_9.index('paint')] = 'needle'
box_1.remove('tape')
box_1.remove('cup')
box_1.remove('doll')
box_4.extend(['tape', 'cup', 'doll'])
box_0[box_0.index('mountain')] = 'boat'
box_0.remove('apple')
box_5.extend(['cup', 'tape', 'doll'])
box_7.extend(['boat', 'pan', 'seaweed'])
box_10[box_10.index('dog')] = 'chair'
box_10[box_10.index('fridge')] = 'car'
box_1.extend(['camera', 'makeup', 'elephant'])
box_0.extend(['pan', 'key'])
  
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
print("Box 13:", box_13)
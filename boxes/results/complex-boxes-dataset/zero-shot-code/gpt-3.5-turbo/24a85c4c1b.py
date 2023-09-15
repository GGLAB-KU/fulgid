box_0 = ['razor', 'zipper', 'whistle']
box_1 = []
box_2 = ['coin', 'coat', 'branch', 'note', 'spoon']
box_3 = []
box_4 = ['keyboard', 'game', 'blender', 'grinder']
box_5 = ['hat', 'toy', 'dice', 'thunder', 'makeup', 'thread', 'headphone']
box_6 = ['sculpture', 'gloves', 'beach', 'jacket', 'bus']
box_7 = ['necklace', 'mirror', 'polish', 'sock']
box_8 = ['crown', 'controller']
box_9 = ['pan', 'book']
box_10 = ['candle', 'truck', 'island', 'lion', 'telescope']

box_5.extend(['thread', 'headphone'])
box_7[1] = 'branch'
box_5[6] = 'controller'
box_8[1] = 'thunder'
box_2[1] = 'sculpture'
box_6[2] = 'coat'
box_9.extend(['thread', 'dice', 'headphone'])
box_10.remove('telescope')
box_10.remove('lion')
box_10.remove('island')
box_7.extend(['towel', 'dress'])
box_9[0] = 'rocket'
box_9[1] = 'whistle'
box_9[2] = 'headphone'
box_6.remove('coat')
box_6.remove('beach')
box_8[0] = 'gloves'
box_8.append('comet')
box_8.clear()
box_5.remove('headphone')
box_10.extend(['shirt', 'bowl', 'bell'])
box_0.clear()
box_2.append('thunder')

boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]

for i, box in enumerate(boxes):
    print(f"Box {i}: {box}")
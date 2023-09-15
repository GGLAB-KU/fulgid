box_0 = ['cow', 'desert', 'book', 'storm', 'razor']
box_1 = ['mountain', 'earring', 'pot', 'lamp', 'mixer']
box_2 = ['moon', 'plane', 'puzzle', 'toy', 'phone']
box_3 = ['camera', 'river', 'horse', 'doll', 'bicycle']
box_4 = ['pants', 'whistle', 'bracelet', 'harmonica', 'shoes']
box_5 = ['card', 'cloud', 'comb', 'jacket', 'bus']
box_6 = ['microwave', 'shirt']
box_7 = ['bear', 'basket', 'lightning', 'chair']
box_8 = ['truck', 'keyboard']
box_9 = []
box_10 = []
box_11 = ['blanket', 'spoon']
box_12 = ['scarf', 'submarine', 'soap', 'pan', 'lipstick']

box_4.remove('pants')
box_4.remove('harmonica')
box_4.remove('shoes')
box_4.append('pen')
box_4.append('fish')
box_4.append('motorcycle')

box_12.remove('submarine')
box_11.remove('spoon')
box_12.append('spoon')
box_11.append('submarine')

box_0.remove('book')
box_0.remove('cow')
box_0.append('umbrella')
box_0.append('coat')

box_3.remove('horse')
box_3.remove('river')

box_4.remove('pen')
box_4.append('tiger')

box_6.append('telescope')
box_6.append('sculpture')

box_8.remove('truck')
box_8.remove('keyboard')

box_1.remove('mountain')
box_1.remove('earring')
box_1.append('camera')
box_1.append('polish')

box_6.remove('shirt')
box_6.remove('microwave')
box_6.remove('sculpture')

box_5.remove('jacket')
box_5.remove('cloud')
box_5.remove('card')
box_5.append('telescope')
box_5.append('sculpture')

box_7.remove('lightning')

box_6.remove('telescope')
box_5.append('telescope')

box_3.remove('bicycle')

box_5.remove('fish')
box_5.remove('bus')
box_5.remove('telescope')

box_3.remove('camera')
box_6.append('camera')

box_0.append('telescope')
box_0.append('planet')

box_5.append('game')

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
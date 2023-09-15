box_0 = []
box_1 = []
box_2 = ['puzzle']
box_3 = []
box_4 = ['pillow', 'pot', 'basket']
box_5 = ['bowl']
box_6 = ['button', 'cloud', 'hat', 'sandals']

box_0.extend(['whistle', 'jacket'])
box_2.remove('puzzle')
box_5.remove('bowl')
box_2.append('bowl')
box_0.remove('whistle')
box_0.append('bowl')
box_5.remove('jacket')
box_5.append('puzzle')
box_4.extend(['paint', 'ship'])
box_2.remove('whistle')
box_4.remove('pillow')
box_4.append('whistle')
box_4.extend(['razor', 'gloves', 'grinder'])
box_0.clear()
box_6.remove('button')
box_6.remove('cloud')
box_6.remove('hat')
box_3.extend(['sandals'])
box_5.remove('jacket')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
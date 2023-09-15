box_0 = ['butterfly']
box_1 = ['violin', 'star']
box_2 = ['grinder', 'shoes', 'blender']
box_3 = ['lock']
box_4 = ['oven', 'sock', 'swimsuit']
box_5 = ['bicycle', 'crown', 'pillow', 'desert', 'mountain']
box_6 = ['apple', 'shorts', 'sculpture', 'boot']
box_7 = ['sandals', 'fridge']
box_8 = ['game', 'coin', 'elephant']
box_9 = ['candle', 'boat', 'tape']
box_10 = ['belt']
box_11 = ['rock', 'toaster']

box_1.remove('star')
box_3.remove('lock')
box_11.remove('rock')
box_11.remove('toaster')
box_1.remove('violin')
box_1.remove('makeup')
box_7.append('apple')
box_4.extend(['lion', 'comet', 'seaweed'])
box_7.remove('sandals')
box_3.remove('butterfly')
box_5.remove('mountain')
box_2.remove('shoes')
box_5.extend(['grinder', 'blender'])
box_5.remove('desert')
box_5.remove('pillow')
box_5.extend(['boot', 'snow'])
box_5.remove('boot')
box_5.remove('grinder')
box_5.extend(['table', 'ring'])
box_3.append('plane')
box_8.remove('coin')
box_6.remove('boot')
box_8.append('coin')
box_7.append('brush')
box_7.remove('fridge')
box_6.append('fridge')
box_2.remove('mountain')
box_8.append('mountain')
box_10.append('piano')

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
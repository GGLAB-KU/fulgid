box_0 = ['comb', 'belt', 'lock']
box_1 = ['game', 'pillow', 'violin']
box_2 = ['bus']
box_3 = ['toothpaste', 'butterfly', 'car', 'dress', 'beach']
box_4 = []
box_5 = []
box_6 = ['console', 'planet', 'fish', 'cat']
box_7 = ['button', 'fork']
box_8 = ['ocean', 'charger', 'lightning', 'mirror']
box_9 = ['gloves', 'pants', 'flower', 'branch', 'submarine']
box_10 = ['bracelet', 'drum', 'island', 'lion']
box_11 = ['skirt', 'harmonica', 'river']
box_12 = ['speaker', 'jacket', 'truck']
box_13 = ['glove']
box_14 = ['piano', 'polish', 'thread', 'seaweed', 'horse']

box_8.remove('ocean')
box_8.remove('charger')
box_8.remove('mirror')
box_2.remove('bus')
box_13.append('bus')
box_14.remove('piano')
box_14.append('controller')
box_12.remove('jacket')
box_6.remove('planet')
box_6.remove('console')
box_6.remove('cat')
box_8.extend(['jungle', 'sun', 'river'])
box_14.remove('thread')
box_14.remove('polish')
box_0.remove('lock')
box_13.append('lock')
box_12.remove('speaker')
box_12.remove('truck')
box_2.extend(['speaker', 'truck'])
box_7.remove('button')
box_7.append('river')
box_1.remove('pillow')
box_14.remove('seaweed')
box_14.append('pillow')
box_5.extend(['gloves', 'dolphin'])
box_14.extend(['puzzle', 'gloves'])
box_5.remove('gloves')
box_5.remove('dolphin')
box_5.extend(['book', 'pan'])
box_10.extend(['keyboard', 'towel', 'frame'])
box_1.remove('seaweed')
box_9.append('seaweed')
box_9.remove('pants')
box_9.remove('submarine')
box_9.extend(['soap', 'lightning'])
box_13.extend(['camera', 'plate'])
box_8.remove('sun')
box_8.remove('lightning')
box_0.remove('glove')
box_0.append('pan')
box_5.append('forest')
box_2.remove('speaker')
box_2.append('sun')

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
print("Box 14:", box_14)
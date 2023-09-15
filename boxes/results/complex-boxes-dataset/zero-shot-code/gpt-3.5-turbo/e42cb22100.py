box_0 = ['coral', 'scarf', 'apple']
box_1 = ['skirt', 'ring', 'note', 'keyboard', 'wig']
box_2 = []
box_3 = ['jacket', 'paint', 'swimsuit', 'horse']
box_4 = ['comb', 'glasses']
box_5 = ['puzzle']
box_6 = ['dress']
box_7 = ['pants', 'pot', 'shark']
box_8 = ['desert', 'button', 'polish', 'river']
box_9 = ['coin', 'sculpture', 'rock']
box_10 = ['table', 'toaster', 'elephant', 'snow']
box_11 = ['watch']
box_12 = ['storm', 'brush', 'bicycle', 'cat', 'bird']

box_0.remove('apple')
box_0.remove('coral')
box_0.append('mask')

box_7.extend(['telescope', 'bowl', 'ship'])
box_7.remove('pot')

box_9.remove('bicycle')
box_9.append('bicycle')

box_1.remove('note')
box_1.remove('keyboard')
box_1.remove('ring')
box_1.extend(['motorcycle', 'mirror', 'thunder'])

box_2.extend(['brush', 'storm', 'bird'])
box_6.clear()

box_3.remove('paint')
box_3.remove('jacket')
box_3.remove('horse')
box_12.extend(['paint', 'jacket', 'horse'])

box_9.remove('sculpture')
box_9.remove('bicycle')
box_10.extend(['sculpture', 'bicycle'])

box_7.remove('pants')
box_1.remove('thunder')
box_1.remove('motorcycle')
box_1.remove('wig')
box_12.extend(['thunder', 'motorcycle', 'wig'])

box_5.remove('puzzle')
box_2.append('makeup')

box_9.remove('rock')
box_9.remove('coin')
box_0.extend(['rock', 'coin'])

box_8.remove('button')
box_8.append('toy')

box_1.append('beach')

box_0.remove('rock')
box_0.remove('mask')
box_12.extend(['harmonica', 'wallet'])

box_1.remove('mirror')
box_8.append('mirror')

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
box0 = []
box1 = ['thread', 'usb', 'comet']
box2 = ['perfume']
box3 = ['game', 'planet', 'phone', 'leaf']
box4 = ['bear']

box4 = []

box4.extend(box3.pop(box3.index('leaf')))
box4.extend(box3.pop(box3.index('game')))
box4.extend(box3.pop(box3.index('planet')))

box3 = ['car', 'pot', 'star']

box1[box1.index('perfume')] = box2.pop(box2.index('perfume'))

box3[box3.index('car')] = 'pan'
box3[box3.index('phone')] = 'bicycle'
box3[box3.index('star')] = 'brush'

box2.extend(box1.pop(box1.index('usb')))
box2.extend(box1.pop(box1.index('perfume')))
box2.extend(box1.pop(box1.index('comet')))

box0.extend(box3.pop(box3.index('pan')))
box0.extend(box3.pop(box3.index('brush')))
box0.extend(box3.pop(box3.index('bicycle')))

box3.extend(box0.pop(box0.index('pan')))
box3.extend(box0.pop(box0.index('brush')))
box3.extend(box0.pop(box0.index('bicycle')))

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
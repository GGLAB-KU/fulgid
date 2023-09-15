box0 = ['tiger', 'whistle']
box1 = ['crown', 'tie', 'planet', 'lamp']
box2 = ['shark', 'bag', 'shirt', 'battery']
box3 = ['fish', 'helmet', 'lightning', 'wig', 'lipstick']
box4 = ['ocean']
box5 = ['candle']
box6 = ['coral', 'mask', 'flute', 'ship']

box4 = []

box2[box2.index('battery')] = 'tie'
box1[box1.index('tie')] = 'battery'

box5.extend(['battery', 'rocket', 'book'])

box3.append(box1.pop(box1.index('planet')))

box6.remove('mask')
box6.remove('ship')

box6[box6.index('flute')] = 'headphone'

box3.extend(['apple', 'sun', 'seaweed'])

box6.remove('headphone')
box6.remove('coral')

box3.extend(box1.pop(box1.index('lamp')))
box3.extend(box1.pop(box1.index('crown')))

box4.extend(box2.pop(box2.index('tie')))
box4.extend(box2.pop(box2.index('bag')))

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)
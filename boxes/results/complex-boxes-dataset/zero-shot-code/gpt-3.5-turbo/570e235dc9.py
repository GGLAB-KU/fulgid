box0 = []
box1 = ['ocean', 'pan']
box2 = ['wallet', 'microscope', 'scissors', 'sandals', 'octopus']
box3 = []
box4 = ['shorts', 'skirt', 'rain', 'note', 'game']
box5 = ['needle', 'candle']

box4.append('candle')
box4.extend(['apple', 'piano', 'dog'])
box2[2:4] = ['shirt', 'usb']
box5.append('microwave')
box2.extend(['jacket', 'forest'])
box3.extend([box5.pop(1), box5.pop(0)])
box3 = []
box5, box2[4] = box2[4], box5
box2.remove('jacket')

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
box0 = []
box1 = ['coat', 'polish']
box2 = []
box3 = ['mask', 'planet', 'lipstick', 'horse', 'zipper']
box4 = ['flower', 'dice', 'table', 'grinder', 'clock']

box4.remove('clock')
box4.remove('grinder')
box4.remove('table')

box2.append('lipstick')
box2.append('zipper')
box3.remove('lipstick')
box3.remove('zipper')

box4.remove('flower')
box4.remove('dice')
box4.append('skirt')
box4.append('pants')

box1.remove('polish')
box4.remove('pants')
box1.append('pants')
box4.append('polish')

box4.remove('polish')
box4.remove('skirt')
box4.append('shark')
box4.append('sculpture')

box1.remove('coat')
box2.remove('zipper')
box1.append('zipper')
box2.append('coat')

box4 = []

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
box0 = ['comet', 'comb', 'tie', 'sandals']
box1 = ['note']
box2 = ['coat', 'bird']
box3 = ['tree', 'lightning', 'bicycle']
box4 = ['truck']

box4.extend(['apple', 'forest', 'earring'])
box0.extend(['meteor', 'seaweed'])
box0.extend(['apple', 'butterfly', 'pillow'])
box1.remove('note')
box4[box4.index('apple')], box0[box0.index('butterfly')] = box0[box0.index('butterfly')], box4[box4.index('apple')]
box4.append(box0.pop(box0.index('sandals')))
box1.extend([box0.pop(box0.index('apple')), box0.pop(box0.index('seaweed')), box0.pop(box0.index('tie'))])
box0.remove('comet')

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
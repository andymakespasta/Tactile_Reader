import json

max_pattern_length = 8
width = 5 #0~4
height = 4 #0~3

#find neighbors, returning 8 neighbors, 5 if side, 3 if edge
def find_neighbors(me):
    list = [] 
    if me[0]>0: #left side
        list.append( [me[0]-1, me[1]] )
        if me[1]>0:
            list.append( [me[0]-1, me[1]-1] )
        if me[1]<height-1:
            list.append( [me[0]-1, me[1]+1] )

    if me[0]<width-1: #right side
        list.append( [me[0]+1, me[1]] )
        if me[1]>0:
            list.append( [me[0]+1, me[1]-1] )
        if me[1]<height-1:
            list.append( [me[0]+1, me[1]+1] )

    if me[1]>0:
        list.append( [me[0], me[1]-1] )
    if me[1]<height-1:
        list.append( [me[0], me[1]+1] )

    return list

#recursively generate all possible patterns
def make_pattern(partial_pattern):
    print(partial_pattern)
    if len(partial_pattern) >= max_pattern_length:
        f.write(json.dumps(partial_pattern, separators=(',', ': ')))
        f.write(",\n ")
    else:
        for possible_next in find_neighbors(partial_pattern[-1]):
            if not(possible_next in partial_pattern):
                part_pattern_plus = partial_pattern[:] #pass by value not reference
                part_pattern_plus.append(possible_next)
                make_pattern(part_pattern_plus)


f = open('weak_dir_patterns.json','w')
f.write("[")


make_pattern([[0,0]]) 
make_pattern([[1,0]]) 
make_pattern([[2,0]]) 
make_pattern([[3,0]]) 
make_pattern([[4,0]])
make_pattern([[4,1]]) 
make_pattern([[4,2]]) 
make_pattern([[4,3]])
make_pattern([[3,3]]) 
make_pattern([[2,3]])
make_pattern([[1,3]])
make_pattern([[0,3]])
make_pattern([[0,2]])
make_pattern([[0,1]])
f.seek(f.tell()-4,0)#removes last comma#
f.write("]")
f.close()
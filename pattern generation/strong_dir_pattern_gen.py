import json

max_pattern_length = 8
allow_short_corner_ends = True
width = 5 #0~4
height = 4 #0~3

#find neighbors, returning 9, neighbor + self
def find_neighborhood(me):
    list = []
    list.append( [me[0]-1, me[1]-1] )
    list.append( [me[0]-1, me[1]] )
    list.append( [me[0]-1, me[1]+1] )
    list.append( [me[0], me[1]-1] )
    list.append( [me[0], me[1]] )
    list.append( [me[0], me[1]+1] )
    list.append( [me[0]+1, me[1]-1] )
    list.append( [me[0]+1, me[1]] )
    list.append( [me[0]+1, me[1]+1] )
    return list

#remove all points in list out of bounds
def remove_out_bounds(list): #passes by reference, wow, much pythonic
    kill_list=[]
    for point in list:
        if point[0]<0 or point[0]>=width or point[1]<0 or point[1]>=height:
            kill_list.append(point)
    for point in kill_list:
        list.remove(point)
    return list

#recursively generate all possible patterns
def make_pattern(partial_pattern):
    print(partial_pattern)
    if len(partial_pattern) >= max_pattern_length:
        f.write(json.dumps(partial_pattern, separators=(',', ': ')))
        f.write(",\n ")
    elif len(partial_pattern) == 1:
        for possible_next in remove_out_bounds(find_neighborhood(partial_pattern[0])):
            if (possible_next != partial_pattern[0]):
                part_pattern_plus = partial_pattern[:] #pass by value not reference
                part_pattern_plus.append(possible_next)
                make_pattern(part_pattern_plus)
    else:
        next_center = [partial_pattern[-1][0]*2-partial_pattern[-2][0], 
                       partial_pattern[-1][1]*2-partial_pattern[-2][1]]
        edge = True
        for possible_next in remove_out_bounds(find_neighborhood(partial_pattern[-1])):
            if (possible_next in find_neighborhood(next_center)) :
                if not(possible_next in find_neighborhood(partial_pattern[-2])):
                    part_pattern_plus = partial_pattern[:] #pass by value not reference
                    part_pattern_plus.append(possible_next)
                    make_pattern(part_pattern_plus)
                    edge = False 
        if edge == True:
            corner = True
            for possible_next in remove_out_bounds(find_neighborhood(partial_pattern[-1])):
                if (possible_next in find_neighborhood(next_center)) and (possible_next != partial_pattern[-1]):
                    part_pattern_plus = partial_pattern[:] #pass by value not reference
                    part_pattern_plus.append(possible_next)
                    make_pattern(part_pattern_plus)
                    corner = False
            if corner == True:
                print("corner!")
                if allow_short_corner_ends == True:
                    f.write(json.dumps(partial_pattern, separators=(',', ': ')))
                    f.write(",\n ")

        




f = open('strong_dir_patterns.json','w')
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
#all patterns that start at [x,x]


f.seek(f.tell()-4,0)#removes last comma#
f.write("]")
f.close()
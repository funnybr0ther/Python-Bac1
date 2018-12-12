def matrix_for_traces(l,theta1,theta2):
    solutions = []
    if len(l) <= 1:
        return "More than one trace needed!"
    for i in range(len(l)+1):
        others = []
        others.append(l[0:i])
        others.append(l[i:len(l)+1])
        basetrace = l[i][0:i]
        for x in basetrace:
            for y in range(len(others)):
                for l in others[y]:
                    coord = l[0:]
                    if abs(coord[0]-basetrace[0]) <= theta1 and euclidian_distance(coord[1:2],basetrace[1:2]) <= theta2:
                        if [i,y] not in solutions:
                            solutions.append([i,y])
trace1 = [(1.0 ,(10.10 ,20.0) ) ,(3.0 ,(10.50 ,20.30) ) ,(5.0 ,(11.0 ,21) ) ]
trace2 = [(1.0 ,(15.00 ,15.0) ) ,(2.0 ,(12.00 ,17.00) ) ,(3.0 ,(10.50 ,20) ) ,(4.0 ,(12.0 ,21.0) ) ]
trace3 = [(1.0 ,(15.00 ,15.0) ) ,(3.0 ,(16.0 ,21.0) ) ,(5.0 ,(20.0 ,21.0) ) ]
print ( matrix_for_traces ([ trace1 , trace2 , trace3 ] ,0.0 ,1.0) )
def euclidian_distance(c1,c2):
    x = (c1[1]-c2[1])**2+(c1[0]-c2[0])**2
    x = x**0.5
    return x

            
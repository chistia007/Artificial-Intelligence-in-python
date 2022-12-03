heuristic_distance={}
graph={}
f=open('input.txt','r')
x=f.read().split("\n")
for i in range(len(x)):
    l=[]
    y=x[i].split(" ")
    heuristic_distance[y[0]]=int(y[1])
    for j in range(2,len(y),2):
        z=list()
        z.append(y[j])          #('Zerind')
        z.append(int(y[j+1]))   #['location', distance]
        z=tuple(z)               #('location', distance)
        l.append(z)              #[('location', distance)]
    graph[y[0]]=l                #Start node to branches {"Arad", [('Zerind', 75)]}
        
def a_star_search(starting__place,destination_place):
    opened=[]
    opened.append(starting__place)
    closed=[]
    place_distance={}
    parent_node={}
    place_distance[starting__place]=0
    parent_node[starting__place]=starting__place
    while (opened):
        place=None
        for i in opened:
            if place==None:
                place=i
            else:
                f_i=place_distance[i] + h(i)      
                f_node=place_distance[place] + h(place)         # checking minumum path of in the nodes in list open
                if f_i < f_node:
                    place=i
        if place==destination_place or graph[place]==None: #checking if node has branches or if the parent node is destination node
            pass
        else:
            for (child,distance) in obtain_childs(place):
                if child not in opened and child not in closed:
                    opened.append(child)
                    parent_node[child]=place   #keep track of the parent of thr child node
                    place_distance[child]=place_distance[place]+distance  #distance of the child node from mthe starting node
                elif place_distance[child]>place_distance[place]+distance: 
                    place_distance[child]=place_distance[place]+distance   # same node visiting from another path
                    parent_node[child]=place
                    if child in closed:
                        i=0
                        size=len(closed)
                        while i<len(closed):
                            if closed[i]==place:
                                closed.pop(i)
                                size-=1
                            i+=1
                        opened.append(child) #child added in opened
        if place==None:
            print('no such path')
            return None

        if place==destination_place:
            path=[]
            while parent_node[place]!=place:
                path.append(place)
                place=parent_node[place]
            path.append(starting__place)
            path=path[::-1]
            p=''
            for i in path:
                if i==starting__place:
                    p="path : "+ i
                elif i==destination_place:
                    p=p+ "--> " + i
                else:
                    p=p+ "--> " + i
            print(p)
            print("Total distance:",str(place_distance[destination_place]),"Km")
            return path
        i=0
        size=len(opened)
        while i<len(opened): 
            if opened[i]==place:
                opened.pop(i)  #poping the node that we traversed from opened
                size-=1
            i+=1
        closed.append(place)   #closing the node that we traversed

    print('path not found')
    return None


def obtain_childs(k):
    if k in graph:
        return graph[k]
    else:
        return None

def h(n):
    heuristic_distance
    return heuristic_distance[n]

a_star_search('Arad','Bucharest')
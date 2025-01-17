graph=dict()
graph['A']=["B","C"]
graph['B']=["E","A"]
graph['C']=['A','B','E','F']
graph['E']=['B','C']
graph['F']=['C']

matrix_elements=sorted(graph.keys())
print(matrix_elements)
cols=rows=len(matrix_elements)
print("{} {}".format(cols,rows))

adjacency_matrix=[[0 for x  in range(rows)] for y in range(cols)]
edges_list=[]

for key in matrix_elements:
    print(graph[key])
    for neighbor in graph[key]:
        edge=[]
        edge.append(key)
        edge.append(neighbor)
        print("{} {}".format(key,neighbor))
        edges_list.append(edge)

print(edges_list)
for edge in edges_list:
    index_of_first_vertex=matrix_elements.index(edge[0])
    index_of_second_vertex=matrix_elements.index(edge[1])
    print("index of first vertex:{}  index of second vertex:{}".format(index_of_first_vertex,index_of_second_vertex))
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex]=1

print(adjacency_matrix)
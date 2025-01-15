graph=dict()
graph['A']=["B","C"]
graph['B']=["E","A"]
graph['C']=['A','B','E','F']
graph['E']=['B','C']
graph['F']=['C']

matrix_elements=sorted(graph.keys())
cols=rows=len(matrix_elements)

adjacency_matrix=[[0 for x  in range(rows)] for y in range(cols)]
edges_list=[]


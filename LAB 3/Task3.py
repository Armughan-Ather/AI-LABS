#Task3
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}
graph = {
  'A': ['B', 'C', 'D'],
  'B': ['D', 'E', 'F'],
  'C': ['F', 'G', 'A'],
  'D': ['H'],
  'E': ['B', 'C', 'D'],
  'F': ['H','I'],
  'G': ['C'],
  'H': ['I'],
  'I': ['H']
}
def dls(graphOrTree,isTree,node, goal, depth, path,visited):
    if depth == 0:
        return False
    if node == goal:
        path.append(node)
        return True
    if node not in graphOrTree:
        return False
    visited.append(node)
    for child in graphOrTree[node]:
      if isTree==False:
        if child not in visited:
          if dls(graphOrTree,isTree,child, goal, depth - 1, path,visited):
            path.append(node)
            return True
      else:
          if dls(graphOrTree,isTree,child, goal, depth - 1, path,visited):
            path.append(node)
            return True
    visited.remove(node)
    return False

def iterative_deepening_dfs(graphOrTree,isTree,start, goal, max_depth):

    if isTree:
      var='tree'
    else:
      var='graph'
    for depth in range(max_depth + 1):
        #print(f"Searching for {var} at depth: {depth}")
        path = []
        visited=[]
        if dls(graphOrTree,isTree,start, goal, depth, path,visited):
            print("\nPath to goal:", " → ".join(reversed(path)))
            #print()
            return
    print("Goal not found within depth limit.")
start_node = 'A'
goal_node = 'I'
max_search_depth = 5
iterative_deepening_dfs(tree,True,start_node, goal_node, max_search_depth)
iterative_deepening_dfs(graph,False,start_node, goal_node, max_search_depth)

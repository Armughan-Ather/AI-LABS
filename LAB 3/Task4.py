# @title
#Task 4

grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    ['S', 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 'G']
]
def bfs_pubg(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    queue=[(start,[start])]
    visited=[]
    visited.append(start)
    while queue:
      (x,y),path=queue.pop(0)
      if grid[x][y]=='G':
        return path

      for dx,dy in directions:
        new_x,new_y=x+dx,y+dy
        if 0<=new_x<rows and 0<=new_y<cols and grid[new_x][new_y]!=1 and (new_x,new_y) not in visited:
          visited.append((new_x,new_y))
          queue.append(((new_x,new_y),path + [(new_x,new_y)]))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)
            grid[i][j] = 0
            break
path = bfs_pubg(grid, start)
if path:
    print("Shortest Path to Safe Zone:", path)
else:
    print("No path found to the safe zone.")

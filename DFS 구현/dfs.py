## recursive dfs fucntion
def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end= " ")
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
            
### graph .. (딕셔너리 ..?)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
print("Recursive_DFS: ", end= " ")
dfs(graph, 'A', visited)


### Stack used DFS
def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end= " ")
            visited.add(node)
            stack.extend(reversed(graph[node]))

print("\nStack_DFS: ", end= " ")
            
dfs_stack(graph, 'A')
print("")

## DFS backtracking algorithm
def dfs_backtrack(graph, start, visited):
    visited.add(start)
    print(start, end= " ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_backtrack(graph, neighbor, visited)
            

print("\nBacktrack_DFS: ", end= " ")
dfs_backtrack(graph, 'A', set())

def dfs_backtrack(graph, start, visited):
    visited.add(start)
    print(start, end = " ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_backtrack(graph, neighbor, visited)


print("\nBacktracking_DFS: ", end = " ")
dfs_backtrack(graph, 'A', set())

## backtrack_dfs with stack
def backtrack_dfs_stack(graph, start):
    stack = [(start, [])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end= " ")
            path.append(node)
            stack.extend([(neighbor, path) for neighbor in graph[node] if neighbor not in path])

print("\nBacktrack_DFS_Stack: ", end= " ")
backtrack_dfs_stack(graph, 'A')
            

def backtrack_dfs_stack(graph, start):
    stack = [(start, [])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end = " ")
            path.append(node)
            stack.extend([(neighbor, path) for neighbor in graph[node] if neighbor not in visited])
            
            

print("\nBacktrack_DFS_Stack: ", end = " ")
backtrack_dfs_stack(graph, 'A')
print("")

def exist(board, word):
    if not board:
        return False
 
    def dfs(board, word, i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
 
        temp = board[i][j]
        board[i][j] = "#"  # Mark as visited
 
        # Explore all adjacent cells
        found = dfs(board, word, i+1, j, k+1) or dfs(board, word, i-1, j, k+1) \
                or dfs(board, word, i, j+1, k+1) or dfs(board, word, i, j-1, k+1)
 
        board[i][j] = temp  # Reset the cell back to its original value
        return found
 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j, 0):
                return True
 
    return False

## stack way in exist
def exist2(board, word):
    
    
    row, col = len(board), len(board[0])

    for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    stack = [(i,j, 0, set())]

                    while stack:
                        x, y, k, visited = stack.pop()
                        if k == len(word) - 1:
                            return True
                        
                        visited.add((x,y))
                    # board_state[i][j] = "#"

                        directions = [(1,0),(-1,0),(0,1),(0,-1)]
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy

                            if (0 <= nx < row and 
                            0 <= ny < col and
                            k + 1 < len(word) and 
                            (nx, ny) not in visited and
                            board[nx][ny] == word[k + 1]):
                                    # 다음 문자 탐색을 위해 stack에 push
                                    stack.append((nx, ny, k + 1, visited.copy()))  # Deep Copy
    return False    

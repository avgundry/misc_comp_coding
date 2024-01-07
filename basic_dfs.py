class Solution:
    # assume graph is adjacency list, i.e.
    # graph[i] = all indices reachable from i?
    def dfs(self, graph):
        n = len(graph)
        visited = [-1 for _ in range(n)]
        parents = [None for _ in range(n)]
        courses = []
        print("visiting shit")

        for i in range(n):
            # If the node is unvisited
            if visited[i] == -1:
                self.dfs_visit(graph, visited, parents, i)

    # recursively visits the graph node at index ind
    def dfs_visit(self, graph, visited, parents, ind):
        visited[ind] = 0
        # print(f"visiting {graph[ind]}")
        for i in range(len(graph[ind])):
            # print(f"attemping to visit graph[{i}]")
            # print(f"{visited[graph[ind][i]]}")
            visit_index = graph[ind][i]
            if visited[visit_index] == -1:
                parents[graph[ind][i]] = ind
                self.dfs_visit(graph, visited, parents, graph[ind][i])
        
        visited[ind] = 1
        print(f"visited {ind}")

if __name__ == "__main__":
    s = Solution()
    s.dfs([[1, 2], [2, 3], [3], []])

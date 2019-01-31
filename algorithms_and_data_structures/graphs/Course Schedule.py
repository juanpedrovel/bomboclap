class Solution:
    def canFinish(self, numCourses, prerequisites):
        pr_len = len(prerequisites)
        visited = [False] * numCourses
        sinks = [False] * numCourses
        edges = []
        for i in range(numCourses):
            edges.append([])
        for u, v in prerequisites:
            edges[u].append(v)
        for i, childs in enumerate(edges):
            if not childs:
                visited[i] = True
                sinks[i] = True
                
        def cycle(node):
            visited[node] = True
            childs = edges[node]
            for i in childs:
                if visited[i] == False:
                    if cycle(i) == True:
                        return True
                elif sinks[i] == False:
                    return True
            sinks[node] = True
            return False
        
        for i in range(numCourses):
            if visited[i] == False:
                if cycle(i) == True:
                    return False
        return True

time = [[1,0]]
k = 2
d = Solution()
print(d.canFinish(k, time))
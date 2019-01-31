class Solution:
    def calcEquation(self, equations, values, queries):
        lens = len(equations)
        keys = {}
        counter = 0
        self.graph = {}
        for i, pair in enumerate(equations):
            for letter in pair:
                if letter not in self.graph:
                    self.graph[letter] = {}
            self.graph[pair[0]][pair[1]] = values[i]
            self.graph[pair[1]][pair[0]] = 1 / values[i]

        result = []
        for pair in queries:
            if pair[0] not in self.graph or pair[1] not in self.graph:
                result.append(-1.0)
                continue
            if pair[0] == pair[1]:
                result.append(1.0)
            elif pair[1] in self.graph[pair[0]]:
                result.append(self.graph[pair[0]][pair[1]])
            else:
                x = self.shorter_path(pair[0], pair[1])
                result.append(x)
        return result

    
    def shorter_path(self, a, b):
        stack = [(a, 1)]
        visited = set()
        while stack:
            item, value = stack.pop()
            if item in visited:
                continue
            visited.add(item)
            for key, weight in self.graph[item].items():
                if key == b:
                    return value * weight
                if key not in visited:
                    stack.append((key, value * weight))
        return -1.0
                
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]
d = Solution()
print(d.calcEquation(equations, values, queries))

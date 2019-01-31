# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self.n = 0

  def ReadData(self):
    self.n = int(input())
    self._data = [int(s) for s in input().split()]
    assert self.n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    for i in range(self.n//2, -1, -1):
        self.SwiftDown(i)

    
  def SwiftDown(self, i):
      max_index = i
      left_child = 2*i + 1
      right_child = 2*i + 2
      if left_child < self.n and self._data[left_child] < self._data[i]:
          max_index = left_child
      if right_child < self.n and self._data[right_child] < self._data[max_index]:
          max_index = right_child
      if i != max_index:
          self._swaps.append((i, max_index))
          self._data[i], self._data[max_index] = self._data[max_index], self._data[i]
          self.SwiftDown(max_index)
           


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

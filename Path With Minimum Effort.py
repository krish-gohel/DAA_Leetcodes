from queue import PriorityQueue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        return self.minimumEffortPathUtil(heights, 0, 0)
    
    def minimumEffortPathUtil(self, nums, i, j) :
        container = PriorityQueue()
        visited = set()
        container.put((0, (i, j)))
        min_effort = sys.maxsize

        while not container.empty() :
            diff, cell = container.get()
            if cell in visited :
                continue
                
            visited.add(cell)

            if cell[0] == len(nums) - 1 and cell[-1] == len(nums[0]) -1 :
                min_effort = min(min_effort, diff)

            for direction in self.directions :
                i1 = direction[0] + cell[0]
                i2 = direction[1] + cell[1]

                if i1 >= 0 and i1 < len(nums) and i2 >= 0 and i2 < len(nums[i1]) :
                    if (i1, i2) not in visited :
                        effort = max(diff, abs(nums[i1][i2] - nums[cell[0]][cell[-1]]))
                        container.put((effort, (i1, i2)))

        return min_effort
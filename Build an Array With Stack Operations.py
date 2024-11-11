class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []

        for i in range(1, target[-1] + 1):
            if i in target:
                s.append("Push")
            else:
                s.append("Push")
                s.append("Pop")

        return s
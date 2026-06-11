class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for (px, py), freq in self.points.items():

            if px == x or py == y:
                continue

            if abs(px - x) != abs(py - y):
                continue
            
            """
            if we directly access the self.points[(px, y)] -> we get `dictionary changed size during iteration`
            """
            res += (
                freq *
                self.points.get((px, y), 0) *
                self.points.get((x, py), 0)
            )
        
        return res

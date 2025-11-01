class HeuristicSolver:
    def __init__(self, kmap):
        self.kmap = kmap
        self.rows = kmap.rows
        self.cols = kmap.cols
        self.table = kmap.table
        self.groups = []

    def is_eligible(self, value):
        """1 > X > Y önceliği"""
        return value in [1, 'X', 'Y']

    def find_groups(self):
        """Grupları bul: yan yana veya alt alta gelenleri tek grup al"""
        visited = [[False]*self.cols for _ in range(self.rows)]
        groups = []

        for r in range(self.rows):
            for c in range(self.cols):
                if visited[r][c]:
                    continue
                cell = self.table[r][c]
                if cell not in [1, 'X', 'Y']:
                    visited[r][c] = True
                    continue

                group_cells = [(r, c)]
                visited[r][c] = True

                # Sağ ve alt hücreyi kontrol et (wrap-around)
                for dr, dc in [(0,1),(1,0)]:
                    nr = (r+dr) % self.rows
                    nc = (c+dc) % self.cols
                    if self.is_eligible(self.table[nr][nc]) and not visited[nr][nc]:
                        group_cells.append((nr, nc))
                        visited[nr][nc] = True

                groups.append(group_cells)

        self.groups = groups
        return groups

    def simplify(self):
        """ABCD veya kullanıcı değişken isimlerine göre sadeleştir"""
        simplified = []
        var_names = self.kmap.var_names
        for group in self.groups:
            if not group:
                continue
            terms = []
            # Basit: her grubun ilk hücresi üzerinden değişkenleri düşür
            row, col = group[0]
            for i, var in enumerate(var_names):
                # örnek basit mantık: son değişkeni düşür
                if i < len(var_names)-1:
                    terms.append(var)
            simplified.append(''.join(terms))
        return simplified


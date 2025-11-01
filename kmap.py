class KMap:
    def __init__(self, num_vars, var_names=None):
        self.num_vars = num_vars
        self.rows, self.cols = self.compute_size(num_vars)
        self.table = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        # Kullanıcı değişken isimleri (A,B,C,D gibi)
        if var_names and len(var_names) == num_vars:
            self.var_names = var_names
        else:
            self.var_names = [f"V{i}" for i in range(num_vars)]

    def compute_size(self, num_vars):
        rows = 2 ** (num_vars // 2)
        cols = 2 ** (num_vars - num_vars // 2)
        return rows, cols

    def set_cell(self, row, col, value):
        if row < 0 or row >= self.rows:
            raise IndexError("Row index out of range")
        if col < 0 or col >= self.cols:
            raise IndexError("Column index out of range")
        if value not in [0, 1, 'X', 'Y']:
            raise ValueError("Invalid cell value. Allowed: 0,1,'X','Y'")
        self.table[row][col] = value

    def get_neighbors(self, r, c):
        """Wrap-around komşular"""
        up = (r - 1) % self.rows
        down = (r + 1) % self.rows
        left = (c - 1) % self.cols
        right = (c + 1) % self.cols
        return [
            self.table[up][c],
            self.table[down][c],
            self.table[r][left],
            self.table[r][right],
        ]

    def add_smart_Y(self, max_Y=1):
        """Yalnız kalan 1’lerin yanına Y ekle, max_Y ile sınırla"""
        new_table = [row[:] for row in self.table]
        count_Y = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.table[r][c] == 1:
                    neighbors = self.get_neighbors(r, c)
                    # Eğer çevresinde başka 1 yoksa ve max_Y aşılmamışsa Y ekle
                    if all(n != 1 for n in neighbors) and count_Y < max_Y:
                        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                            rr = (r+dr) % self.rows
                            cc = (c+dc) % self.cols
                            if new_table[rr][cc] == 0:
                                new_table[rr][cc] = 'Y'
                                count_Y += 1
        self.table = new_table

    def display(self):
        print("KMap Tablosu:")
        for r in self.table:
            print(r)


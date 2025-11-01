from kmap import KMap
from heuristic import HeuristicSolver

# ABCD değişkenleri
kmap = KMap(4, ['A', 'B', 'C', 'D'])
kmap.set_cell(0, 0, 1)
kmap.set_cell(2, 2, 1)

print("Başlangıç KMap:")
kmap.display()

solver = HeuristicSolver(kmap)
groups = solver.find_groups()
simplified = solver.simplify()
print("\nGruplar (başlangıç):", groups)
print("Sadeleştirilmiş ifadeler (başlangıç, ABCD ile):", simplified)

# Akıllı Y ekle
kmap.add_smart_Y()

print("\nKMap sonrası (akıllı Y eklenmiş):")
kmap.display()

new_groups = solver.find_groups()
new_simplified = solver.simplify()
print("\nYeni Gruplar:", new_groups)
print("Yeni Sadeleştirilmiş ifadeler (ABCD ile):", new_simplified)


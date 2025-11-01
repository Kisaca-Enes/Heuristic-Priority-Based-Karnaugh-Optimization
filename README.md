# Heuristic K-Map Optimizer

**Heuristic K-Map Optimizer** is an advanced library to minimize Boolean expressions using Karnaugh Maps (K-Map) with automated optimizations. It reduces manual simplification, minimizes literal counts, and provides configurable X/Y hierarchical control for more robust results.

---

## Core Concept

Classical K-Map simplifies Boolean functions by grouping 1s. For example, for a 4-variable K-Map (A, B, C, D):

- Rows represent AB
- Columns represent CD
- Values: 0 or 1

Classical minimization example:

F(A,B,C,D) = Σ m(0, 5, 10, 15)


Classical K-Map limitations:

1. Does not hierarchically handle "don't care" (X) cells
2. Cannot automatically reduce literals for isolated single 1s

---

## Unique Features of This Algorithm

### 1. Priority System: 1 > X > Y

- `1` → Mandatory inclusion
- `X` → Optional inclusion
- `Y` → Only used to reduce literals for isolated 1s, not elsewhere

Mathematically:

include(cell) =
True if cell = 1
Optional if cell = X
Only if needed if cell = Y
False if cell = 0


---

### 2. Literal Reduction for Single 1s

Classical K-Map:

ABCD


Heuristic approach (single isolated 1 with neighbors):

1 * 1 = 1
1 * 0 = 0


- Single isolated 1 multiplies with neighboring Y
- Drops unnecessary literals

Example:

Cell value: 1 at (0,0)
Classical simplification: ABCD
Heuristic simplification: ABC # D is dropped because Y multiplies with 0


---

### 3. Wrap-Around and Grouping

- Supports wrap-around like classical K-Map
- Users can configure which 1s are adjacent and how X/Y are used
- Adjacent 1s form a **single group**, extra Y is **not added unnecessarily**

---

### 4. Resistance to Manipulation

- X or empty cells are not automatically included in groups
- Y acts as lowest-priority filler
- Only isolated 1s are simplified using Y
- Algorithm avoids incorrect group inclusion

---

## Example Usage

### Initial K-Map

4x4 K-Map

[
[1, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 1, 0],
[0, 0, 0, 0]
]


### Initial Groups and Simplified Expression

Groups: [[(0,0)], [(2,2)]]
Simplified (ABCD): ['ABC', 'ABC']


### K-Map After Smart Y Placement

KMap:
[
[1, 'Y', 0, 'Y'],
['Y', 0, 0, 0],
[0, 0, 1, 'Y'],
['Y', 0, 0, 0]
]

New Groups: [[(0,0)], [(2,2)]]
New Simplified (ABCD): ['ABC', 'ABC']


> Note: Y is only added next to isolated 1s, reducing literal count effectively.

---

## Advantages

1. Fewer literals → optimized Boolean expressions
2. Manipulation-resistant → hierarchical X/Y usage
3. User-configurable → variable names and Y addition levels
4. Wrap-around support → preserves classical K-Map functionality
Heuristic K-Map optimizer with controlled Y-cells to minimize manipulation and enhance simplification.
---

## Disadvantages

1. More complex than classical K-Map
2. Larger K-Maps may require longer processing
3. Misconfigured Y settings may reduce optimization effectiveness

---

## Summary

This algorithm **automatically optimizes classical K-Map expressions**, reduces literals for isolated 1s using Y, and provides hierarchical control for X/Y cells.  

Mathematically:

F_heuristic = ∏_groups (OR of 1s and Y) # minimized literals via Y


> The heuristic K-Map achieves both optimization and safer group formation for complex Boolean functions.


# Heuristic-Priority-Based-Karnaugh-Optimization
Heuristic K-Map Optimizer

Heuristic K-Map Optimizer is an advanced approach to minimize boolean expressions using Karnaugh Maps (K-Map) with automated optimizations. This library reduces manual simplifications, minimizes the number of literals, and provides resistance against manipulation through configurable X/Y hierarchies.

Core Concept

The classical K-Map simplifies boolean functions by grouping 1s. For a 4-variable K-Map (A, B, C, D):

Rows: AB

Columns: CD

Values: 0 or 1

Classical minimization example:

F(A,B,C,D)=∑m(0,5,10,15)
F(A,B,C,D)=∑m(0,5,10,15)

Classical algorithms have limitations:

They do not hierarchically handle “don’t care” (X) cells.

They cannot automatically reduce the number of literals for isolated single 1s.

Unique Features of This Algorithm
1. Priority System: 
1>X>Y
1>X>Y

1: Mandatory inclusion

X: Optional inclusion

Y: Only used to reduce literals for isolated single 1s; not added elsewhere

Mathematically:

include(cell)={True	if cell = 1
Optional	if cell = X
Only if needed	if cell = Y
False	if cell = 0
include(cell)=
⎩

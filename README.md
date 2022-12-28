#Logical Zonotope Python Library
Logical Zonotope: A Set Representation for Binary Vectors
Based on https://arxiv.org/abs/2210.08596

logical zonotopes can be used to greatly reduce the computational complexity of a variety of operations over sets of binary vectors, including logical operations (e.g. XOR, NAND, AND, OR) and semi-tensor products.

### Installation
```
pip install logical-zonotope
```

```Python
from logical_zonotope import LogicalZonotope, z_xnor

#Instanciating Logical Zonotope Objects
zonotope_1 = LogicalZonotope()
zonotope_2 = LogicalZonotope()
zonotope_1.set((1, 1), {(1, 0)})
zonotope_2.set((0, 1), {(1, 1), (1, 0), (1, 1)})

# Calling the z_xnor method
z_xnor(zonotope_1, zonotope_2).print()
```
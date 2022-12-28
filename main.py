from logical_zonotope import LogicalZonotope, z_or

if __name__ == '__main__':
    zonotope_1 = LogicalZonotope()
    zonotope_2 = LogicalZonotope()
    zonotope_1.set((1, 1), {(1, 0)})
    zonotope_2.set((0, 1), {(1, 1), (1, 0), (1, 1)})
    #z_not(zonotope_1).print()
    #z_nand(zonotope_1, zonotope_2).print()
    z_or(zonotope_1, zonotope_2).print()
    #unique(zonotope_2).print()
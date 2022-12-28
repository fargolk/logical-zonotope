from logical_zonotope import LogicalZonotope


def tuple_and(t1, t2):
    return tuple((int(i and j)) for i, j in zip(t1, t2))


def tuple_nand(t1, t2):
    return tuple(int(not (i and j)) for i, j in zip(t1, t2))


def tuple_xor(t1, t2):
    return tuple(int((i ^ j)) for i, j in zip(t1, t2))


def z_and(z1, z2):
    z1_and_z2 = LogicalZonotope()
    z1_and_z2.center = tuple_and(z1.center, z2.center)
    z1_and_z2.generators = [tuple_and(i, j) for i, j in zip(z1.generators, z2.generators)]
    z1_and_z2.generators = z1_and_z2.generators + [tuple_and(z1.center, j) for j in z2.generators]
    z1_and_z2.generators = z1_and_z2.generators + [tuple_and(z2.center, j) for j in z1.generators]
    z1_and_z2.generators = list(set(z1_and_z2.generators))
    return z1_and_z2


def z_xor(z1, z2):
    z1_xor_z2 = LogicalZonotope()
    z1_xor_z2.center = tuple_xor(z1.center, z2.center)
    z1_xor_z2.generators = set(z1.generators) | set(z2.generators)
    return z1_xor_z2


def z_not(z):
    z1 = LogicalZonotope()
    z1.generators = []
    tmp_list = []
    for i in range(0, len(z.center)):
        tmp_list.append(1)
    z1.center = tuple(tmp_list)
    return z_xor(z, z1)


def z_nand(z1, z2):
    return z_not(z_and(z1, z2))


def z_or(z1, z2):
        z1_or_z2 = z_nand(z_nand(z1, z1), z_nand(z2, z2))
        return z1_or_z2


def z_xnor(z1, z2):
    return z_not(z_xor(z1, z2))


def unique(z):
    z.generators = list(set(z.generators))
    return z


def dimension(z):
    return len(z.center)

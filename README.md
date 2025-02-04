**1-Electron integrals (h)**

Starts with “begin_one_electron_integrals”.

*Form:*

i   j   h(i, j)

*Symmetry:*

h(i, j) = h(j, i)

All Terms for DUCC Hamiltonians are printed.

One unique element is printed for the Bare Hamiltonian, and the remainder must be filled in.

**2-Electron integrals (v)**

Starts with “begin_two_electron_integrals”.

*Form:*

i   j   k   l   v(i, j, k, l)

v(electron 1, electron 1, electron 2, electron 2)


*Symmetry:*

DUCC: V(i, j, k, l) = V(k, l, i, j) = V(j, i, l, k) = V(l, k, j, i)

All Terms for DUCC Hamiltonians are printed.

Bare: V(i, j, k, l) = V(k, l, i, j) = V(j, i, l, k) = V(l, k, j, i) = V(j, i, k, l) = V(i, j, l, k) = V(k, l, j, i) = V(l, k, i, j)

One unique element is printed for the Bare Hamiltonian, and the remainder must be filled in.


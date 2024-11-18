import os
import numpy as np

Start = 2.20
Stop = 2.01
Increment = -0.01
RangeStop = Stop + Increment

for value in np.arange(Start,RangeStop,Increment):
  with open('input.nw','w') as input:
    input.write('''
echo
start H8
title "H8"

memory total 180 gb

geometry units bohr
symmetry c1''')
  
    input.write('''
H 0 0 0
H 0 0 {0:.2f}
H 0 0 {1:.2f}
H 0 0 {2:.2f}
H 0 0 {3:.2f}
H 0 0 {4:.2f}
H 0 0 {5:.2f}
H 0 0 {6:.2f}'''.format(value,2*value,3*value,4*value,5*value,6*value,7*value))

    # if value == Start:

    input.write('''
end

basis spherical
  * library cc-pVTZ
end

scf
thresh 1e-8
end

tce
  2eorb
  2emet 13
  ccsd
  thresh 1e-8
  maxiter 300
end

# set tce:print_integrals T
# set tce:qorb 8
# set tce:qela 4
# set tce:qelb 4

set tce:qducc T
set tce:nactv 4
set tce:nonhf T
set tce:ducc_model 6

set tce:printtol 0.02

task tce
''')
#     else:
#       input.write('''
# end

# basis spherical
#   * library cc-pVTZ
# end

# tce
#   2eorb
#   2emet 13
#   ccsd
#   maxiter 300
# end

# set tce:print_integrals T
# set tce:qorb 6
# set tce:qela 3
# set tce:qelb 3

# # set tce:qducc T
# # set tce:nactv 3
# # set tce:nonhf T
# # set tce:ducc_model 6

# set tce:printtol 0.02

# task tce
# ''')

  commandline = "mpirun -n 2 /hpc/home/baum612/code/nwchem/bin/LINUX64/nwchem input.nw > {:.2f}.out".format(value)
  os.system(commandline)

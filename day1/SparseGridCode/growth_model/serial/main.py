#======================================================================
#
#     This routine solves an infinite horizon growth model
#     with dynamic programming and sparse grids
#
#     The model is described in Scheidegger & Bilionis (2017)
#     https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2927400
#
#     external libraries needed:
#     - IPOPT (https://projects.coin-or.org/Ipopt)
#     - PYIPOPT (https://github.com/xuy/pyipopt)
#     - TASMANIAN (http://tasmanian.ornl.gov/)
#
#     Simon Scheidegger, 11/16 ; 07/17
#======================================================================

import nonlinear_solver_initial as solver     #solves opt. problems for terminal VF
import nonlinear_solver_iterate as solviter   #solves opt. problems during VFI
from parameters import *                      #parameters of model
import interpolation as interpol              #interface to sparse grid library/terminal VF
import interpolation_iter as interpol_iter    #interface to sparse grid library/iteration
import postprocessing as post                 #computes the L2 and Linfinity error of the model

import TasmanianSG                            #sparse grid library
import numpy as np
import copy

import matplotlib.pyplot as plt
import numpy as np
from random import uniform
from mpl_toolkits.mplot3d import Axes3D

#======================================================================
# Start with Value Function Iteration

# terminal value function
valnew0=TasmanianSG.TasmanianSparseGrid()
valnew1=TasmanianSG.TasmanianSparseGrid()
valnew2=TasmanianSG.TasmanianSparseGrid()
valnew3=TasmanianSG.TasmanianSparseGrid()
valnew4=TasmanianSG.TasmanianSparseGrid()
valnew = [valnew0, valnew1, valnew2, valnew3, valnew4]
for z in zlist:
	print("Currently at State", z)
	valnew[z] = interpol.sparse_grid_adapt(n_agents, iDepth, z)

# value function during iteration

print("we made it this far")
valold = [0,0,0,0,0]
for z in zlist:
    valold[z] = valnew[z]

for i in range(numstart, numits):
	valnew0=TasmanianSG.TasmanianSparseGrid()
	valnew1=TasmanianSG.TasmanianSparseGrid()
	valnew2=TasmanianSG.TasmanianSparseGrid()
	valnew3=TasmanianSG.TasmanianSparseGrid()
	valnew4=TasmanianSG.TasmanianSparseGrid()
	valnew = [valnew0, valnew1, valnew2, valnew3, valnew4]
	for z in zlist:
    		valnew[z] = (interpol_iter.sparse_grid_iter_adapt(n_agents, iDepth, valold, z))
	print("Valnew length:", len(valnew))
	print("Valold length:", len(valold))
	for z in zlist:
        	valold[z] = valnew[z]

aPnts = np.empty([10000, 2])
for iI in range(aPnts.shape[0]):
    for iJ in range(2):
        aPnts[iI][iJ] = uniform(0.2, 3)

aRes = np.empty([aPnts.shape[0],5])
for i in range(5):
    for j in range(aPnts.shape[0]):
        kj = np.array([aPnts[j]])
        aRes[j,i] = valnew[i].evaluateBatch(kj) # Evaluate the interpolant at the cartesian grid

for z in zlist:
	post.plot_routine(2,valnew[z], 2, aPnts.shape[0], z)
np.savetxt("FinalValues.txt", aRes)
np.savetxt("EvalPoints", aPnts)
	


#======================================================================
print( "===============================================================")
print( " " )
print( " Computation of a growth model of dimension ", n_agents ," finished after ", numits, " steps")
print( " " )
print( "===============================================================")
#======================================================================

# compute errors
avg_err=post.ls_error(n_agents, numstart, numits, No_samples)


#======================================================================
print( "===============================================================")
print( " ")
print( " Errors are computed -- see errors.txt")
print( " ")
print( "===============================================================")
#======================================================================

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

#======================================================================
# Start with Value Function Iteration

# terminal value function
valnew0=TasmanianSG.TasmanianSparseGrid()
valnew1=TasmanianSG.TasmanianSparseGrid()
valnew2=TasmanianSG.TasmanianSparseGrid()
valnew3=TasmanianSG.TasmanianSparseGrid()
valnew4=TasmanianSG.TasmanianSparseGrid()
valnew = [valnew0, valnew1, valnew2, valnew3, valnew4]
if (numstart==0):
    for z in zlist:
    	print("Currently at State", z)
    	valnew[z] = interpol.sparse_grid_adapt(n_agents, iDepth, z)
    	valnew[z].write("valnew_1." + str(numstart) + ".txt") #write file to disk for restart

# value function during iteration
else:
    for (z in zlist):
        valnew[z].read("valnew_1." + str(numstart) + ".txt")  #write file to disk for restart

print("we made it this far")
valold = []
valold = list(copy.deepcopy(valnew))

for i in range(numstart, numits):
	valnew0=TasmanianSG.TasmanianSparseGrid()
	valnew1=TasmanianSG.TasmanianSparseGrid()
	valnew2=TasmanianSG.TasmanianSparseGrid()
	valnew3=TasmanianSG.TasmanianSparseGrid()
	valnew4=TasmanianSG.TasmanianSparseGrid()
	valnew = [valnew0, valnew1, valnew2, valnew3, valnew4]
	for z in zlist:
    		valnew[z] = (interpol_iter.sparse_grid_iter_adapt(n_agents, iDepth, valold, z))
    	valold = []
    	valold = list(copy.deepcopy(valnew))
    	valnew.write("valnew_1." + str(i+1) + ".txt")

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

#======================================================================
#
#     This routine interfaces with the TASMANIAN Sparse grid
#     The crucial part is
#
#     aVals[iI]=solveriter.iterate(aPoints[iI], n_agents)[0]
#     => at every gridpoint, we solve an optimization problem
#
#     Simon Scheidegger, 11/16 ; 07/17
#======================================================================

import TasmanianSG
import numpy as np
from parameters import *
import nonlinear_solver_iterate as solveriter

#======================================================================

def sparse_grid_iter(n_agents, iDepth, valold, z):

    grid  = TasmanianSG.TasmanianSparseGrid()

    k_range=np.array([k_bar, k_up])

    ranges=np.empty((n_agents, 2))


    for i in range(n_agents):
        ranges[i]=k_range

    iDim=n_agents
    iOut=1

    grid.makeLocalPolynomialGrid(iDim, iOut, iDepth, which_basis, "localp")
    grid.setDomainTransform(ranges)

    aPoints=grid.getPoints()
    iNumP1=aPoints.shape[0]
    aVals=np.empty([iNumP1, 1])

    file=open("comparison1.txt", 'w')
    for iI in range(iNumP1):
        print("interpolation_iter.py function call z:", z)
        aVals[iI]=solveriter.iterate(aPoints[iI], n_agents, valold, z)[0]
        v=aVals[iI]*np.ones((1,1))
        to_print=np.hstack((aPoints[iI].reshape(1,n_agents), v))
        np.savetxt(file, to_print, fmt='%2.16f')

    file.close()
    grid.loadNeededPoints(aVals)

    f=open("grid_iter.txt", 'w')
    np.savetxt(f, aPoints, fmt='% 2.16f')
    f.close()

    return grid

#======================================================================


def sparse_grid_iter_adapt(n_agents, iDepth, valold, z):

    grid  = TasmanianSG.TasmanianSparseGrid()

    k_range=np.array([k_bar, k_up])

    ranges=np.empty((n_agents, 2))


    for i in range(n_agents):
        ranges[i]=k_range

    iDim=n_agents
    iOut=1

    grid.makeLocalPolynomialGrid(iDim, iOut, iDepth, which_basis, "localp")
    grid.setDomainTransform(ranges)

    aPoints=grid.getPoints()
    iNumP1=aPoints.shape[0]
    aVals=np.empty([iNumP1, 1])
    grid.loadNeededPoints(aVals)

    file=open("comparison1.txt", 'w')
    for iI in range(iNumP1):
        aVals[iI]=solveriter.iterate(aPoints[iI], n_agents, valold, z)[0]
        v=aVals[iI]*np.ones((1,1))
        to_print=np.hstack((aPoints[iI].reshape(1,n_agents), v))
        np.savetxt(file, to_print, fmt='%2.16f')

    for iK in range(refinement_level):
        grid.setSurplusRefinement(fTol, 1, "fds")   #also use fds, or other rules
	aPoints = grid.getNeededPoints()
        aVals = np.empty([aPoints.shape[0], 1])
        for iI in range(aPoints.shape[0]):
            aVals[iI] = solveriter.iterate(aPoints[iI], n_agents, valold, z)[0]

        grid.loadNeededPoints(aVals)

    file.close()

    f=open("grid_iter.txt", 'w')
    np.savetxt(f, aPoints, fmt='% 2.16f')
    f.close()

    return grid

#======================================================================

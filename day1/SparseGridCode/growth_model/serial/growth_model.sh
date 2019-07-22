#!/bin/bash -l
#SBATCH --ntasks=1 ## how many cpus used here
#SBATCH --time=01:00:00 ## walltime requested
#SBATCH --output=slurm_test.out ## output file #SBATCH --error=slurm_test.err ## error
### executable 

srun python main.py

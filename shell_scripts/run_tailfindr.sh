#! /bin/csh
#PBS -q hotel
#PBS -N TALEOFTWOTAILS
#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:04:00
#PBS -A jlykkeandersen
#PBS -V
#PBS -o tailfindr.o
#PBS -e tailfindr.e

module load R
Rscript /home/t2shaw/BG_GS_Nanopore_Analysis/run_tail_finder.r $IN
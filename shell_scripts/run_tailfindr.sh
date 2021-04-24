#! /bin/csh
#PBS -q hotel
#PBS -N TALEOFTWOTAILS
#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:01:00
#PBS -A jlykkeandersen
#PBS -V
#PBS -o tailfindr.o
#PBS -e tailfindr.e

Rscript /home/t2shaw/BG_GS_Nanopore_Analysis/run_tail_finder.r
#! /bin/csh
#PBS -q hotel
#PBS -N TALEOFTWOTAILS
#PBS -l nodes=1:ppn=2
#PBS -l walltime=1:00:00
#PBS -A jlykkeandersen
#PBS -V
#PBS -o tailfindr.o
#PBS -e tailfindr.e

module load R
cd $DIR
Rscript /home/t2shaw/BG_GS_Nanopore_Analysis/run_tail_finder.r $IN $OUT

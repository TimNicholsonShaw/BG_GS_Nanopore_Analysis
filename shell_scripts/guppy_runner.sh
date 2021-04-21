#! /bin/csh
#PBS -q hotel
#PBS -N GUPPY
#PBS -l nodes=1:ppn=8
#PBS -l walltime=04:00:00
#PBS -A jlykkeandersen
#PBS -V
#PBS -o guppy.o
#PBS -e guppy.e

/home/t2shaw/ont-guppy-cpu/bin/guppy_basecaller \
-i $INPUTPATH \
-s $SAVEPATH \
-c dna_r9.4.1_450bps_fast.cfg \
--recursive \
--barcode_kits SQK-PBK004 \
--fast5_out\
--cpu_threads_per_caller 2 \
--num_callers 4 \
--trim_strategy none


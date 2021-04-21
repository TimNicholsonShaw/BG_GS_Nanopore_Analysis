#! /bin/csh
#PBS -q hotel
#PBS -N GUPPY
#PBS -l nodes=1:ppn=12
#PBS -l walltime=04:00:00
#PBS -A jlykkeandersen
#PBS -V
#PBS -o sambamout_$SAM
#PBS -e sambamerror_$SAM

/home/t2shaw/ont-guppy-cpu/binguppy_basecaller \
-i $INPUTPATH \
-s $SAVEPATH \
-c dna_r9.4.1_450bps_fast.cfg \
--recursive \
--barcode_kits SQK-PBK004 \
--trim_barcodes \
--fast5_out\

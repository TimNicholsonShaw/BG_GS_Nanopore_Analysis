library(tailfindr)
args = commandArgs(trailingOnly = T)
# error with setting up compute clusters
# try running 
# parallel:::setDefaultClusterOptions(setup_strategy = "sequential")

# Code with all the setting necessary to quickly run the tailfindr library

# test code
tailfindr_test <- function(){
    df <- find_tails(fast5_dir = system.file('extdata', 'cdna', package = 'tailfindr'),
                 save_dir = '~/Downloads',
                 csv_filename = 'cdna_tails.csv',
                 num_cores = 4)
    return(df)
}

# Install R packages to local directory using the lib parameter in install.pacakges


find_tails(fast5_dir = ars[1],
            save_dir = './',
            csv_filename = args[2],
            num_cores = 4,
            basecall_group = 'Basecall_1D_001',
            dna_datatype = 'custom-cdna',
            front_primer="GACACAACTGTGTTCACTAGC",
            end_primer="ACTTGCCTGTCGCTCTATCTTCACACGACGCTCTTCCGA"
            )
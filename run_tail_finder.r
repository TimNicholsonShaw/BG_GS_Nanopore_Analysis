library(tailfindr)

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
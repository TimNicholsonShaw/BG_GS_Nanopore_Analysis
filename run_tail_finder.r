.libPaths("~/R_libs/")#this will only work on tscc now
library(tailfindr) 
library(withr)
args = commandArgs(trailingOnly = T)

# error with setting up compute clusters
# try running 
# parallel:::setDefaultClusterOptions(setup_strategy = "sequential")

# Code with all the setting necessary to quickly run the tailfindr library
#Use this to make Rmpi work, change
#install.packages("Rmpi",
  #               configure.args =
   #              c("--with-Rmpi-include=/opt/openmpi/intel/ib/include/",
    #               "--with-Rmpi-libpath=/opt/openmpi/intel/ib/lib/",
     #              "--with-Rmpi-type=OPENMPI"))
# test code
tailfindr_test <- function(){
    df <- find_tails(fast5_dir = system.file('extdata', 'cdna', package = 'tailfindr'),
                 save_dir = '~/Downloads',
                 csv_filename = 'cdna_tails.csv',
                 num_cores = 4)
    return(df)
}

# Install R packages to local directory using the lib parameter in install.pacakges
# Use withr package to get with_libpaths() and specify the devtools library path

find_tails(fast5_dir = args[1],
                        save_dir = args[2],
                        csv_filename = "A_tails.csv",
                        num_cores = 15,
                        basecall_group = 'Basecall_1D_001')

aksdlkn n lkdlkfjlke
quit()
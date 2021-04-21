library(ggplot2)
library(tidyverse)
library(dplyr)

read_in_prepped_sam <- function(csv_file) {
    df <- read_csv(csv_file)

    df <- select(df, -QNAME, -RNAME, -MAPQ, -CIGAR, -RNEXT, -PNEXT, -TLEN, -QUAL, -FLAG, -SEQ) #drop unnecessary columns
    return(df)
}



plot_lengths <- function(df, samples, xmin=0, xmax=1000) {
    df <- pivot_longer(df, cols=c("LENGTH"))
    df <- filter(df, id %in% samples)
    plt <- ggplot(df,aes(x=value, color=id, linetype=condition, fill=substrate)) + 
                geom_density()
    return(plt)
}

plot_right_location <- function(df, samples) {
    df <- select(df, SAMPLE %in% samples, ATTRIBUTE=="RIGHT")

    plt <- ggplot(df, aes(x=VALUE, color=SAMPLE)) +
        geom_density()

    return (plt)
}

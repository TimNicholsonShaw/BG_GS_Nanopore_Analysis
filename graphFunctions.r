library(ggplot2)
library(tidyverse)

read_in_prepped_sam <- function(csv_file) {
    df <- read_csv(csv_file)

    df <- select(df, -QNAME, -RNAME, -MAPQ, -CIGAR, -RNEXT, -PNEXT, -TLEN, -QUAL, -FLAG, -SEQ) #drop unnecessary columns

    df <- pivot_longer(df, cols=c(RIGHT,LENGTH), names_to="ATTRIBUTE", values_to="VALUE")
    return(df)
}

plot_lengths <- function(df, sample, xmin=0, xmax=1000) {
    df <- select(df, SAMPLE %in% samples, ATTRIBUTE=="LENGTH")
    plt <- ggplot(df,aes(x=VALUE, color=SAMPLE)) + 
                geom_density()
        return(plt)
}

plot_right_location <- function(df, samples) {
    df <- select(df, SAMPLE %in% samples, ATTRIBUTE=="RIGHT")

    plt <- ggplot(df, aes(x=VALUE, color=SAMPLE)) +
        geom_density()

    return (plt)
}

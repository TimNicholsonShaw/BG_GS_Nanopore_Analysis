library(ggplot2)

read_in_prepped_sam <- function(csv_file) {
    df <- read_csv(csv_file)

    df <- select(df, -QNAME, -RNAME, -MAPQ, -CIGAR, -RNEXT, -PNEXT, -TLEN, -QUAL, -FLAG, -SEQ) #drop unnecessary columns

    df <- pivot_longer(df, cols=c(RIGHT,LENGTH), names_to="ATTRIBUTE", values_to="VALUE")
    return(df)
}

plot_lengths <- function(df, sample) {
    filter(df, SAMPLE==sample, ATTRIBUTE=="LENGTH") %>%
        ggplot(aes(x=VALUE)) + geom_density()

}
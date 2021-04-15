library(ggplot2)

read_in_prepped_sam <- function(csv_file) {
    df <- read_csv(csv_file)

    df <- select(df, -QNAME, -RNAME, -MAPQ, -CIGAR, -RNEXT, -PNEXT, -TLEN, -QUAL, -FLAG, -SEQ) #drop unnecessary columns

    df <- pivot_longer(df, cols=c(RIGHT,LENGTH), names_to="ATTRIBUTE", values_to="VALUE")
    return(df)
}

plot_lengths <- function(df, sample, xmin=0, xmax=1000) {
    
        plt <- ggplot(filter(df, SAMPLE==sample, ATTRIBUTE=="LENGTH"),
                        aes(x=VALUE)) + 
                        geom_density()


        return(plt)
}

plot_right_location <- function(df, sample, xmin=600, xmax=2600) {
    plt <- ggplot(
        filter(df, SAMPLE==sample, ATTRIBUTE=="RIGHT"),
        aes(x=VALUE)) +
        geom_density()

    return (plt)
}

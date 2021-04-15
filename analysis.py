import pandas as pd
import tools


"""
Things I want to ask and know about each sam file
xPercent mapped
xPercent mapped with with mismapped 5' ends
-Median Length
-Stdev length
-Percent mapped longer than 500nt
-Percent mapped, with proper 5' ends that map to full length
"""

def findPercentMapped(sam_df):
    """
    Takes a SAM dataframe and finds the percent that successfully mapped.
    """
    total = len(sam_df)

    is_mapped = sam_df.FLAG.isin([0,16])

    return len(sam_df[is_mapped]) / total

def findMismappedFivePrime(sam_df, proper_5_loc=706, margin=10):
    """
    Takes a SAM dataframe and finds the percent of total that mapped successully,
    but is mismapped in the 5' end. Likely sequencing errors. So probably an
    unreliable read to look at.
    """

    total = len(sam_df)

    is_mapped = sam_df.FLAG.isin([0,16])

    improperFiveMapped = ((sam_df.POS < proper_5_loc - margin) | (sam_df.POS > proper_5_loc + margin)) & is_mapped

    return len(sam_df[improperFiveMapped]) / total

def findTotalReads(sam_df):
    return len(sam_df)

def findMedianLengthMapped(sam_df):

    sam_df = tools.isExtendedOrReturnsExtended(sam_df)
    is_mapped = sam_df.FLAG.isin([0,16])
    sam_df = sam_df[is_mapped]

    return sam_df.LENGTH.median()

def findMeanLengthMapped(sam_df):

    sam_df = tools.isExtendedOrReturnsExtended(sam_df)
    is_mapped = sam_df.FLAG.isin([0,16])
    sam_df = sam_df[is_mapped]

    return sam_df.LENGTH.mean()

def findMedianLengthTotal(sam_df):
    return sam_df.SEQ.str.len().median()

def findMeanLengthTotal(sam_df):
    return sam_df.SEQ.str.len().mean()

def findStdevLengthMapped(sam_df):

    sam_df = tools.isExtendedOrReturnsExtended(sam_df)
    is_mapped = sam_df.FLAG.isin([0,16])
    sam_df = sam_df[is_mapped]

    return sam_df.LENGTH.std()

def findStdevLengthTotal(sam_df):
    return sam_df.SEQ.str.len().std()

def summarizeSAM(sam_df):
    pass




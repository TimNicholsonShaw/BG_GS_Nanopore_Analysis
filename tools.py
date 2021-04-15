"""
A suite of tools for analysis of Beta Globin Specific Nanopore Sequencing
"""
import re, csv
from glob import glob
import pandas as pd

#What each column in a sam file represents
samColumnsDict = {
    0:'QNAME',
    1:"FLAG",
    2:"RNAME",
    3:"POS",
    4:"MAPQ",
    5:"CIGAR",
    6:"RNEXT",
    7:"PNEXT",
    8:"TLEN",
    9:"SEQ",
    10:"QUAL"
}

#Can take leftmost coordinate and cigar and output where rightmost coord is
def rightFinder(left, CIGAR): #What is the rightmost coord of a Sam record

    codes ={ #use codes to determine whether or not template is consumed
        "M":True,
        "I":False,
        "D":True,
        "N":True,
        "S":False,
        "H":False,
        "P":False,
        "=":True,
        "X":True,
    } 
    
    for item in re.findall(r'(\d+)([\w+]{1})', CIGAR):
        if codes[item[1]]:
            left+=int(item[0])
    return left

#Finds the length of the read that maps to the template using the CIGAR string
def lengthFinder(CIGAR):
    length=0
    codes ={
        "M":True,
        "I":True,
        "D":False,
        "N":False,
        "S":False,
        "H":False,
        "P":False,
        "=":True,
        "X":True,
    }
    for item in re.findall(r'(\d+)([\w+]{1})', CIGAR):
        if codes[item[1]]:
            length+=int(item[0])
    return length

#Filters out only reads that mapped. Adds a right map coord and mapped length
def samFilterer(sam_loc): 
    with open(sam_loc, "r") as reader, open(sam_loc+".filtered", 'w') as writer:
        reader = csv.reader(reader, delimiter="\t", quotechar="@")
        reader.__next__()

        writer = csv.writer(writer, delimiter="\t")

        for line in reader:
            if line[1]=='0' or line[1]=='16': #flag for map and rev comp map
                writer.writerow(line[:11]+ #SAM entry - extra garbage
                    [rightFinder(int(line[3]), line[5])] +
                    [lengthFinder(line[5])]
                    )

def globSamFilterer(pattern): #give a pattern of files and it'll will filter them all
    files = glob(pattern)

    for file in files:
        samFilterer(file)
        print("finished", file)


def samReader(file_loc):
    """
    Reads a sam file into a pandas dataframe
    """
    #names of SAM Columns

    sam_cols = [samColumnsDict[x] for x in range(11)]

    df = pd.read_csv(file_loc, 
        comment="@", 
        delimiter="\t", 
        header=None, 
        usecols=range(11),
        names=sam_cols)

    return df

def samExtender(sam_df):
    """
    Adds a mapped length and a right side position.
    """

    sam_df['RIGHT'] = [rightFinder(left, CIGAR) for left,CIGAR in zip(sam_df.POS, sam_df.CIGAR)]

    sam_df['LENGTH'] = [lengthFinder(CIGAR) for CIGAR in sam_df.CIGAR]

    return sam_df

def isExtendedOrReturnsExtended(sam_df):
    if "LENGTH" in sam_df.columns and "RIGHT" in sam_df.columns:
        return sam_df
    else:
        return samExtender(sam_df)

def exportSAMForR(sam_df):
    pass

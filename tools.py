"""
A suite of tools for analysis of Beta Globin Specific Nanopore Sequencing
"""
import re, csv

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





    
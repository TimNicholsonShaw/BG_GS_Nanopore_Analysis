"""
A suite of tools for analysis of Beta Globin Specific Nanopore Sequencing
"""
import re

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
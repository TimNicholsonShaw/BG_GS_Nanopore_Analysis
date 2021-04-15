from tools import samReader, samExtender, filterProperMapped
import pandas as pd

def exportForRAnalysis(sam_file_locs, outFile):

    out_df = None 

    for file in sam_file_locs:
        sam_df = samReader(file)
        sam_df = samExtender(sam_df)
        sam_df = filterProperMapped(sam_df)

        sam_df["SAMPLE"] = file[file.rfind("/")+1:]

        if type(out_df) == pd.core.frame.DataFrame:
            out_df = out_df.append(sam_df)
        else:
            out_df = sam_df
        
        print(file, len(out_df))

    out_df.to_csv(outFile, index=False)

    return out_df




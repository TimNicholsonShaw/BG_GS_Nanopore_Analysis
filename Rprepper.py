from tools import samReader, samExtender, filterProperMapped, filterSenseStrand
import pandas as pd

def exportForRAnalysis(sam_file_locs, outFile, metadata=""):
    # need to incorporate the ability to add metadata here
    # metadata order must match sam_file_locs order
    out_df = None 


    if metadata:
        df = pd.read_csv(metadata)
        cols = df.columns
        assert len(sam_file_locs) == len(df)

        for i in range(len(sam_file_locs)):
            sam_df = samReader(sam_file_locs[i])
            sam_df = samExtender(sam_df)
            sam_df = filterProperMapped(sam_df)
            
            md = df.loc[i]
            for col in cols:
                sam_df[col] = md[col]

            print(sam_file_locs[i], "->", md[cols[0]])
            if type(out_df) == pd.core.frame.DataFrame:
                out_df = out_df.append(sam_df)
            else:
                out_df = sam_df
    else:
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

def exportForRAnalysisSenseStrandOnly(sam_file_locs, outFile, metadata=""):
    # need to incorporate the ability to add metadata here
    # metadata order must match sam_file_locs order
    out_df = None 


    if metadata:
        df = pd.read_csv(metadata)
        cols = df.columns
        assert len(sam_file_locs) == len(df)

        for i in range(len(sam_file_locs)):
            sam_df = samReader(sam_file_locs[i])
            sam_df = samExtender(sam_df)
            sam_df = filterSenseStrand(sam_df)
            
            md = df.loc[i]
            for col in cols:
                sam_df[col] = md[col]

            print(sam_file_locs[i], "->", md[cols[0]])
            if type(out_df) == pd.core.frame.DataFrame:
                out_df = out_df.append(sam_df)
            else:
                out_df = sam_df
    else:
        for file in sam_file_locs:
            sam_df = samReader(file)
            sam_df = samExtender(sam_df)
            sam_df = filterSenseStrand(sam_df)

            sam_df["SAMPLE"] = file[file.rfind("/")+1:]

            if type(out_df) == pd.core.frame.DataFrame:
                out_df = out_df.append(sam_df)
            else:
                out_df = sam_df
            
            print(file, len(out_df))

    out_df.to_csv(outFile, index=False)

    return out_df






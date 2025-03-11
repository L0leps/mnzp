import pandas as pd

def round_and_save(input_file, output_file, decimals=3):
    df = pd.read_csv(input_file)
    df = df.round(decimals)
    df.to_csv(output_file, index=False)

round_and_save("CigarettesSW.csv", "CigarettesSW_rounded.csv", decimals=3)

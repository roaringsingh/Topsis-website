import pandas as pd
from topsispackage_prabhnoorsingh import topsis as tp


def file_topsis(f, d):
    df = pd.read_csv(f)
    w = [float(x) for x in d['weights'].split(',')]
    i = [x for x in d['impacts'].split(',')]
    try:
        df = tp.topsis_calc(df, w, i)
    except Exception:
        return pd.DataFrame()
    return df

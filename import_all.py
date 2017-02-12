import glob
from numpy import NaN
import pandas as pd

from stats_labels import ALL_NEIGHBORHOODS, CRIME_NAMES, HOOD_SPELLING_VARIATIONS, CRIME_SPELLING_VARIATIONS


def create_csts_skeleton(file_names):
    yearsm = {}
    for month_file in file_names:
        year_str, _, _ = month_file.split('/')[-1].split('_')
        yearsm[int(year_str)] = year_str
    years = sorted(yearsm.keys())
    crime2stat = dict(zip(CRIME_NAMES, [NaN] * len(CRIME_NAMES)))
    hood2crime = dict(zip(ALL_NEIGHBORHOODS, [crime2stat] * len(ALL_NEIGHBORHOODS)))
    month2hood = dict(zip(range(1, 13), [hood2crime] * 12))
    return dict(zip(years, [month2hood] * len(years)))


def loadm():
    xl_files = sorted(glob.glob('./data/20*.xls*'))
    csts = create_csts_skeleton(xl_files)
    skipped_crime_stat = {}
    for month_file in xl_files:
        print "loading", month_file
        year_str, month_str, _ = month_file.split('/')[-1].split('_')
        year = int(year_str)
        month = int(month_str)
        months_stats = csts.get(year)

        xl = pd.ExcelFile(month_file)
        current_month_sheet_name = xl.sheet_names[0]
        df = xl.parse(current_month_sheet_name)
        y, x = df.shape
        hoods = df.icol(0)
        for xx in range(x):
            local_crime = df.icol(xx).name.lower()
            canonical_crime = CRIME_SPELLING_VARIATIONS.get(local_crime)
            if canonical_crime:
                for i, hood in enumerate(hoods):
                    if isinstance(hood, float):
                        continue
                    hood = hood.strip().upper()
                    stat = df.icol(xx).iloc[i]
                    if months_stats[month].get(hood):
                        if not stat:  # some stats zero = empty cell
                            stat = 0
                        months_stats[month][hood][canonical_crime] = stat
                    else:
                        alt_hood = HOOD_SPELLING_VARIATIONS.get(hood)
                        if alt_hood and months_stats[month].get(alt_hood):
                            months_stats[month][alt_hood][canonical_crime] = stat
                        else:
                            print("skipping: no '{}' found in {}".format(hood, month_file))
        print '=' * 20
        print ' ' * 20
    return csts

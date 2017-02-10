import glob
from numpy import NaN
import pandas as pd

from stats_labels import ALL_NEIGHBORHOODS, CRIME_NAMES, UNIFIED_MAPPING


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
    xl_files = sorted(glob.glob('./data/20*.xlsx'))
    csts = create_csts_skeleton(xl_files)
    for month_file in xl_files:
        print month_file
        print '=' * 20
        print ' ' * 20
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
            crime = df.icol(xx).name.lower()
            if crime in CRIME_NAMES:
                for i, hood in enumerate(hoods):
                    stat = df.icol(xx).iloc[i]
                    hood = hood.strip()
                    if months_stats[month].get(hood):
                        months_stats[month][hood][crime] = stat
                    else:
                        alt_hood = UNIFIED_MAPPING.get(hood)
                        if alt_hood and months_stats[month].get(alt_hood):
                            months_stats[month][alt_hood][crime] = stat
                        else:
                            raise Exception("skipping: no '{}' in \n{}".format(hood, sorted(months_stats[month].keys())))
    return csts

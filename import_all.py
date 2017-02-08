import glob
from numpy import NaN
import pandas as pd

from stats_labels import ALL_NEIGHBORHOODS, CRIME_NAMES


def create_csts_skeleton():
    crime2stat = dict(zip(CRIME_NAMES, [NaN] * len(CRIME_NAMES)))
    hood2crime = dict(zip(ALL_NEIGHBORHOODS, [crime2stat] * len(ALL_NEIGHBORHOODS)))
    month2hood = dict(zip(range(1, 13), [hood2crime] * 12))
    years = range(2000, 2018)
    return dict(zip(years, [month2hood] * len(years)))


def loadm():
    csts = create_csts_skeleton()
    xl_files = sorted(glob.glob('./data/20*.xlsx'))
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
                    print hood
                    stat = df.icol(xx).iloc[i]
                    if months_stats[month].get(hood):
                        months_stats[month][hood][crime] = stat
                    else:
                        print "skipping: no {} in \n{}".format(hood, months_stats[month])
    return csts

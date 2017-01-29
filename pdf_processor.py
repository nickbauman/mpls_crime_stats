from pdf_util import convert_pdf_to_txt_as_pages
import csv

NEIGHBORHOODS_A = ['ARMATAGE',
    'AUDUBON PARK',
    'BANCROFT',
    'BELTRAMI',
    'BOTTINEAU',
    'BRYANT',
    'BRYN - MAWR',
    'CARAG',
    'CEDAR - ISLES - DEAN',
    'CEDAR RIVERSIDE',
    'CENTRAL',
    'CLEVELAND',
    'COLUMBIA PARK',
    'COMO',
    'COOPER',
    'CORCORAN',
    'DIAMOND LAKE',
    'DOWNTOWN EAST',
    'DOWNTOWN WEST',
    'EAST HARRIET',
    'EAST ISLES',
    'EAST PHILLIPS',
    'ECCO',
    'ELLIOT PARK',
    'ERICSSON',
    'FIELD',
    'FOLWELL',
    'FULTON',
    'HALE',
    'HARRISON',
    'HAWTHORNE',
    'HIAWATHA',
    'HOLLAND',
    'HOWE',
    'JORDAN',
    'KEEWAYDIN',
    'KENNY',
    'KENWOOD',
    'KING FIELD',
    'LIND - BOHANON',
    'LINDEN HILLS',
    'LOGAN PARK',
    'LONGFELLOW',
    'LORING PARK',
    'LOWRY HILL']

NEIGHBORHOODS_B = ['LOWRY HILL EAST',
    'LYNDALE',
    'LYNNHURST',
    'MARCY HOLMES',
    'MARSHALL TERRACE',
    'MCKINLEY',
    'MID - CITY INDUSTRIAL',
    'MIDTOWN PHILLIPS',
    'MINNEHAHA',
    'MORRIS PARK',
    'NEAR - NORTH',
    'NICOLLET ISLAND - EAST BANK',
    'NORTH LOOP',
    'NORTHEAST PARK',
    'NORTHROP',
    'PAGE',
    'PHILLIPS WEST',
    'POWDERHORN PARK',
    'PROSPECT PARK - EAST RIVER ROAD',
    'REGINA',
    'SEWARD',
    'SHERIDAN',
    'SHINGLE CREEK',
    'ST. ANTHONY EAST',
    'ST. ANTHONY WEST',
    'STANDISH',
    'STEVENS SQUARE - LORING HEIGHTS',
    'SUMNER - GLENWOOD',
    'TANGLETOWN',
    'UNIVERSITY OF MINNESOTA',
    'VENTURA VILLAGE',
    'VICTORY',
    'WAITE PARK',
    'WEBBER - CAMDEN',
    'WENONAH',
    'WEST CALHOUN',
    'WHITTIER',
    'WILLARD - HAY',
    'WINDOM',
    'WINDOM PARK']

ALL_NEIGHBORHOODS = NEIGHBORHOODS_A + NEIGHBORHOODS_B

CRIME_NAMES = ['total', 'homicide', 'rape', 'robbery', 'aggassault', 'burglary', 'larceny', 'autotheft', 'arson']


def _remove_blanks(page_text):
    lines = page_text.splitlines()
    return filter(lambda x: x != '', lines)


def mine_pdf(path):
    pages_text = convert_pdf_to_txt_as_pages(path, 2)
    assert len(pages_text) == 2
    crime_to_stat_map = {}
    neighborhoods = [NEIGHBORHOODS_A, NEIGHBORHOODS_B]

    blanks_removed = _remove_blanks(pages_text[0])

    # Page 1 has the stats at index 4
    neigh_a_idx = 4

    for x, crime in enumerate(CRIME_NAMES):
        offset = x * len(neighborhoods[0]) + neigh_a_idx
        for stat in blanks_removed[offset:len(neighborhoods[0]) + offset]:
            if crime_to_stat_map.get(crime):
                crime_to_stat_map[crime].append(stat)
            else:
                crime_to_stat_map[crime] = [stat]

    blanks_removed = _remove_blanks(pages_text[1])

    # Page 2 has the stats at len(neighborhoods[1]) + neigh_a_idx + 1
    neigh_a_idx = len(neighborhoods[1]) + neigh_a_idx + 1

    for x, crime in enumerate(CRIME_NAMES):
        offset = x * len(neighborhoods[1]) + neigh_a_idx
        for stat in blanks_removed[offset:len(neighborhoods[1]) + offset]:
            if crime_to_stat_map.get(crime):
                crime_to_stat_map[crime].append(stat)
            else:
                crime_to_stat_map[crime] = [stat]
    return crime_to_stat_map


def write_csv(source_path):
    crime_map = mine_pdf(source_path)
    dest_path = '{}.csv'.format('.'.join(source_path.split('.')[:-1]))
    with open(dest_path, 'wb') as fd:
        writer = csv.writer(fd, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        heading = ['neighborhood'] + CRIME_NAMES
        writer.writerow(heading)
        for i, hood in enumerate(ALL_NEIGHBORHOODS):
            row_data = [hood]
            for cn in CRIME_NAMES:
                stats = crime_map[cn]
                stat = stats[i]
                row_data.append(stat)
            writer.writerow(row_data)


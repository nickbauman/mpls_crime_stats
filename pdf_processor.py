from pdf_util import convert_pdf_to_txt_as_pages

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


def mine_pdf(path):
    pages_text = convert_pdf_to_txt_as_pages(path)
    assert len(pages_text) == 2
    crime_to_stat_map = {}
    neighborhoods = [NEIGHBORHOODS_A, NEIGHBORHOODS_B]
    for i, page_text in enumerate(pages_text):
        lines = page_text.splitlines()
        blanks_removed = filter(lambda x: x != '', lines)
        crime_names = blanks_removed[3].split()
        neigh_a_idx = 4
        for x, crime in enumerate(crime_names):
            offset = x * len(neighborhoods[i]) + neigh_a_idx
            for stat in blanks_removed[offset:len(neighborhoods[i]) + offset]:
                if crime_to_stat_map.get(crime):
                    crime_to_stat_map[crime].append(stat)
                else:
                    crime_to_stat_map[crime] = [stat]
    return crime_to_stat_map

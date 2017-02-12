NEIGHBORHOODS_A = ['ARMATAGE',
    'AUDUBON PARK',
    'BANCROFT',
    'BELTRAMI',
    'BOTTINEAU',
    'BRYANT',
    'BRYN - MAWR',
    'CAMDEN INDUSTRIAL',  # introduced
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
    'HUMBOLDT INDUSTRIAL AREA',
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
    'NORTH RIVER IND. AREA',  # combined with McKinley in 1996
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

HOOD_SPELLING_VARIATIONS = {'BRYN-MAWR': 'BRYN - MAWR',
    'CAMDEN IND. AREA': 'CAMDEN INDUSTRIAL',
    'CEDAR-ISLES-DEAN': 'CEDAR - ISLES - DEAN',
    'CEDAR-RIVERSIDE': 'CEDAR RIVERSIDE',
    'COLUMBIA': 'COLUMBIA PARK',
    'FOWELL': 'FOLWELL',
    'HUMBOLDT IND. AREA': 'HUMBOLDT INDUSTRIAL AREA',
    'LIND-BOHANON': 'LIND - BOHANON',
    'MARCY-HOLMES': 'MARCY HOLMES',
    'MID-CITY INDUSTRIAL': 'MID - CITY INDUSTRIAL',
    'MINNEAHAHA': 'MINNEHAHA',
    'NEAR NORTH': 'NEAR - NORTH',
    'NICOLLET ISLAND': 'NICOLLET ISLAND - EAST BANK',
    'NORTH RIVER IND. AREA': 'NORTH RIVER IND. AREA',
    'NORTHRUP': 'NORTHROP',
    'PHILLIPS EAST': 'EAST PHILLIPS',
    'PHILLIPS MIDTOWN': 'MIDTOWN PHILLIPS',
    'PROSPECT PARK': 'PROSPECT PARK - EAST RIVER ROAD',
    'PROSPECT PARK - EAST RIVER RD': 'PROSPECT PARK - EAST RIVER ROAD',
    'STEVENS SQUARE': 'STEVENS SQUARE - LORING HEIGHTS',
    "STEVEN'S SQUARE - LORING HEIGHTS": 'STEVENS SQUARE - LORING HEIGHTS',
    'STEVENS SQUARE - LORING HGTS': 'STEVENS SQUARE - LORING HEIGHTS',
    'SUMNER GLENWOOD': 'SUMNER - GLENWOOD',
    'U OF M': 'UNIVERSITY OF MINNESOTA',
    'WEBBER-CAMDEN': 'WEBBER - CAMDEN',
    'WILLARD-HAY': 'WILLARD - HAY'}

ALL_NEIGHBORHOODS = NEIGHBORHOODS_A + NEIGHBORHOODS_B

CRIME_NAMES = ['total', 'homicide', 'rape', 'robbery', 'aggassault', 'burglary', 'larceny', 'autotheft', 'arson']

CRIME_SPELLING_VARIATIONS = {'agg assault': 'aggassault',
    'agg assaults': 'aggassault',
    'aggassault': 'aggassault',
    'aggassaults': 'aggassault',
    'arson': 'arson',
    'aslt': 'aggassault',
    'auto theft': 'autotheft',
    'autotheft': 'autotheft',
    'burglary': 'burglary',
    'hom': 'homicide',
    'homcide': 'homicide',
    'homicide': 'homicide',
    'larceny': 'larceny',
    'mvt': 'autotheft',
    'rape': 'rape',
    'rob': 'robbery',
    'robbery': 'robbery',
    'theft': 'larceny'}

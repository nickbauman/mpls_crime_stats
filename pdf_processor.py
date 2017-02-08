from pdf_util import convert_pdf_to_txt_as_pages, convert_all_pdf_to_txt
import csv
from stats_labels import NEIGHBORHOODS_A, NEIGHBORHOODS_B, CRIME_NAMES, ALL_NEIGHBORHOODS


def _remove_blanks(page_text):
    lines = page_text.splitlines()
    return filter(lambda x: x != '', lines)


def xmine_pdf(path):
    pages_text = convert_pdf_to_txt_as_pages(path, 2)
    assert len(pages_text) == 2
    crime_to_stat_map = {}
    neighborhoods = [NEIGHBORHOODS_A, NEIGHBORHOODS_B]

    blanks_removed = _remove_blanks(pages_text[0])

    # Page 1 has the stats at index 4
    stats_begin = 4

    for x, crime in enumerate(CRIME_NAMES):
        offset = x * len(neighborhoods[0]) + stats_begin
        for stat in blanks_removed[offset:len(neighborhoods[0]) + offset]:
            if crime_to_stat_map.get(crime):
                crime_to_stat_map[crime].append(stat)
            else:
                crime_to_stat_map[crime] = [stat]

    blanks_removed = _remove_blanks(pages_text[1])

    # Page 2 has the stats at len(neighborhoods[1]) + neigh_a_idx + 1
    stats_begin = len(neighborhoods[1]) + stats_begin + 1

    for x, crime in enumerate(CRIME_NAMES):
        offset = x * len(neighborhoods[1]) + stats_begin
        for stat in blanks_removed[offset:len(neighborhoods[1]) + offset]:
            if crime_to_stat_map.get(crime):
                crime_to_stat_map[crime].append(stat)
            else:
                crime_to_stat_map[crime] = [stat]
    return crime_to_stat_map, pages_text


def mine_pdf(path):
    pages_text = convert_pdf_to_txt_as_pages(path, 2)
    compact_texts = map(_remove_blanks, pages_text)
    compact_text = compact_texts[0] + compact_texts[1]
    crime_to_stat_map = {}
    stats = []
    for item in compact_text:
        try:
            stat = int(item)
            stats.append(stat)
        except ValueError:
            continue

    offset = 0
    for crime in CRIME_NAMES:
        extent = offset + len(NEIGHBORHOODS_A)
        for stat in stats[offset:extent]:
            if crime_to_stat_map.get(crime):
                crime_to_stat_map[crime].append(stat)
            else:
                crime_to_stat_map[crime] = [stat]
        offset += len(NEIGHBORHOODS_A)

    for crime in CRIME_NAMES:
        extent = offset + len(NEIGHBORHOODS_B)
        for stat in stats[offset:extent]:
            if crime_to_stat_map.get(crime):
                crime_to_stat_map[crime].append(stat)
            else:
                crime_to_stat_map[crime] = [stat]
        offset += len(NEIGHBORHOODS_B)

    assert len(crime_to_stat_map) == len(CRIME_NAMES), 'expected {} but was {} :\n{}'.format(len(CRIME_NAMES),
        len(crime_to_stat_map), crime_to_stat_map)

    return crime_to_stat_map, pages_text


def write_csv(source_path):
    crime_map, pages_text = mine_pdf(source_path)
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
    return crime_map, pages_text

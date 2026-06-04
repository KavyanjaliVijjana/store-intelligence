LEFT_SHELF = (0, 100, 300, 900)
RIGHT_SHELF = (650, 100, 960, 900)
CENTER_AREA = (300, 250, 650, 950)

ZONES = {
    "left_shelf": LEFT_SHELF,
    "right_shelf": RIGHT_SHELF,
    "center_area": CENTER_AREA
}


def get_zone(x, y):

    for zone_name, (x1, y1, x2, y2) in ZONES.items():

        if x1 <= x <= x2 and y1 <= y <= y2:
            return zone_name

    return None
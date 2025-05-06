"""
Environment variables for the project.
"""

# Map of German literary movements
MOVEMENT_MAP = {
    (1050, 1350): "Middle High German",
    (1351, 1600): "Late Medieval/Early Modern",
    (1601, 1720): "Baroque",
    (1721, 1780): "Enlightenment",
    (1765, 1785): "Sturm und Drang",
    (1786, 1805): "Weimar Classicism",
    (1795, 1840): "Romanticism",
    (1841, 1900): "Realism/Naturalism",
    (1901, 1945): "Expressionism/Modernism",
}


def get_period(year: int) -> str:
    for (start, end), period in MOVEMENT_MAP.items():
        if start <= year <= end:
            return period
    return "Unknown"

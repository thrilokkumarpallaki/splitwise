from enum import StrEnum


class SplitType(StrEnum):
    EQUAL_SPLIT = 'EQUAL'
    EXACT_SPLIT = 'EXACT'
    PERCENTAGE_SPLIT = 'PERCENTAGE'
    RATIO_SPLIT = 'RATIO'

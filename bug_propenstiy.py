from math import exp


def bug_propensity_raw(timestamp):
    """
    Computes raw bug-propensity value based on timestamp
    :param timestamp:
    :return: bug-propensity raw value
    """
    large_time_cons = 150 * (10 ** 7)
    return 1 / float(1 + exp(-12 * timestamp / large_time_cons + 12))


def bug_propensity_percentage(raw_value):
    """
    Computes percentage bug-propensity from raw value
    :param raw_value:
    :return: bug-propensity percentage
    """
    return (1 - (2 / (1 + exp(0.2*raw_value))))*100

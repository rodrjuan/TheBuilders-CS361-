import statistics

def calculate_mean(*args):
    return statistics.mean(args)

def calculate_median(*args):
    return statistics.median(args)

def calculate_mode(*args):
    try:
        return statistics.mode(args)
    except statistics.StatisticsError:
        return "No mode found."

def calculate_variance(*args):
    return statistics.variance(args)

def calculate_std_dev(*args):
    return statistics.stdev(args)

def calculate_range(*args):
    return max(args) - min(args)

def calculate_quantiles(*args):
    quantiles = statistics.quantiles(args, n=4)
    return quantiles[0], quantiles[1], quantiles[2]

from statistics import mean, median


def calculate_stats(forecasts):
    if not forecasts:
        return {}
    return {
        "maximum": max(forecasts),
        "minimum": min(forecasts),
        "average": mean(forecasts),
        "median": median(forecasts),
    }

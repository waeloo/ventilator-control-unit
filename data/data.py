import core
from data_io import printjson

def metrics_to_dictionary(metrics):
    metrics_dictionary = {}

    for key in metrics:
        metrics_dictionary.update(metrics[key].to_dictionary())

    return metrics_dictionary


def metrics_from_dictionary(metrics_dictionary):
    metrics = {}

    for key in metrics_dictionary:
        metric = core.Metric.from_dictionary(metrics_dictionary[key])
        metrics.update({metric.id: metric})

    return metrics



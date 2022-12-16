>>> import statistics
>>> data = [13, 17, 23, 15, 21, 6, 18, 37, 25, 23, 47, 19, 26, 24, 17, 24, 83, 8, 15, 29]
>>> statistics.__all__
['NormalDist', 'StatisticsError', 'fmean', 'geometric_mean', 'harmonic_mean', 'mean', 'median', 'median_grouped', 'median_high', 'median_low', 'mode', 'multimode', 'pstdev', 'pvariance', 'quantiles', 'stdev', 'variance']
>>> sum(data) / len(data)
24.5
>>> statistics.mean(data)
24.5
>>> statistics.median(data)
22.0
>>> statistics.mode(data)
17
>>> statistics.stdev(data)
16.602155852399665
>>> statistics.variance(data)
275.63157894736844
>>> statistics.quantiles(data)
[15.5, 22.0, 25.75]
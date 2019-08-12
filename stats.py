import pstats
stats = pstats.Stats('function.profile')
stats.strip_dirs().sort_stats('time').print_stats()
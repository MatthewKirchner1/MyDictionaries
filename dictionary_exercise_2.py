# Open file and create string
winners_file = open("WorldSeriesWinners.txt", "r")
winners_string = winners_file.read()

# Create list of winners
winners_list = winners_string.split("\n")

# Create list of distnct winners
distinct_winners_set = set(winners_list)
distinct_winners_list = list(distinct_winners_set)

# Create dictionary for years and add values
world_series_winners_by_yr = {}

year = 1903
i = 0

for year in range(1903, 2009):

    if year == 1904 or year == 1994:
        world_series_winners_by_yr[year] = "No World Series"

    else:
        world_series_winners_by_yr[year] = winners_list[i]
        i += 1

# Create dictionary for winner frequency
world_series_winners_by_freq = {}

for x in distinct_winners_list:
    world_series_winners_by_freq[x] = distinct_winners_list.count(x)

from catchment.models import read_variable_from_csv, daily_stats, daily_std
from catchment.views import boxplot


data = read_variable_from_csv('data/rain_data_small.csv')
data.shape

# test daily_stats(data)
daily_stats(data)

# test daily_std(data)
daily_std(data)

# test  boxplot(data_dict)
data_dict = {'Rainfall (mm)': data}
boxplot(data_dict)


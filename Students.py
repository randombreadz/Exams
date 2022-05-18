import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
gender_list = df["gender"].to_list()
math_score = df["math score"].to_list()

gender_mean = statistics.mean(gender_list)
math_mean = statistics.mean(math_score)

gender_median = statistics.median(gender_list)
math_median = statistics.median(math_score)

gender_mode = statistics.mode(gender_list)
math_mode = statistics.mode(math_score)

print("Mean, Median and Mode of gender is {}, {} and {} respectively".format(gender_mean, gender_median, gender_mode))
print("Mean, Median and Mode of math scores is {}, {} and {} respectively".format(math_mean, math_median, math_mode))

gender_std_deviation = statistics.stdev(gender_list)
math_std_deviation = statistics.stdev(math_score)

gender_first_std_deviation_start, gender_first_std_deviation_end = gender_mean-gender_std_deviation, gender_mean+gender_std_deviation
gender_second_std_deviation_start, gender_second_std_deviation_end = gender_mean-(2*gender_std_deviation), gender_mean+(2*gender_std_deviation)
gender_third_std_deviation_start, gender_third_std_deviation_end = gender_mean-(3*gender_std_deviation), gender_mean+(3*gender_std_deviation)

math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

gender_list_of_data_within_1_std_deviation = [result for result in gender_list if result > gender_first_std_deviation_start and result < gender_first_std_deviation_end]
gender_list_of_data_within_2_std_deviation = [result for result in gender_list if result > gender_second_std_deviation_start and result < gender_second_std_deviation_end]
gender_list_of_data_within_3_std_deviation = [result for result in gender_list if result > gender_third_std_deviation_start and result < gender_third_std_deviation_end]

math_list_of_data_within_1_std_deviation = [result for result in math_score if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_score if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_score if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

print("{}% of data for gender lies within 1 standard deviation".format(len(gender_list_of_data_within_1_std_deviation)*100.0/len(gender_list)))
print("{}% of data for gender lies within 2 standard deviations".format(len(gender_list_of_data_within_2_std_deviation)*100.0/len(gender_list)))
print("{}% of data for gender lies within 3 standard deviations".format(len(gender_list_of_data_within_3_std_deviation)*100.0/len(gender_list)))
print("{}% of data for math scores lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_score)))
print("{}% of data for math scores lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_score)))
print("{}% of data for math scores lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_score)))

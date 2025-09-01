import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

respondents_count = 50000

age = np.random.randint(low = 1, high = 100, size = (respondents_count))
income = np.random.normal(23000,10000,size = respondents_count)
satisfaction_rating = np.random.randint(low = 1, high = 10, size = respondents_count)
hobbies_hours = np.random.normal(10,5,size = respondents_count)

age_median = np.median(age)
print(age_median)

income_median = np.median(income)
print(income_median)

satisfaction_rating_median = np.median(satisfaction_rating)
print(satisfaction_rating_median)

hobbies_hours_median = np.median(hobbies_hours)
print(hobbies_hours_median)

survey_data = pd.DataFrame({"Age":age, "Income": income, "Satisfaction_Rating":satisfaction_rating, "Hobbies_Hours": hobbies_hours})
survey_data.head(20)

cov_satisfaction_hobbies = np.corrcoef(income, satisfaction_rating)[0,1]
print(cov_satisfaction_hobbies)

fig, axs = plt.subplots(2,2,constrained_layout = True)

plt.rc("font", family = "Serif")
fig.suptitle("Survery Data Visualization")

axs[0,0].hist(age, bins = 50)
axs[0,1].hist(income, bins = 50)
axs[1,0].hist(hobbies_hours, bins = 10)
axs[1,1].hist(satisfaction_rating, bins = 20)

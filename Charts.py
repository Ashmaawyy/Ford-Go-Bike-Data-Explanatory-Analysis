import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)

ford_data = pd.read_csv('201902-fordgobike-tripdata.csv')
# for faster computation I may use random samples of range 20,000 of the dataset in the plots
sample = np.random.choice(ford_data.shape[0], 20000, replace = False)
ford_data_subset = ford_data.iloc[sample]
def data_cleaning():
    ford_data.drop(columns = ['start_station_latitude', 'start_station_longitude', 'end_station_latitude', 'end_station_longitude'], axis = 1, inplace = True)
    ford_data['member_gender'].fillna(str(ford_data['member_gender'].mode()).replace(str(ford_data['member_gender'].mode()), 'Male'), inplace = True)
    ford_data['member_birth_year'].fillna(ford_data['member_birth_year'].mean().__round__(), inplace = True)
    ford_data.dropna(axis = 0, inplace = True)
    ford_data.info()


def gender_barplot():

    sns.countplot(data = ford_data, x = 'member_gender');

def gender_catblot():
    
    sns.catplot(data = ford_data_subset, x = 'member_gender', y = 'duration_sec');

def user_type_barplot():
    sns.countplot(data = ford_data, x = 'user_type');

def user_type_catplot():
    sns.catplot(data = ford_data_subset, x = 'user_type', y = 'duration_sec');

def user_birth_year_hist():
    bins = np.arange(1930, ford_data['member_birth_year'].max(), 10)
    plt.xlabel('Years of Birth')
    plt.ylabel('Count')
    plt.hist(ford_data['member_birth_year'], bins = bins);
    plt.axvline(ford_data['member_birth_year'].mean().__round__(), color = 'red')
    plt.axvline(ford_data['member_birth_year'].max(), color = 'black')
    plt.legend(['Mean', 'Max']);
    plt.show()

def user_birth_year_duration_plot():
    sns.regplot(data = ford_data_subset, y = 'member_birth_year', x = 'duration_sec');


def user_age_gender_duration():
    ttype_markers = [['Male', '^'], ['Female', 'p'], ['Other', 'o']]

    for ttype, marker in ttype_markers:
        plot_data = ford_data_subset.loc[ford_data_subset['member_gender'] == ttype]
        sns.regplot(data = plot_data, x = 'duration_sec', y = 'member_birth_year', marker = marker, fit_reg = False)
        plt.legend(['Males', 'Females', 'Other']);


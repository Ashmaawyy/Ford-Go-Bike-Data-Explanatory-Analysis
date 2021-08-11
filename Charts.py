import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ford_data = pd.read_csv('201902-fordgobike-tripdata.csv')
def data_cleaning():
    ford_data.drop(columns = ['start_station_latitude', 'start_station_longitude', 'end_station_latitude', 'end_station_longitude'], axis = 1, inplace = True)
    ford_data['member_gender'].fillna(str(ford_data['member_gender'].mode()).replace(str(ford_data['member_gender'].mode()), 'Male'), inplace = True)
    ford_data['member_birth_year'].fillna(ford_data['member_birth_year'].mean().__round__(), inplace = True)
    ford_data.dropna(axis = 0, inplace = True)
    ford_data.info()


def gender_barplot():

    sns.countplot(data = ford_data, x = 'member_gender');

def gender_catblot():
    
    sns.catplot(data = ford_data, x = 'member_gender', y = 'duration_sec');

def user_type_barplot():
    sns.countplot(data = ford_data, x = 'user_type');

def user_type_catplot():
    sns.catplot(data = ford_data, x = 'user_type', y = 'duration_sec');

def user_birth_year_hist():
    bins = np.arange(1930, ford_data['member_birth_year'].max(), 10)
    plt.axvline(ford_data['member_birth_year'].mean().__round__(), color = 'red')
    plt.axvline(ford_data['member_birth_year'].max(), color = 'black')
    plt.hist(ford_data['member_birth_year'], bins = bins);

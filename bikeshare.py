import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""Get user input - ask for the city the user wants to explore. Ask if they want to filter by month or day of week."""
def get_filters():
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input('What city would you like to know more about: Chicago, New York City or Washington? ')
        if city.lower() in cities:
            break
        else:
            print('Please enter city as shown.')
    while True:
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = input('Would you like to filter by month? If not, enter: all. If you would like data by month, enter: Jan, Feb, Mar, Apr, May or Jun (as shown). ')
        if month.lower() in months:
            break
        else:
            print('Please enter city as shown.')
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input('Would you like to filter by day of week? If not, enter: all. If you would like data by day, enter: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday (as shown). ')
        if day.lower() in days:
            break
        else:
            print('Please enter city as shown.')

    print('Great! Let\'s learn more about {}!'.format(city.title()))

    print('-'*40)
    return city, month, day

"""Read data from csv files and create month, day and hour columns from 'Start Time' column.  Filters by month and day if applicable."""
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['jan','feb','mar','apr','may','jun']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

"""Display statistics on the most frequent times of travel - most common month, day of week and hour."""
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print('The most popular month is: ', popular_month)

    popular_day = df['day'].mode()[0]
    print('The most popular day is: ', popular_day)

    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""Display the most commonly used start station, end station and trip. Trip is a new field by concatenating start and end station."""
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start = df['Start Station'].mode()[0]
    print('The most popular start station is: ', popular_start)

    popular_end = df['End Station'].mode()[0]
    print('The most popular end station is: ', popular_end)

    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print('The most popular trip is: ', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""Display the total and mean travel time."""
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel = df['Trip Duration'].sum()
    print('Total travel time is: ', total_travel)

    mean_travel = df['Trip Duration'].mean()
    print('Average travel time is: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""Display counts of users types, gender and earliest, latest and most common birth year."""
def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('The number of users per user type is: ', user_types)

    while True:
        if 'Gender' in df.columns:
            gender = df['Gender'].value_counts()
            print('The breakdown of gender is: ', gender)
            break
        else:
            break
    while True:
        if 'Birth Year' in df.columns:
            earliest_yob = df['Birth Year'].min()
            most_recent_yob = df['Birth Year'].max()
            most_common_yob = df['Birth Year'].mode()[0]
            print('The earliest birth year is {}. The most recent birth year is {}. And the most common birth year is {}.'.format(earliest_yob, most_recent_yob, most_common_yob))
            break
        else:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""Ask the user if they would like to see the first 5 rows and data. If yes, display first 5 rows.  If no, move on."""
def viewable_df(df):
    while True:
        raw_data = input('\nWould you like to see the first 5 rows of raw data behind these statistics? Enter yes or no.\n')
        if raw_data.lower() == 'yes':
            print(df.head())
            break
        else:
            break

"""Main code block - run each definition as defined above. Then ask user if they would like to restart the program."""
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        viewable_df(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

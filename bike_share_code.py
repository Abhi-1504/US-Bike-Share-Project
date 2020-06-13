import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago', 'new york city', 'washington']
        # lower() method use to avoid case sensitivity related exception
        city = input("Please enter the city you want the data for (Chicago, New York City, Washington) : ").lower()
        if city in cities:
            # Extra layer for confirmation on filter
            option = input("Please confirm whether {} is the city for which you want data from (y/n) : ".format(city)).lower()
            if option == 'y':
                break
            else:
                continue
        else:
            print("Sorry, you seem to have entered an incorrect city. Please try again. Pssst! Check for Typos..")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
         months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
         # lower() method use to avoid case sensitivity related exception
         month = input("Please enter the month you want the data for (All, January, February, ... , June) : ").lower()
         if month in months:
            # Extra layer for confirmation on filter
             option = input("Please confirm whether {} is the month for which you want data from. (y/n) : ".format(month)).lower()
             if option == 'y':
                break
             else:
                continue
         else:
            print("Sorry, you seem to have entered an incorrect month. Please try again. Pssst! Check for Typos..")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
         days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
         # lower() method use to avoid case sensitive related exception
         day = input("Please enter the day you want the data for ('All', 'Monday', 'Tuesday', ... 'Sunday') : ").lower()
         if day in days:
            # Extra layer for confirmation on filter
             option = input("Please confirm whether {} is the day for which you want the data from. (y/n) : ".format(day)).lower()
             if option == 'y':
                break
             else:
                continue
         else:
            print("Sorry, you seem to have entered an incorrect day. Please try again. Pssst! Check for Typos..")

    print('-'*100)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Loading the csv data file of the selected city in the panda DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Coverting the start time into datetime format for further statistical caluclation
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting month and weekdays from the start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Converting input month and day filters into numerical value and filtering out data as per the raw input filters

    # Month filter conversion
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Creating a new dataframe by filtering out data by month
        df = df[df['month'] == month]

    # Day filter conversion
    if day != 'all':
        # Creating a new dataframe by filtering out data by day
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # Checking if no month filter is applied
    months = ['january', 'february', 'march', 'april', 'may','june']
    if len(df['month'].unique()) == 1:
        #converting into month name
        month = months[df['month'].unique()[0] - 1].title()
        print("You have queried for Single month data for the month of",month)
    # Calculating Most common month in the data
    else:
        most_common_month = months[df['month'].mode()[0] -1]
        print('The most common month is :', most_common_month)

    # TO DO: display the most common day

    # Checking if no day filter is applied
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if len(df['day_of_week'].unique()) == 1:
        # Converting into month name
         print("You have queried for Single day data for the day of", ''.join(df['day_of_week'].unique()))
    # Calculating Most common day in the data
    else:
        most_common_day = df['day_of_week'].value_counts().idxmax()
        print('The most common day is :', most_common_day)
    # TO DO: display the most common start hour
    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extracting hour from the Start Time column and creating an hour column
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # Filtering out the max entry of a start station in the data
    most_commonly_used_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is :', most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    # Filtering out the max ntry of a start station in the data
    most_commonly_used_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is :', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    # Filtering out the most frequent combination of start and end station, using underscore as the symbol to seperate both the station afterwards
    most_frequent_start_and_end_station = df['Start Station'] + '_' + df['End Station']
    most_frequent_start_and_end_station = most_frequent_start_and_end_station.value_counts().idxmax()
    print('The most frequent combination of start station and end station is : \n Start: {} \t End: {}'.format(most_frequent_start_and_end_station.split('_')[0],most_frequent_start_and_end_station.split('_')[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration statistics...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # Calculating total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time)
    # TO DO: display mean travel time

    # Calculating average travel time
    total_travel_time = df['Trip Duration'].mean()
    print('The average travel time is:', total_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('The counts of user stats are :\n\n')
    # TO DO: Display counts of user types

    # Creating a pandas series of unique user types
    user_type_list = df['User Type'].value_counts()
    print(user_type_list.to_frame(),'\n\n')

    # TO DO: Display counts of gender

    # Validation of existence of gender column in the dataframe if it exists
    if 'Gender' in df.columns:
        # Calculating the count of Gender
        Gender_list = df['Gender'].value_counts().dropna()
        print(Gender_list.to_frame(),'\n')
    else:
        print('No Gender Data to display...')

    # TO DO: Display earliest, most recent, and most common year of birth

    #Checking if the column exist in the dataframe
    if 'Birth Year' in df.columns:
        #Creating a year list series and dropping empty values
        Year_list = df['Birth Year'].dropna()

        #Calculating oldest birth Year
        oldest_birth_year = min(Year_list)
        print('The oldest birth year is :',oldest_birth_year)

        #Calculating youngest birth year
        youngest_birth_year = max(Year_list)
        print('The youngest birth year is:',youngest_birth_year)

        #Calculating the most common year of oldest_birth_year
        common_birth_year = Year_list.mode()
        print('The most coomon year of birth is :',common_birth_year[0])

    else:
        print('No Birth year data to display')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

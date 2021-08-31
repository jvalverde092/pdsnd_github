import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def filter_month():
    month = None
    bool_good_option = False
    while(not(bool_good_option)):
        month = (input('Choone one month option : (january, february, march, april, may, june)\n')).lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june']:
            print("Incorrec option, choose again\n")
        else:
            bool_good_option = True
    return month

def filter_day():
    day = None
    bool_good_option = False
    while(not(bool_good_option)):
        day = (input('Choone one day-of-week option : (monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n')).lower()
        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print("Incorrec option, choose again\n")
        else:
            bool_good_option = True
    return day

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
    city = None
    bool_good_option = False
    while(not(bool_good_option)):
        city = (input('Whould you like to see data for : (chicago, new york city, washington)?\n')).lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Incorrec option, choose again\n")
        else:
            bool_good_option = True
            
    filter_month_year = None       
    bool_filter_month_day = False
    while(not(bool_filter_month_day)):
        filter_month_day = (input('Whould you like to filter the data by month, day, both or not at all? Type "none" for no time filter\n')).lower()
        if filter_month_day not in ['month', 'day', 'both', 'none']:
            print("Incorrec option, choose again\n")
        else:
            bool_filter_month_day = True    
    
    if filter_month_day == 'none':
        print('-'*40)
        return city, 'all', 'all'
    else:
        month = 'all'
        day = 'all'
        if filter_month_day == 'month' or filter_month_day == 'both':
            # TO DO: get user input for month (all, january, february, ... , june)
            month = filter_month()
        if filter_month_day == 'day' or filter_month_day == 'both':
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = filter_day()
        print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print("The most popular month is : {}".format(months[df['month'].mode()[0]-1]))

    # TO DO: display the most common day of week
    print("The most popular day-of-week is : {}".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("The most popular hour is : {} h".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most popular start station is : {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most popular end station is : {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = (df['Start Station'] + '__' + df['End Station']).mode()[0]
    print("The most popular start station - end station is : {} - {}".format(start_end_station.split('__')[0], start_end_station.split('__')[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is : {}".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("The mean travel time is : {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The count of user types is :\n{}".format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    try:
        print("The count of user types is :\n{}".format(df['Gender'].value_counts()))
    except:
        print("There isn't gender column")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth is : {}".format(int(df['Birth Year'].min())))
        print("The most recetn year of birth is : {}".format(int(df['Birth Year'].max())))
        print("The most common year of birth is : {}".format(int(df['Birth Year'].mode()[0])))
    except:
        print("There isn't year of birth column")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_raw_data(df):
    i = 0
    while True:
        df1 = df.iloc[i*5:(i+1)*5,:]
        print(df1)
        i += 1
        continue_ans = (input('Would yo like to view individual trip data (yes or no)?\n')).lower()
        if continue_ans != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        print_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

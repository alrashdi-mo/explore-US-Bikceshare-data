import time
import pandas as pd
from search_tool import search # call search function from search_tool.py script

# global raw_df
CITY_DATA = { 'chicago': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities_list =["chicago", "nyc", "washington"]
    monthes_list= ["all", 'january', 'february', 'march', 'april', 'may', 'june']
    days_list= ["all", "monday", "tuesday","wednesday", "thursday","friday", "saturday", "sunday"]

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). 
    
    city = str(input("Please Enter City to filter ('Chicago', 'NYC', 'Washington') : ")).lower()
    while city not in cities_list:
        city = str(input("Sorry!, please enter a valid city name again ('Chicago', 'NYC', 'Washington') : ")).lower()
        
    # get user input for month (all, january, february, ... , june)
    month = str(input("Please enter month to filter (all, january, february, ... , june) : ")).lower()
    while month not in monthes_list:
        month = str(input("Sorry!, please enter a valid Month (all, or any month from january-june) : ")).lower()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("Please Enter day to filter (all, monday, tuesday,..) : ")).lower()
    while day.lower() not in days_list:    
          day = str(input("Sorry!, Please Enter a valid day (all, or any day from monday-sunday) : ")).lower()


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
    import sys
    try:
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError:
        print(f"Error: The file '{CITY_DATA[city]}' does not exist.")
        exit()
    except PermissionError:
        print(f"Insufficient permission to read {CITY_DATA[city]}!")
        exit()   
        
    global raw_df
    raw_df = df # assign raw data
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # extract hours from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    # extract hours from Start Time to create new columns
    df['year'] = df['Start Time'].dt.year
    #round duration values to ease the use of search tool 
    df['Trip Duration'] = df['Trip Duration'].round()
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
        df = df.loc[df['day_of_week'] == day.title()]
        # df.to_csv('final.csv')
    return df 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # df['month']=list(df['month'])
    # display the most common month
    most_common_month = df['month'].mode()[0]
    
    # display the most common day of week
    most_common_week = df['day_of_week'].mode()[0]
    
    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    
    print(' The most common month is {}'.format(int(most_common_month)))
    print(' The most common day of the week is {}'.format(str(most_common_week)))
    print(' The most common hour is {}'.format(int(most_common_hour)))
    print(' This took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start and end station trip
    
    most_common_start_end_station = df['Start Station'] + " to " +  df['End Station']
    most_common_start_end_station = most_common_start_end_station.mode()[0]  
    
    
    
    print(' The most common start station is {}'.format(str(most_common_start_station)))
    print(' The most common end station is {}'.format(str(most_common_end_station)))
    print(' The most common combination station trip : \n {}'.format(str(most_common_start_end_station)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()

    print('The total travel time is {}'.format(round(total_travel_time)))
    print('The average travel time is {}'.format(round(average_travel_time)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # user_counts = df['User Type'].value_counts()
    count_users = df['User Type'].value_counts()
    print('Type of Users:')
    for index, count in enumerate(count_users):
        print("{}: {}".format(count_users.index[index], count))
    
    if 'Gender' in df.columns:
        user_gender(df)
    if 'Birth Year' in df.columns:
        user_birth_year(df)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_gender(df):
    """"Display counts of genders"""
    
    count_gender = df['Gender'].value_counts()
    print('\nType of Genders:')
    for index, type_count in enumerate(count_gender):
        print("{}: {}".format(count_gender.index[index], type_count))

def user_birth_year(df):    
    
    """Display earliest, most recent, and most common year of birth"""
    
    earliest_birth_year = df['Birth Year'].min()
    recent_birth_year = df['Birth Year'].max()
    common_birth_year = df['Birth Year'].mode()[0]
    
    print('\nThe earliest year of birth is {}'.format(int(earliest_birth_year)))
    print('The most recent year of birth is {}'.format(int(recent_birth_year)))   
    print('The most common year of birth is {}'.format(int(common_birth_year)))

next_lines = 5
def display_data(selected_data):
    """ Display data lines of raw/filtered data to the user """
    count_index = len(selected_data.index) + 1
    global next_lines
    while next_lines <= count_index:
        print_next =str(input('\nWould you like to see the first {} lines of the row data are:\n'.format(int(next_lines)))).lower()
        if print_next == 'yes':
            rows = selected_data.head(next_lines)
            print('The first {} lines of the row data are:\n'.format(int(next_lines)), rows)
            next_lines +=5
            continue
        elif print_next == 'no':
            next_lines = 5
            break
        else: print('___ Please Enter Yes or No ___')
    print('__ Sorry you reached the limit of {} ,There is no extra data to show! ___'.format(int(count_index))) 
             
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            select= int(input('Please select an Option:\n 1: View Raw Data\n 2: View Filtered Data\n 3: Advance Search Tool\n 4: Restart\n 5: Exit\n Select a number:'))
            if select == 1:
                display_data(raw_df)
            elif select == 2:
                display_data(df)
            elif select == 3:
                search(raw_df)
            elif select == 4:
                break
            elif select == 5:
                print('Goodbye!')
                exit()
            else:
                print('____ Please select a valid choice! ____')
        
if __name__ == "__main__":
	main()

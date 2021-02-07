import time
import pandas as pd
import numpy as np
from collections import Counter



df = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



months = ('all', 'january', 'february', 'june','july','march','may','april','august','September','october','November','December')
cities = ('chicago', 'new york city', 'washington')
days = ('all','monday', 'tuesday','sunday','thursday', 'friday','wednesday','saturday','sunday')
city= input('what is your city? ' ).lower()
while city not in cities :
      print ("we don't have data for this city ")
      break
month = input("what month or months you do biking ?(all, january, february, ... , june) ").lower()
while month not in months :
      print ('wrong input please try again')
      month = input("what month or months you do biking ?(all, january, february, ... , june) ")
day = input('what day you  bike ? (all, monday, tuesday, ... sunday) ').lower()
while day not in days :
    print ('wrong input please try again')
    day = input('what day you  bike ? (all, monday, tuesday, ... sunday) ')

def get_filters(city,month,day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    print('-'*40)
    return city, month, day
get_filters(city,month,day)

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


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if city == 'chicago':
        rc = pd.read_csv('chicago.csv')
#---------------------------------------
        #display the most common month

        rc['date'] = pd.to_datetime(rc['Start Time'])
        rc['month'] = rc['date'].dt.month
        yay = rc['month']
#-------------------------------------------------------
        #display the most common day of week

        rc['Start Time'] = pd.to_datetime(rc['Start Time'], format="%Y/%m/%d %H:%M:%S")
        rcn = rc['Start Time'].dt.weekday
        mostday = rc['Start Time'].dt.day_name()
        pla = mostday.value_counts()
        top=pla.idxmax()
#--------------------------------------------------
        #display the most common starting hour

        f = rc['Start Time'].dt.hour
        items_counts = f.value_counts()
#----------------------------------------------------
        print ('the most common month for biking in Chicago for the first six months of 2017 :{}\n'.format( yay.max()))
        print('the most common day of the week for biking in Chicago : {}\n'.format(top))
        print('the most common starting hour in Chicago is {}\n'.format(items_counts.idxmax()))

#----------------------------------------------------------------------------
    if city == 'new york city':
        rc = pd.read_csv('new_york_city.csv')
#-----------------------------
        #display the most common month

        rc['date'] = pd.to_datetime(rc['Start Time'])
        rc['month'] = rc['date'].dt.month
        yay = rc['month']
#-------------------------------------------------------
        #display the most common day of week

        rc['Start Time'] = pd.to_datetime(rc['Start Time'], format="%Y/%m/%d %H:%M:%S")
        rcn = rc['Start Time'].dt.weekday
        rcd = rc['Start Time'].dt.day_name()
        pla = rcd.value_counts()
        top=pla.idxmax()
#--------------------------------------------------
        #display the most common starting hour

        f = rc['Start Time'].dt.hour
        items_counts = f.value_counts()
#----------------------------------------------------
        print ('the most common month for biking in New York City for the first six months of 2017 : {}\n'.format( yay.max()))
        print('the most common day of the week for biking in New York City : {}\n'.format(top))
        print('the most common starting hour in New York City is {}\n'.format(items_counts.idxmax()))

#-----------------------------------------------------------

    if city == 'washington':
        rc = pd.read_csv('washington.csv')
#-----------------------------
        #display the most common month

        rc['date'] = pd.to_datetime(rc['Start Time'])
        rc['month'] = rc['date'].dt.month
        yay = rc['month']
#------------------------------------------
        #display the most common day of week

        rc['Start Time'] = pd.to_datetime(rc['Start Time'], format="%Y/%m/%d %H:%M:%S")
        rcn = rc['Start Time'].dt.weekday
        rcd = rc['Start Time'].dt.day_name()
        pla = rcd.value_counts()
        top=pla.idxmax()
#--------------------------------------------------
        #display the most common starting hour

        f = rc['Start Time'].dt.hour
        items_counts = f.value_counts()
#----------------------------------------------------
        print ('the most common month for biking in Washington for the first six months of 2017 : {}\n'.format( yay.max()))
        print('the most common day of the week for biking in Washington : {}\n'.format(top))
        print('the most common starting hour in Washington is {}\n'.format(items_counts.idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    breaktwo()
    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

#---------------------------------------------------------
    if city == 'chicago':
        rc = pd.read_csv('chicago.csv')
#------------------------------------------------
        #display most commonly used start station

        count_stations =rc['Start Station'].value_counts()
        top_station = count_stations.idxmax()
#-----------------------------------------
        #display most commonly used end station

        end_stations =rc['End Station'].value_counts()
        end_station = count_stations.idxmax()
#----------------------------------------------------
        #display most frequent combination of start station and end station trip

        rc['Trip'] = rc['Start Station'].str.cat(rc['End Station'],sep=" to ")# i joined the 2 columns together :)
        trips = rc['Trip'].value_counts() #count values
        most_trip = trips.idxmax()
#----------------------------------------------------------
        print('The most commonly used start station in Chicago is {}\n'.format(top_station))
        print('The most commonly used end station in Chicago is {}\n'.format(end_station))
        print('The most frequent combination of start station and end station trip in Chicago is : {}'.format(most_trip))

        #--------------------------------------


    if city == 'new york city':
        rc = pd.read_csv('new_york_city.csv')
#---------------------------------------------
        #display most commonly used start station

        count_stations =rc['Start Station'].value_counts()
        top_station = count_stations.idxmax()
#-----------------------------------------
        #display most commonly used end station

        end_stations =rc['End Station'].value_counts()
        end_station = count_stations.idxmax()
#----------------------------------------------------
        #display most frequent combination of start station and end station trip

        rc['Trip'] = rc['Start Station'].str.cat(rc['End Station'],sep=" to ")# i joined the 2 columns together :)
        trips = rc['Trip'].value_counts() #count values
        most_trip = trips.idxmax()
#----------------------------------------------------------
        print('The most commonly used start station in New York City is {}\n'.format(top_station))
        print('The most commonly used end station in New York City is {}\n'.format(end_station))
        print('The most frequent combination of start station and end station trip in New York City is : {}'.format(most_trip))

#--------------------------------------


    if city == 'washington':
        rc = pd.read_csv('washington.csv')
#-------------------------------------------
        #display most frequent combination of start station and end station trip

        count_stations =rc['Start Station'].value_counts()
        top_station = count_stations.idxmax()
#-----------------------------------------
        #display most commonly used end station

        end_stations =rc['End Station'].value_counts()
        end_station = count_stations.idxmax()
#----------------------------------------------------
        #display most frequent combination of start station and end station trip

        rc['Trip'] = rc['Start Station'].str.cat(rc['End Station'],sep=" to ")# i joined the 2 columns together :)
        trips = rc['Trip'].value_counts() #count values
        most_trip = trips.idxmax()
#----------------------------------------------------------
        print('The most commonly used start station in Washington is {}\n'.format(top_station))
        print('The most commonly used end station in Washington is {}\n'.format(end_station))
        print('The most frequent combination of start station and end station trip in Washington is : {}'.format(most_trip))
#---------------------------------------------------------------------------------------------------------------------------------


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    breakthree()



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    if city == 'chicago':
        rc = pd.read_csv('chicago.csv')

        print('The total travel time in Chicago is : {}'.format(rc['Trip Duration'].sum())) #display total travel time
        print('The mean travel time in Chicago is : {}'.format(rc['Trip Duration'].mean()))#display mean travel time
 #------------------------
    if city == 'new york city':
        rc = pd.read_csv('new_york_city.csv')

        print('The total travel time in New York City is : {}'.format(rc['Trip Duration'].sum())) #display total travel time
        print('The mean travel time in New York City is : {}'.format(rc['Trip Duration'].mean()))#display mean travel time
 #------------------------
    if city == 'washington':
        rc = pd.read_csv('washington.csv')

        print('The total travel time in Washington is : {}'.format(rc['Trip Duration'].sum())) #display total travel time
        print('The mean travel time in Washimgton is : {}'.format(rc['Trip Duration'].mean()))#display mean travel time



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    breakfour()
#trip_duration_stats(city)
#breakthree()

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if city == 'chicago':
        rc = pd.read_csv('chicago.csv')

        most_year = rc['Birth Year'].value_counts()

        print('The counts of user types for Chicago is :\n{}'.format(rc['User Type'].value_counts()))#Display counts of user types
        print('\nThe counts of gender in Chicago is :\n{}'.format(rc['Gender'].value_counts()))#Display counts of gender
        print('\nFor Chicago :\nThe most common year of birth is : {}\nThe most recent year of birth is : {}\nThe earliest year of birth is : {}\n '.format(most_year.idxmax(),rc['Birth Year'].max(),rc['Birth Year'].min()))# Display earliest, most recent, and most common year of birth
    #------------------------
    if city == 'new york city':
        rc = pd.read_csv('new_york_city.csv')

        most_year = rc['Birth Year'].value_counts()

        print('The counts of user types for New York City is :\n{}'.format(rc['User Type'].value_counts()))#Display counts of user types
        print('\nThe counts of gender in New York City is :\n{}'.format(rc['Gender'].value_counts()))#Display counts of gender
        print('\nFor New York City :\nThe most common year of birth is : {}\nThe most recent year of birth is : {}\nThe earliest year of birth is : {}\n '.format(most_year.idxmax(),rc['Birth Year'].max(),rc['Birth Year'].min()))# Display earliest, most recent, and most common year of birth
   #------------------------
    if city == 'washington':
        rc = pd.read_csv('washington.csv')

        print('The counts of user types for Washington is :\n{}'.format(rc['User Type'].value_counts()))#Display counts of user types
        print("\nSorry we don't have genders data for Washimgton")#Display counts of gender
        print("\nSorry we don't have year of birth data for Washimgton")# Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    breakfive()

def main():

    while True:

        df = load_data(city, month, day)
        breakone()
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
def breakfive():
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'yes':
              main()
        else:
            quit()

def breakfour():
    break_four = input('\nWould you like to displays statistics on bikeshare users for {} ? Enter yes or no.\n'.format(city)).lower()
    if break_four=='yes':
        user_stats(city)
    if break_four!='yes':
        breakfive()

def breakthree():
    break_three = input('\nWould you like to displays the statistics on the total and average trip duration for {} ? Enter yes or no.\n'.format(city)).lower()
    if break_three=='yes':
        trip_duration_stats(city)
    else:
        breakfour()


def breaktwo():
    break_two = input('\nWould you like to displays the statistics on the most popular stations and trip for {} ? Enter yes or no.\n'.format(city)).lower()
    if break_two=='yes':
        station_stats(city)
    else:
        breakthree()


def breakone():
    break_one = input('\nWould you like to display the statistics on the most frequent times of travel for {} ? Enter yes or no.\n'.format(city)).lower()
    if break_one=='yes':
        time_stats(city)
    else:
        breaktwo()


if __name__ == "__main__":
	main()

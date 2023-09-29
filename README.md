# explore-US-Bikceshare-dataMohammed Alrashdi
Uploaded Files:
1- readme.txt
2- bikeshare.py
3- search_tool.py

Note: To ensure correct execution of the script please ensure that both bikeshare and search_tool files are in the same directory

This programme is designed to explore US Bikceshare data by computing descriptive statistics and providing an interactive user experince.
The user will be able to view and filter the data by selectng the required city, month and day for better analysis. 
Further, the programme consist of an advanced GUI search tool to view the data by typing the required Station Name or Trip Duration.

To start the programe:

1- Run the bikeshare.py Script
2- The system will ask you to input a city to import the raw data(chicago, new york or washington)
3- The system will ask you to input a month to filter the data ( january to june)
4- The system will ask you to input a day to filter the data ( monday to sunday)
5- Once inputing the correct selections, the system will compute and display interesting statistical 
results based on the given city data and selected day and month filters.
6- finaly, the system will ask the user to select an option as show below:

Please select an Option:
 1: View Raw Data
 2: View Filtered Data
 3: Advance Search Tool
 4: Restart
 5: Exit
 Select a number:

7- Options 1 and 2 will display the first 5 lines of the data and ask the user if extra data needs to be displayed.
8- option 3 will run another script(search_tool.py) which is an davanecd tool to search by Station Name or Trip Duration.

The search window can take a digit to search for Trip Duration or a string to search for Station name
         
Examples: 
To search for Trip Duration: type 500 then click the Search button
To search for Station Name: type 'Streeter Dr & Grand Ave' then click the Search button
once finshed click close button
note: the search by Station Name feature will provide search results for both Start and End Stations

9- option 4 will restart the programe and ask the user to input a city name and select filters
10-option 5 will close the programe


References:

1- https://www.w3schools.com/python/default.asp
2- https://github.com/patrickbloomingdale/Udacity-Project-Explore-US-Bikeshare-Data
3- https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

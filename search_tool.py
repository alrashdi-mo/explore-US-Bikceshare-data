import pandas as pd
import tkinter as tk
from tkinter import ttk # for treeview

def search(raw_df):
    """create GUI to interact with the Bikeshare data """
    
    df = raw_df #get raw data
    tool_window = tk.Tk()
    tool_window.geometry("1100x400")  # width x height
    tool_window.title("Bikeshare Advanced Search")  # adding a title to the window
    
    label1 = tk.Label(tool_window, text="Search", width=5, font=20)  # added a Label
    label1.grid(row=1, column=0, padx=50, pady=20)
    
    label2 = tk.Label(tool_window, text="Search by Station Name or Trip Duration", width=40, font=20)  # added a Label
    label2.grid(row=0, column=1, padx=100, pady=10)

    entry = tk.Entry(tool_window, width=35, bg="white", font=18)  # added entry box for searching
    entry.grid(row=1, column=1, padx=1)

    button1 = tk.Button(tool_window, text="Search", width=7, font=18, command=lambda: my_search()) #add search button
    button1.grid(row=1, column=2, padx=2)
    
    button2= tk.Button(tool_window, text="Close", width=7, font=18, command=lambda: close_win())
    button2.grid(row=0, column=2, padx=2)

    def my_search():
        """filter data by Station Name or Trip Duration:E
        The search window can take a digit to search for Trip Duration 
        or a string to search for Station name
         
        Examples: 
        To search for Trip Duration: type 500 then click the Search button
        To search for Station Name: type 'Streeter Dr & Grand Ave' then click the Search button
        """
        headers = list(df)  # get a list of the column names as headers
        query = entry.get().strip() # get user entered string
        if query.isdigit(): # if query is number
            str1 = df["Trip Duration"] == float(query) 
        else:
            str1 = df["Start Station"].str.contains(query, case=False) | df["End Station"].str.contains(query, case=False)
        
        df2 = df[(str1)]  # combine all conditions
        filter_data = df2.to_numpy().tolist()  # Create list of list using rows
        tree_view = ttk.Treeview(tool_window, selectmode="browse")  # selectmode="browse" or "extended"
        tree_view.grid(row=2, column=1, columnspan=4, padx=10, pady=20)  #
        tree_view["height"] = 10 # Number of rows to display
        tree_view["show"] = "headings"
        tree_view["columns"] = headers # column headers

        for i in headers:
            tree_view.column(i, width=100, anchor="c")
            tree_view.heading(i, text=i) # Headings of respective columns
        for dt in filter_data:
            v = [r for r in dt]  # creating a list from each row
            tree_view.insert("", "end", iid=v[0], values=v)  # adding row
            
    def close_win():
        tool_window.destroy()
        
    tool_window.mainloop()

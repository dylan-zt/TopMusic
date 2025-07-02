from urllib.request import urlopen
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar
from re import *
from webbrowser import open as urldisplay
from sqlite3 import *




def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (not recommended!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; ' + \
                               'rv:91.0; ADSSO) Gecko/20100101 Firefox/91.0')
            print("Warning - Request to server does not reveal client's true identity.")
            print("          Use this option only if absolutely necessary!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        print(f"\nCannot find requested document '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print(f"\nAccess denied to document at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except URLError as message: # probably the wrong server address
        print(f"\nCannot access web server at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message: # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              f"the document at URL '{str(url)}'")
        print(f"Error message was: {message}\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL " + \
              f"'{url}' as '{char_set}' characters")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              f"the document from URL '{url}'")
        print(f"Error message was: {message}\n")
        return None

    # Optionally write the contents to a local text file
    # (silently overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(f'{target_filename}.{filename_extension}',
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print(f"\nUnable to write to file '{target_filename}'")
            print(f"Error message was: {message}\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution below.
#

# Create the main window
main_window = Tk()

pop_music_image = PhotoImage(file='bubblegum_cover.gif')
main_window.title("Pop Music Statistics")
main_window.geometry("700x500")
main_window.configure(bg="lightsteelblue")

# image place onto a canvas and resized 
canvas_image = Canvas(main_window, width=400, height=200)
canvas_image.create_image(100, 100, image=pop_music_image, anchor=CENTER)

#----------------------#
#     CONSTANTS        #
#----------------------#

# background color of GUI
GUI_BG_COLOUR = "pink"
# Font for widgets
WIDGET_FONT = ("Arial", 12, "bold")

#-----------------------#
# data_source for top 3 songs

url = 'https://www.americantop40.com/charts/top-40-238/latest/'
# access web document
songs_file = urlopen(url)
# extract raw data
songs_raw_bytes = songs_file.read()
# interpret as Unicode chars
songs_source_code = songs_raw_bytes.decode("UTF-8")
# close the web document
songs_file.close() 

# Define the HTML tags we want to find in the officialcharts source document 
start_tag = ') 2x" sizes="" alt='
end_tag = 'class="lazyload" srcSet="" width'

# find second infomation (name of artist for song)
start_tag2 = 'class="track-artist" target="_blank" rel="noopener">'
end_tag2 = '</a><div'


# start and end postion of first song result
start_pos = songs_source_code.find(start_tag)
end_pos = songs_source_code.find(end_tag, start_pos)

#start and end postion of arist for fist song
start_pos2 = songs_source_code.find(start_tag2)
end_pos2 = songs_source_code.find(end_tag2, start_pos2)

#song name
first_song = songs_source_code[start_pos + len(start_tag) : end_pos]
#artist name
first_artist_song = songs_source_code[start_pos2 + len(start_tag2) : end_pos2]




# second song result
start_pos = songs_source_code.find(start_tag, end_pos)
end_pos = songs_source_code.find(end_tag, start_pos)

#start and end for second artist name
start_pos2 = songs_source_code.find(start_tag2, end_pos2)
end_pos2 = songs_source_code.find(end_tag2, start_pos2)

#2nd song name
second_song = songs_source_code[start_pos + len(start_tag) : end_pos]

#2nd arist name
second_artist_song = songs_source_code[start_pos2 + len(start_tag2) : end_pos2]



# third song result
start_pos = songs_source_code.find(start_tag, end_pos)
end_pos = songs_source_code.find(end_tag, start_pos)

# start and end for third artist name
start_pos2 = songs_source_code.find(start_tag2, end_pos2)
end_pos2 = songs_source_code.find(end_tag2, start_pos2)

#3rd song name
third_song = songs_source_code[start_pos + len(start_tag) : end_pos]

#3rd artist name
third_artist_song = songs_source_code[start_pos2 + len(start_tag2) : end_pos2]
#-------------------------------------------------------------------------


# data_source for top 3 artists

url = 'https://www.billboard.com/charts/artist-100/'
artist_file = urlopen(url)  # access web document
artist_raw_bytes = artist_file.read()  # extract raw data
artist_source_code = artist_raw_bytes.decode("UTF-8")  # interpret as Unicode chars
artist_file.close()  # close the web document


# Define the HTML tags we want to find in the source document
start_tag_first = '0028@tablet">'  # First artist has a different start tag
start_tag = '230@tablet-only">'
end_tag = '</h3>'



# Start position for the first artist
start_pos_first = artist_source_code.find(start_tag_first)
end_pos_first = artist_source_code.find(end_tag, start_pos_first)

# Slice out the first artist's name from the source document
first_artist = artist_source_code[start_pos_first + len(start_tag_first): end_pos_first].strip()

# Finding the value for the number of weeks an artist has being on charts (weeks_on_charts) 
start_tag_weeks = '<p class="c-tagline  a-font-primary-bold-xxs u-letter-spacing-00 lrv-u-text-transform-uppercase lrv-u-padding-lr-050 lrv-u-margin-tb-00 lrv-u-padding-t-050">Weeks on chart</p>'
start_pos_weeks = artist_source_code.find(start_tag_weeks)

# Locate the span that follows the "Weeks on chart" tag
if start_pos_weeks != -1:
    # Finding first <span> tag after "Weeks on chart"
    start_tag_span = '<span class="c-label  a-font-primary-bold-xxl lrv-u-padding-lr-1 lrv-u-padding-t-025" >'
    start_pos_span = artist_source_code.find(start_tag_span, start_pos_weeks)

    if start_pos_span != -1:
        # Finding the end </span> tag
        end_pos_span = artist_source_code.find('</span>', start_pos_span)
        # slice desired value between start and end tag
        weeks_on_chart1 = artist_source_code[start_pos_span + len(start_tag_span): end_pos_span].strip()
    else:
        weeks_on_chart1 = "closing Span tag not found"
else:
    weeks_on_chart1 = "Weeks on chart tag not found"
# Start position for the second artist
start_pos = artist_source_code.find(start_tag, end_pos_first)
end_pos = artist_source_code.find(end_tag, start_pos)

# Slice out the second artist's name from the source document
second_artist = artist_source_code[start_pos + len(start_tag): end_pos].strip()

# Finding number of weeks for second artist (weeks_on_chart2) 
span_tag = '<span class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max" >'
end_span_tag = '</span>'

# there are 500+ occurrences that have the same start and end tag as shown above
# for the desired data, we need the 6th occurrence
current_position = 0
span_count = 0
weeks_on_chart2 = None

# use Loop function to find the 6th occurrence in the html document
while True:
    # Find the next span tag
    start_pos = artist_source_code.find(span_tag, current_position)
    
    if start_pos == -1:
        break  # function stops when zero span_tag found
    
    span_count += 1
    
    # If 6th span_tag found, slice the contents
    if span_count == 6:
        end_pos = artist_source_code.find(end_span_tag, start_pos)

        # This is the desired value for GUI; corresponds with the number of weeks an arist
        #has remained on the charts
        weeks_on_chart2 = artist_source_code[start_pos + len(span_tag): end_pos].strip()
        break
    
    #current position of "span tag" in loop function
    #(without this line of code, the loop function will keep finding the same "span tag" resulting in a false reading)
    current_position = start_pos + len(span_tag)

# Start position for the third artist
start_pos = artist_source_code.find(start_tag, end_pos)
end_pos = artist_source_code.find(end_tag, start_pos)

# Slice out the third artist's name from the source document
third_artist = artist_source_code[start_pos + len(start_tag): end_pos].strip()

# Finding number of weeks for Third artist (weeks_on_chart3) 
span_tag = '<span class="c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max" >'
end_span_tag = '</span>'

# there are 500+ occurrences that have the same start and end tag as shown above
# for the desired data, we need the 9th occurrence
current_position = 0
span_count = 0
weeks_on_chart3 = None

# use Loop function to find the 9th occurrence in the html document
while True:
    # Find the next span tag
    start_pos = artist_source_code.find(span_tag, current_position)
    
    if start_pos == -1:
        break  # function stops when zero span_tag found
    
    span_count += 1
    
    # If 9th span_tag found, slice the contents
    if span_count == 9:
        end_pos = artist_source_code.find(end_span_tag, start_pos)

        # This is the desired value that corresponds with the number of weeks an arist
        #has remained on the charts
        weeks_on_chart3 = artist_source_code[start_pos + len(span_tag): end_pos].strip()
        break
    
    #current position of "span tag" in loop function
    #without this line of code, the loop function will keep finding the same "span tag" resulting in a false reading
    current_position = start_pos + len(span_tag)

#-----------------------------------------------------------------------------#

# data_soure for top 3 albums

#Url for top album chart
url = 'https://www.officialcharts.com/charts/albums-chart/'
# access web document
albums_file = urlopen(url)
# extract raw data
albums_raw_bytes = albums_file.read()
# interpret as Unicode chars
albums_source_code = albums_raw_bytes.decode("UTF-8")
# close the web document
albums_file.close() 

# Define the HTML tags we want to find in the officialcharts source document 
start_tag = 'data-title='
end_tag = 'data-artist'

start_tag2 ='data-artist="'
end_tag2 = '" type'

# locate the position of the Album title in the source document using "find"
start_pos = albums_source_code.find(start_tag)
end_pos = albums_source_code.find(end_tag, start_pos)

start_pos2 = albums_source_code.find(start_tag2)
end_pos2 = albums_source_code.find(end_tag2, start_pos2)



# Slice out the first album title from the source
# document and save the details in a variable
first_album = albums_source_code[start_pos + len(start_tag) : end_pos]
first_artist_album = albums_source_code[start_pos2 + len(start_tag2) : end_pos2]

# Use the string "find" function to locate the position of the
# title & authors of the second book in the source document,
# remembering to start searching after the position of the first
# book

start_pos = albums_source_code.find(start_tag, end_pos)
end_pos = albums_source_code.find(end_tag, start_pos)

start_pos2 = albums_source_code.find(start_tag2, end_pos2)
end_pos2 = albums_source_code.find(end_tag2, start_pos2)

# Slice out the second book's title & authors from the source
# document and save the details in a variable
second_album = albums_source_code[start_pos + len(start_tag) : end_pos]
second_artist_album = albums_source_code[start_pos2 + len(start_tag2) : end_pos2]

# Use the string "find" function to locate the position of the
# title & authors of the third book in the source document,
# remembering to start after the position of the second book
start_pos = albums_source_code.find(start_tag, end_pos)
end_pos = albums_source_code.find(end_tag, start_pos)

start_pos2 = albums_source_code.find(start_tag2, end_pos2)
end_pos2 = albums_source_code.find(end_tag2, start_pos2)

# Slice out the third book's title & authors from the source
# document
third_album = albums_source_code[start_pos + len(start_tag) : end_pos]
third_artist_album = albums_source_code[start_pos2 + len(start_tag2) : end_pos2]
#--------------------------------------#
#      Functions for GUI buttons       #
#--------------------------------------#

# Function for displaying details in the entry widget
def show_data_source():
    # determin which button is selected, by the radio button variable
    if category_condition.get() == 1:
        urldisplay('https://www.americantop40.com/charts/top-40-238/latest/')
        message = "Data source: \nhttps://www.americantop40.com/charts/top-40-238/latest/"
    elif category_condition.get() == 2:
        urldisplay('https://www.billboard.com/charts/artist-100/')
        message = "Data source: \nhttps://www.billboard.com/charts/artist-100/"
    elif category_condition.get() == 3:
        urldisplay('https://www.officialcharts.com/charts/albums-chart/')
        message = "Data source: \nhttps://www.officialcharts.com/charts/albums-chart/"
    else:
        message = "please select a category"

    # Message displayed in the entry widget
    result_entry.delete('1.0', END)
    result_entry.insert('1.0', message)

bold_black = "\033[1;30m"

# Function for show_top_three button activation 
def show_top_three():
    
    if category_condition.get() == 1:
        message = "        Top Three Songs and Artist name from Americantop40\n" f"""
    1. {first_song} by {first_artist_song}
    2. {second_song} by {second_artist_song}
    3. {third_song} by {third_artist_song}
              """
    elif category_condition.get() == 2:
        message = "        Top Three Arist and the number of weeks postioned on billboard chart\n" f"""
    1. {first_artist}, {weeks_on_chart1} weeks on Billboard charts
    2. {second_artist}, {weeks_on_chart2} weeks on Billboard charts
    3. {third_artist}, {weeks_on_chart3} weeks on Billboard charts
               """
    elif category_condition.get() == 3:
        message = "         Top Three Albums and the Artist name from UK official charts\n" f"""
    1. {first_album} by {first_artist_album}
    2. {second_album} by {second_artist_album}
    3. {third_album} by {third_artist_album}
                """
                
    else:
        message = "please select a category"
    
    # Message displayed in the entry widget
    result_entry.delete('1.0', END)
    result_entry.insert('1.0', message)
    
#names of sources for top three infomation
source1 = "American top 40 songs"
source2 = "billboard top 100 artists"
source3 = "UK officialcharts top albums"

    

#-----------------------------------------------#
#   Create frames for organizing layout of GUI
#-----------------------------------------------#


# frame for displaying the title up the top of the GUI
title_frame = Frame(main_window)


# Selection frame for the 3 radio buttons
selection_frame = Frame(main_window,
                        bg=GUI_BG_COLOUR,
                        relief="groove",
                        borderwidth=2)

# frame for displying the top three and data source button 
Display_frame = Frame(main_window,
                       bg=GUI_BG_COLOUR,
                       relief="groove",
                       borderwidth=2)

# Saving frame for the scaler widget (saving category)
saving_frame = Frame(main_window,
                     bg=GUI_BG_COLOUR,
                     relief="groove",
                     borderwidth=2)
#----------------------------------------

title_label = Label(title_frame,
                   text="Pop Music Statistics Of 2024",
                   fg="white", bg="lightsteelblue",
                   font=("Arial", 16, 'bold')
                   )

# Title for left side widget with radio buttons
category_label = Label(selection_frame,
                      text="Categories",
                      font=WIDGET_FONT,
                      fg="white", bg="pink")

enrty_results_label = Label(main_window,
                            bg = "lightsteelblue",
                            text = "Message",
                            font = ("Arial", 12,),
                            fg = "black"
                            )
                            



# variable radio buttons 
category_condition = IntVar()
selected_value = IntVar()


# Three radio buttons for different categories

# Top Streamed Songs
radio_button_1 = Radiobutton(selection_frame,
                             text="Top Streamed Songs",
                             font=WIDGET_FONT, fg="white",
                             bg="palevioletred",
                             variable=category_condition,
                             value=1)
# Most Popular Artist
radio_button_2 = Radiobutton(selection_frame,
                             text="Most Popular Artist",
                             font=WIDGET_FONT,
                             fg="white",
                             bg="palevioletred",
                             variable=category_condition,
                             value=2)

# Top Performing Albums
radio_button_3 = Radiobutton(selection_frame,
                             text="Top Performing Albums",
                             font=WIDGET_FONT,
                             fg="white",
                             bg="palevioletred",
                             variable=category_condition,
                             value=3)


# Top_three_button and data_source_button belong in the same widget below categories

top_three_button = Button(Display_frame,
                        text="Show Top Three",
                        bg="lavenderblush",
                        command=show_top_three)

data_source_button = Button(Display_frame,
                        text="Show Data Source",
                        bg="lavenderblush",
                        command=show_data_source)  

# title for scaling wiget
saving_label = Label(saving_frame,
                     text="Save Option",
                     fg="white", font=WIDGET_FONT,
                     bg="pink")

# create a scale with 3 values corresponding to the categories 
saving_scale = Scale(saving_frame,
                     from_=1, to=3,
                     orient=HORIZONTAL,
                     bg="lavenderblush",
                     variable = selected_value,
                     length=300)


                     

# Result entry to display output from buttons
result_entry = Text(main_window, bg = "lavenderblush", width=80, height=5)

# function for transfering selected data from GUI to ranking.db
def insert_rankings(data_source, ranking, identifier, property):

    import os
    print("Current working directory:", os.getcwd())
    print("Database file exists:", os.path.exists('saved_rankings.db'))

    data_connect = connect('saved_rankings.db')

    data_cursor = data_connect.cursor()
    
    # SQL formatting
    query_sql = (
        f"INSERT INTO rankings "
        f"VALUES ("
        f"'{data_source}', "
        f"'{ranking}', "
        f"'{identifier}', "
        f"'{property}')"
        ) #End of query_sql

    # Execute the query
    data_cursor.execute(query_sql)
    
    # count the number of rows inserted
    row_quant = data_cursor.rowcount

    # changes are made and applied permanently to database
    data_connect.commit()
    
    # cursor and connection is closed
    data_cursor.close()
    data_connect.close()

    # the number of rows inserted is returned
    return row_quant
    
    #------------------------------------------------------------#
    # Function for inserting the disired data into the Database. #
    #------------------------------------------------------------#

    # user will decide what infomation to upload to data base by selecting source type,
    # positioning the slider (1-3) to select specific ranking then clicking save button.
def save_category():

    # radiobutton for top songs
    if category_condition.get() == 1:  
        if selected_value.get() == 1:
            message = insert_rankings(source1, 1, first_song, first_artist_song)
        elif selected_value.get() == 2:
            message = insert_rankings(source1, 2, second_song, second_artist_song)
        elif selected_value.get() == 3:
            message = insert_rankings(source1, 3, third_song, third_artist_song)

    # radiobutton for top artists 
    elif category_condition.get() == 2:  
        if selected_value.get() == 1:
            message = insert_rankings(source2, 1, first_artist, weeks_on_chart1)
        elif selected_value.get() == 2:
            message = insert_rankings(source2, 2, second_artist, weeks_on_chart2)
        elif selected_value.get() == 3:
            message = insert_rankings(source2, 3, third_artist, weeks_on_chart3)

    # radiobutton for top albums          
    elif category_condition.get() == 3:  
        if selected_value.get() == 1:
            message = insert_rankings(source3, 1, first_album, first_artist_album)
        elif selected_value.get() == 2:
            message = insert_rankings(source3, 2, second_album, second_artist_album)
        elif selected_value.get() == 3:
            message = insert_rankings(source3, 3, third_album, third_artist_album)

        

    else:
        print("please select a category")

save_category()


# Display saved result in entry window
# (save_button is placed under the save_category function so the
#   command variable is recognised)
save_button = Button(saving_frame,
                     text="Save Option",
                     bg="lavenderblush",
                     command=save_category)


#---------------------------------------------------------#
#            grid positioning  of widgets                 #
#---------------------------------------------------------#

#Title positioning 
title_frame.grid(row=0, column=0, columnspan=2, pady=10)
title_label.grid(row=0, column=1)

#image postion 
canvas_image.grid(row=1, column=1)

# category widget positioning 
selection_frame.grid(row=1, column=0, padx=10, pady=0)
category_label.grid(row=0, column=0, padx=10, pady=5)
radio_button_1.grid(row=1, column=0, sticky='w', padx=10, pady=2)
radio_button_2.grid(row=2, column=0, sticky='w', padx=10, pady=2)
radio_button_3.grid(row=3, column=0, sticky='w', padx=10, pady=2)

# Data display button positioning 
Display_frame.grid(row=2, column=0, padx=10, pady=0)
top_three_button.grid(row=1, column=0, padx=10, pady=5)
data_source_button.grid(row=2, column=0, padx=10, pady=5)

# Saving widget with scaler button positioning
saving_frame.grid(row=2, column=1, pady=5)
saving_label.grid(row=0, column=1)
saving_scale.grid(row=1, column=1, padx=10, pady=5, sticky="w")
save_button.grid(row=2, column=1, columnspan=2)

# results displayed positioning
enrty_results_label.grid(row=3, column=0,columnspan=2,padx=10, pady=10)
result_entry.grid(row=4, column=0, columnspan=2)


# Start the event loop to detect user inputs
main_window.mainloop()


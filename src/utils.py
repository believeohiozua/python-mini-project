import urllib.request
from visualizers.barchart import BarChartVisualizer
from visualizers.piechart import PieChartVisualizer
from .webscrapper import Webscrapper


def text_scraper_and_analyser(): 
    '''
    This method runs a loop for users to input and analyze a website
    it retuns a visual analyses from a valid url 
    and exits when the user quits
    '''  
    while True == 1: 
        url_input = input('\nEnter the website you wish to scrape or q to quit : ')
        if url_input == 'q' or url_input == 'Q':
            print('\nOops lets do this again some other time\n')
            break
        else:
            if url_input and url_input[:4] != 'http':
                 url_input = 'http://' + url_input
            # try:
            if url_input and url_input[:4] == 'http' and urllib.request.urlopen(url_input).getcode() == 200:  
                print('\nscraping... : ' + str(url_input))                 
                text_data = Webscrapper(url_input).text_generator()
                if text_data is not None:
                    choice = input('\n Done! \n press any key to view analysis or q to quit: ')  
                    if choice == 'q':
                        print('\nOops lets do this again some other time')
                        break                    
                    else:
                        print("\nHERE YOU GO\n")
                        BarChartVisualizer(text_data).show_bar_chart()
                        PieChartVisualizer(text_data).show_pie_chart()
                        print("\nLets continue...")
                        continue 

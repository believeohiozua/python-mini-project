import matplotlib.pyplot as plt


class PieChartVisualizer():
    '''
    This class takes a valid dictionary of word and their counts 
    and returns a pie chart visualization
    '''
    def __init__(self, data):
        self.data = data
        
    def show_pie_chart(self):
        if self.data is not None and len(self.data) == 2:          
            fig = plt.figure(figsize =(10, 10))         
            plt.pie(self.data[1], labels = self.data[0], autopct='%1.2f%%', radius=1)
            plt.show()
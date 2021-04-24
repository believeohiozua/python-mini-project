import matplotlib.pyplot as plt


class BarChartVisualizer():
    '''
    This class takes a valid dictionary of word and their counts 
    and returns a bar chart visualization
    '''
    def __init__(self, data):
        self.data = data
        
    def show_bar_chart(self):
        if self.data is not None:
            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])              
            ax.bar(self.data[0],self.data[1])       
            plt.show()

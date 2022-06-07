import pandas
import matplotlib.pyplot as plt

'''
Reads in a data set from csv, converts to a panda's data frame, and then displays a few graphs with the data

args:
    none
    
return 
    none
'''
def main():
    read_data_path = 'flatten_data.csv'

    data_frame = pandas.read_csv(read_data_path)
    data_frame = data_cleanup(data_frame)

    show_age_histogram(data_frame)
    show_sex_histogram(data_frame)
    show_race_histogram(data_frame)


'''
Cleans up the dataset from the CSV file. mainly replace over_50k to a boolean and add NULL value for '?'

args:
    data_frame (pandas data frame): The data frame that holds the data from the CSV file

return 
    none
'''
def data_cleanup(data_frame):
    data_frame['over_50k'] = data_frame['over_50k'].astype(bool)
    data_frame = data_frame.where(data_frame != '?', None)

    return data_frame


'''
Displays a histogram with the ages as the x value

args:
    data_frame (pandas data frame): The data frame that holds the data from the CSV file

return 
    none
'''
def show_age_histogram(data_frame):
    data_frame['age'].hist()
    plt.show()


'''
Displays a histogram with the sex as the x value

args:
    data_frame (pandas data frame): The data frame that holds the data from the CSV file

return 
    none
'''
def show_sex_histogram(data_frame):
    data_frame['sex'].hist()
    plt.show()


'''
Displays a histogram with race as the x value

args:
    data_frame (pandas data frame): The data frame that holds the data from the CSV file

return 
    none
'''
def show_race_histogram(data_frame):
    data_frame['race'].hist()
    plt.show()


if __name__ == '__main__':
    main()

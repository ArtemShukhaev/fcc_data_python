import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('Sea Level Predictor/epa-sea-level.csv')


    # Create scatter plot
    fig, ax = plt.subplots()
    
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
   
    # Create first line of best fit
    reg = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = reg.slope * x_pred + reg.intercept
    
    plt.plot(x_pred, y_pred, 'orange', linewidth=2)
    
    # Create second line of best fit

    reg_2000 = linregress(x=df[df['Year']>=2000]['Year'], y=df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    x_pred_2000 = pd.Series([i for i in range(2000, 2051)])
    y_pred_2000 = reg_2000.slope * x_pred_2000 + reg_2000.intercept
    
    plt.plot(x_pred_2000, y_pred_2000, 'r', linewidth=2)
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
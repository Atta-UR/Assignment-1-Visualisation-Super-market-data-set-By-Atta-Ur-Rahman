import pandas as pd
import matplotlib.pyplot as plt


def lineplot(x, y, xlabel, ylabel, title, color, labels):
    """ Funtion to Create Lineplot. Arguments:
        list of values for xaxis
        list of values for yaxis
        xlabel, ylabel and titel value
        color name
        label value
    """
    plt.figure(figsize=(10, 7))
    for index in range(len(x)):
        plt.plot(x[index], y[index], label=labels[index], color=color[index])
    plt.xticks(rotation=90)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.savefig('Supperstore_line_plot.jpg', dpi=500)
    plt.show()
    return


def barplot(x, y, xlabel, ylabel, title, color):
    """Funtion to Create Barplot. Arguments:
        list of values for xaxis
        list of values for yaxis
        xlabel, ylabel and titel value
        color name
    """
    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.bar(x, y, color=color)
    for bars in ax.containers:
        ax.bar_label(bars)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=90)
    plt.savefig('Supperstore_bar_plot.jpg', dpi=500)
    plt.show
    return


def pieplot(data, labels, title, plot_row, plot_col):
    """
        Funtion to Create Pieplot. Arguments:
        data to compare
        labels related to data we want to compare
        Title of pie plot
        number of plot in each row and column
    """
    fig, axes = plt.subplots(plot_row, plot_col, figsize=(10, 7))
    axes = axes.ravel()
    for i, title in enumerate(title):
        ax = axes[i]
        ax.pie(data[i], labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title(f'{title}')
    plt.tight_layout()
    plt.savefig('Supperstore_pie_plot.jpg', dpi=500)
    plt.show()
    return


def get_data_and_plot(dataframe):
    """Funtion to refine data of stores for line plot
       So, I get the weekly sum of each stores sales to compare their
       sales trend.
       then the linplot funtion is called to draw the graph.
    """
    dataframe["Date"] = pd.DatetimeIndex(dataframe["Date"])
    weekly_sales = dataframe.groupby(['City', pd.Grouper(key='Date',
                                                         freq='W')])[
                                                          'Total'].sum(
                                                            ).reset_index()
    store1 = weekly_sales[weekly_sales['City'] == 'Yangon']
    store2 = weekly_sales[weekly_sales['City'] == 'Mandalay']
    store3 = weekly_sales[weekly_sales['City'] == 'Naypyitaw']
    xlabel = 'Weeks'
    ylabel = 'Amount Per week $'
    titel = 'Weekly Sum of Sales of Stores in Cities'
    lineplot([store1['Date'], store2['Date'], store3['Date']],
             [store1['Total'], store2['Total'], store3['Total']],
             xlabel, ylabel, titel,
             ['red', 'green', 'blue'], ['Yango', 'Mandalay', 'Naypyitaw'])
    return


def get_data_and_bar(dataframe):
    """Funtion to refine data of stores for bar plot
       So, I get the total sum of sales for each Product line to compare
       which catagories product sold most.
       then the barplot funtion is called to draw the graph
    """
    product_sales = dataframe.groupby('Product line')['Total'].sum()
    product_sales = pd.DataFrame(product_sales)
    product_sales = product_sales.reset_index()
    color = ['lightblue', 'blue', 'purple', 'red', 'black', 'green']
    barplot(product_sales['Product line'], product_sales['Total'],
            'Product Name', 'Total Sale Price', 'Sales Sum of Products', color)
    return


def get_data_and_pie(dataframe):
    """Funtion to refine data of stores for pie plot
       So, I get the total sum for both gender male and
       female to compare the ratio of
       Product lines bought by both genders.
       then the barplot funtion is called to draw the graph
    """
    product_lines = dataframe['Product line'].unique()
    gender_value = []
    for i, product_line in enumerate(product_lines):
        product_data = dataframe[dataframe['Product line'] == product_line]
        gender_counts = product_data['Gender'].value_counts()
        labels = gender_counts.index
        gender_value.append([gender_counts[0], gender_counts[1]])
    print(gender_value,labels)
    pieplot(gender_value, labels, product_lines, 3, 2)


dataframe = pd.read_csv('supermarket_sales.csv')
get_data_and_plot(dataframe)
get_data_and_pie(dataframe)
get_data_and_bar(dataframe)

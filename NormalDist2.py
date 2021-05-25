import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv('data.csv')
diagram = ff.create_distplot([df["Height(Inches)"].tolist()],["Weight"], show_hist=False)
diagram.show()
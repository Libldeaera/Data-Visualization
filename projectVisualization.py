# Import
import pandas as pd
import seaborn as sns
import matplotlib.pylot as plt
import numpy as np

sns.set(rc = {'figure.figsize':(5, 5)})

# Read Data
df = pd.read_csv("world-happiness-report.csv")
df.head(10)

# Explarotary Data Analysis
df.info()

df["Country name"].value_counts()

df.describe().T

# Visualizing Data and Preprocessing
from os import mkdir

try:
  mkdir("Plots")
  except:
    pass
  mypath = "Plots"
  
  f, axes = plt.subplots(5, 2, figsize = (20, 30))
  f.tight_layout(pad = 8)
  f.subtitle("Distribution Before Preprocessing")
  cols = df.select_dtypes(exclude = "object").columns
  
  x_axis = 0
  y_axis = 0
  
  for col in cols:
    sns.hisplot(data = df, x = col, KDE = True, ax = axes[x_axis, y_axis])
    
    axes[x_axis, y_axis].set_xlabel(col.title())
    axes[x_axis, y_axis].set_ylabel("Count")
    axes[x_axis, y_axis].set_title(f "{col.title()} Count")
    
    if y_axis == 1:
      y_axis = 0
      x_axis += 1
      #continue
      else:
        y_axis += 1
        
        plt.savefig("Plots/histograms.png)
                    plt.show()
                    

  f, axes = plt.subplots(5, 2, figsize = (20, 30))
  f.tight_layout(pad = 8)
  f.subtitle("Boxplots")
  cols = df.select_dtypes(exclude = "object").columns
  
  x_axis = 0
  y_axis = 0
  
  for col in cols:
    sns.hisplot(data = df, x = col, KDE = True, ax = axes[x_axis, y_axis])
           
    axes[x_axis, y_axis].set_xlabel(col)
    axes[x_axis, y_axis].set_ylabel("Count")
    axes[x_axis, y_axis].set_title(f "{col.title()} Box Plot")
    
    if y_axis == 1:
      y_axis = 0
      x_axis += 1
      #continue
      else:
        y_axis += 1
        
        plt.savefig("Plots/boxplots.png)
                    plt.show()
                    
                    # Grouping Data by Year For Visualization
                    
                    year_group = df.groupby("year").sum()
                    year_group
                      
                    # Saving Plot as "png" format
                    year_group["Positive Affect"].plot()
                    plt.savefig("Plots/PositiveAffectPlot.png")
                    
                    year_group["Negative Affect"].plot()
                    plt.savefig("Plots/NegativeAffectPlot.png")
                    
                    year_group
                    
                    ax1 = sns.barplot(x = year_group.index, y = year_group['Social Support'].values)
                    ax1.tick_params(axis = 'x', rotation = 90)
                    plt.savefig("Plots/SocialSupport.png")
                    
                    sns.set(rc = {'figure.figsize':(15, 10)})
                    plt.title('Correlation Matrix')
                    sns.heatmap(df.corr(), annot = True)
                    plt.savefig("Plots/CorrelationMatrix.png")
                    
                    sns.jointplot(data = df, x = "year", y = "Social Support")
                    sns.jointplot(data = df, x = "Life Ladder", y = "Social Support")
                    
                    # Exporting Reports as PDF format
                    import os
                    from os import listdir, mkdir
                    from os.path import isfile, join
                    
                    all_files = os.listdir("Plots/")
                    reports = [f"Plots/{file}" for file in all_files]
                    print(reports)
                    
                    !pip install FPDF
                    
                    from fpdf import FPDF
                    
                    WIDTH = 210
                    HEIGHT = 297
                    
                    pdf = FPDF()
                    pdf.set_font("Arial", "B", 56)
                    pdf.add_page()
                    pdf.cell(180, 20, txt = 'REPORT', align = 'C')
                    
                    #pdf.add_page()
                    for.report in reports:
                    pdf.add_page()
                    pdf.set_font("Arial", "B", 24)
                    pdf.cell(180, 20, txt = 'REPORT', align = 'C')
                    pdf.image(report, 5, 30, WIDTH-5)
                    
                    pdf.output("CountriesReports.pdf", "F")
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
      
  

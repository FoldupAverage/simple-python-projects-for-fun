from advertools import sitemap_to_df
import pandas as pd

df = sitemap_to_df('https://www.jcchouinard.com/sitemap.xml')
df['loc'].to_csv('output/urls.txt', header=None, index=None, sep='\t', mode='a')
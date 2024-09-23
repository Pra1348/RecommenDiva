from faker import Faker
import random
import csv
import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import altair as alt
from bokeh.plotting import figure, output_file, save
import holoviews as hv
from holoviews import opts
import panel as pn
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import geopandas as gpd
import folium
import wordcloud
from pyecharts.charts import Line, Pie, Bar
from pyecharts import options as opts
from wordcloud import WordCloud

# Initialize Faker
fake = Faker()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_fake_data(num_entries):
    """Generate a list of dictionaries with fake fashion data."""
    fashion_data = []
    
    for _ in range(num_entries):
        product_name = fake.word().capitalize() + " " + fake.word().capitalize()
        brand = fake.company()
        category = random.choice(['Tops', 'Bottoms', 'Dresses', 'Shoes', 'Accessories', 'Bags', 'Jewelry'])
        price = round(random.uniform(10, 1000), 2)
        color = random.choice(['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow', 'Pink', 'Purple'])
        size = random.choice(['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'])
        material = random.choice(['Cotton', 'Polyester', 'Leather', 'Silk', 'Denim', 'Wool', 'Linen'])
        gender = random.choice(['Male', 'Female', 'Unisex', 'Kids'])
        season = random.choice(['Spring', 'Summer', 'Fall', 'Winter', 'All-season'])
        style = random.choice(['Casual', 'Formal', 'Sporty', 'Elegant', 'Bohemian', 'Vintage', 'Streetwear'])
        availability = random.randint(0, 100)
        rating = round(random.uniform(1, 5), 1)
        review_count = random.randint(0, 500)
        country = fake.country()
        region = fake.state()
        brand_reputation = random.choice(['High', 'Medium', 'Low'])
        eco_friendly = random.choice([True, False])
        description = fake.text(max_nb_chars=200)
        
        logging.info(f"Generated entry: {product_name}")
        logging.info(f"Product details: {product_name}, {brand}, {category}, ${price}, {color}, {size}, {material}, {gender}, {season}, {style}, {availability}, {rating}, {review_count}, {country}, {region}, {brand_reputation}, {eco_friendly}, {description}")
        logging.info("---")
        
        fashion_data.append({
            'product_name': product_name,
            'brand': brand,
            'category': category,
            'price': price,
            'color': color,
            'size': size,
            'material': material,
            'gender': gender,
            'season': season,
            'style': style,
            'availability': availability,
            'rating': rating,
            'review_count': review_count,
            'country': country,
            'region': region,
            'brand_reputation': brand_reputation,
            'eco_friendly': eco_friendly,
            'description': description
        })
    
    return fashion_data

def save_to_csv(data, filename):
    """Save the list of dictionaries to a CSV file."""
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['product_name', 'brand', 'category', 'price', 'color', 'size', 'material', 'gender', 'season', 'style', 'availability', 'rating', 'review_count', 'country', 'region', 'brand_reputation', 'eco_friendly', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
            
        logging.info(f"Data successfully saved to {filename}")
    
    except Exception as e:
        logging.error(f"An error occurred while saving data to CSV: {e}")

def display_data_in_table(data):
    """Display the data as a table using pandas."""
    df = pd.DataFrame(data)
    print(df.head())  # Print the first few rows of the DataFrame
    df.to_html('fashion_data.html', index=False)  # Save the DataFrame as an HTML file for better viewing
    
    # Additional visualization
    visualize_data(df)

def visualize_data(df):
    """Visualize the data using multiple libraries."""
    
    # Plotly Visualizations
    fig = px.histogram(df, x='price', nbins=30, color_discrete_sequence=['royalblue'], title='Price Distribution')
    fig.update_layout(xaxis_title='Price', yaxis_title='Count')
    fig.write_html('price_distribution_plotly.html')
    fig.show()

    # Word Cloud Visualization for Product Descriptions
    text = " ".join(description for description in df.description)
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    wc.to_file("wordcloud_product_descriptions.png")
    plt.figure(figsize=(10, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title('Word Cloud of Product Descriptions')
    plt.show()

    # Geographic Visualization using Folium
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['price'], df['rating']))
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    base = world.plot(color='white', edgecolor='black')
    gdf.plot(ax=base, marker='o', color='red', markersize=5)
    plt.title('Geographic Distribution of Products')
    plt.savefig('geographic_distribution.png')
    plt.show()

    # Pyecharts Visualizations
    bar = Bar()
    bar.add_xaxis(df['category'].unique().tolist())
    bar.add_yaxis("Average Price", df.groupby('category')['price'].mean().round(2).tolist())
    bar.set_global_opts(title_opts=opts.TitleOpts(title="Average Price by Category"))
    bar.render("average_price_by_category_pyecharts.html")

    pie = Pie()
    pie.add("Gender Distribution", [list(z) for z in zip(df['gender'].unique(), df['gender'].value_counts().tolist())])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="Gender Distribution"))
    pie.render("gender_distribution_pyecharts.html")

    line = Line()
    line.add_xaxis(df['season'].unique().tolist())
    line.add_yaxis("Average Rating", df.groupby('season')['rating'].mean().round(2).tolist())
    line.set_global_opts(title_opts=opts.TitleOpts(title="Average Rating by Season"))
    line.render("average_rating_by_season_pyecharts.html")

    # Dash Visualization
    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.H1("Interactive Price vs Rating Scatter Plot"),
        dcc.Graph(id="scatter-plot"),
        dcc.Slider(
            id="rating-slider",
            min=df['rating'].min(),
            max=df['rating'].max(),
            value=df['rating'].min(),
            marks={str(rating): str(rating) for rating in df['rating'].unique()},
            step=None
        )
    ])

    @app.callback(
        Output("scatter-plot", "figure"),
        [Input("rating-slider", "value")]
    )
    def update_figure(selected_rating):
        filtered_df = df[df['rating'] >= selected_rating]
        fig = px.scatter(filtered_df, x="price", y="rating", color="category",
                         size="review_count", hover_name="product_name")
        fig.update_layout(transition_duration=500)
        return fig

    if __name__ == '__main__':
        app.run_server(debug=True)

def main():
    """Main function to generate and save fake data."""
    num_entries = 1000
    logging.info(f"Generating {num_entries} entries of fake data...")
    fashion_data = generate_fake_data(num_entries)
    
    # Print a sample of the generated data
    logging.info(f"Sample data: {fashion_data[:5]}")
    
    save_to_csv(fashion_data, 'fashion_data.csv')
    
    # Display data in table format and visualize
    display_data_in_table(fashion_data)

if __name__ == "__main__":
    main()

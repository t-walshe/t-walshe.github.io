"""
Use this code as the basis for generating charts
"""

from html.parser import HTMLParser
from pathlib import Path

from bokeh.plotting import figure, show, output_file, save

from bs4 import BeautifulSoup


if __name__ == "__main__":
    # Example comes from: https://docs.bokeh.org/en/2.4.3/docs/gallery/bar_stacked.html
    
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    years = ["2015", "2016", "2017"]
    colors = ["#c9d9d3", "#718dbf", "#e84d60"]

    data = {'fruits' : fruits,
            '2015'   : [2, 1, 4, 3, 2, 4],
            '2016'   : [5, 3, 4, 2, 4, 6],
            '2017'   : [3, 2, 4, 4, 5, 3]}

    p = figure(x_range=fruits, 
               height=512,                   ## 
               max_width=int(512*1.4),       ##
               sizing_mode="scale_width",    ##
               title="Fruit Counts by Year",
               toolbar_location=None, tools="hover", tooltips="$name @fruits: @$name")

    p.vbar_stack(years, x='fruits', width=0.9, color=colors, source=data,
                 legend_label=years)

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"

    # set output to static HTML file - change these as desired
    output_file(filename="custom_filename.html", title="Static HTML file")

    # Uncomment to view the plot
    #show(p)

    # save the results to a file
    _ = save(p)
    
    
    
    # Load the generated plot, extract the body, place in container
    parser.feed(Path("custom_filename.html").read_text())
    parsed_html = BeautifulSoup(Path("custom_filename.html").read_text())
    body = parsed_html.find('body')

    content: list = [str(tag) for tag in body.contents]
    content.insert(0, '<div class="container" style="display: flex; justify-content: center;">')
    content.append('</div>')

    _ = Path("custom_graph_formatted.html").write_text(" ".join(content))
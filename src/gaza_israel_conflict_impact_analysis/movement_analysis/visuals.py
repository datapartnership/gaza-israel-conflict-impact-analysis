from bokeh.core.validation import silence
from bokeh.core.validation.warnings import EMPTY_LAYOUT
from bokeh.layouts import column
from bokeh.models import Legend
from bokeh.plotting import ColumnDataSource, figure

# Use the silence function to ignore the EMPTY_LAYOUT warning
silence(EMPTY_LAYOUT, True)


def get_line_chart(
    df,
    title,
    source,
    subtitle=None,
    measure="measure",
    category="category",
):
    # Initialize the figure
    p2 = figure(x_axis_type="datetime", width=750, height=400, toolbar_location="above")
    p2.add_layout(Legend(), "right")

    # Define the color palette (make sure this has enough colors for the categories)
    color_palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

    # Loop through each unique category and plot a bar
    for id, unique_category in enumerate(df[category].unique()):
        # Filter the DataFrame for each category
        category_df = df[df[category] == unique_category].copy()
        category_df.sort_values(
            by="agg_day_period", inplace=True
        )  # Ensure the DataFrame is sorted by date
        category_source = ColumnDataSource(category_df)

        # Plot the bars
        p2.line(
            x="agg_day_period",
            y=measure,
            width=1.5,
            source=category_source,
            color=color_palette[id],
            legend_label=unique_category,
        )

        # Configure legend
        p2.legend.click_policy = "hide"
        p2.legend.location = "top_right"

    # # Set the subtitle as the title of the plot if it exists
    # if subtitle:
    #     p2.title.text = subtitle

    # Create title and subtitle text using separate figures
    title_fig = figure(title=title, toolbar_location=None, width=750, height=40)
    title_fig.title.align = "left"
    title_fig.title.text_font_size = "14pt"
    title_fig.border_fill_alpha = 0
    title_fig.outline_line_color = None

    sub_title_fig = figure(title=source, toolbar_location=None, width=750, height=40)
    sub_title_fig.title.align = "left"
    sub_title_fig.title.text_font_size = "10pt"
    sub_title_fig.title.text_font_style = "normal"
    sub_title_fig.border_fill_alpha = 0
    sub_title_fig.outline_line_color = None

    # Combine the title, plot, and subtitle into a single layout
    layout = column(title_fig, p2, sub_title_fig)

    return layout

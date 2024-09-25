from IPython.display import display, HTML
from functools import wraps

def compare_print(background_colors=None, labels=None):
    """
    A decorator to display outputs of LLMs side by side in a Jupyter Notebook cell.
    
    Parameters:
    - background_colors: Optional list of background colors for each LLM output panel.
    - labels: Optional list of labels for each LLM output panel.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get the outputs by calling the decorated function
            outputs = func(*args, **kwargs)
            
            # Ensure outputs are iterable (list, tuple)
            if not isinstance(outputs, (list, tuple)):
                outputs = [outputs]
            
            # Number of LLM outputs
            num_outputs = len(outputs)
            
            # Set default labels if none are provided
            nonlocal labels
            if labels is None:
                labels = [f"Output {i+1}" for i in range(num_outputs)]
            
            # Set default pastel background colors if none are provided
            nonlocal background_colors
            if background_colors is None:
                background_colors = [
                    "#FFEBE8",  # Light pastel pink
                    "#E8F0FF",  # Light pastel blue
                    "#E8FFE8",  # Light pastel green
                    "#FFF3E8"   # Light pastel orange
                ]
            
            # Ensure we have enough background colors, if not repeat colors
            while len(background_colors) < num_outputs:
                background_colors += background_colors[:num_outputs - len(background_colors)]
            
            # Set the default text color (dark enough to be visible on light backgrounds)
            text_color = "#333333"  # Dark gray color for good contrast
            
            # Style the layout for side-by-side display with text color
            html_content = "<div style='display: flex; flex-direction: row;'>"
            
            # Create a column for each LLM output with a pastel background and safe text color
            for i in range(num_outputs):
                html_content += f"""
                <div style='flex: 1; margin: 3px; padding: 10px; border: 1px solid #ddd; 
                             background-color: {background_colors[i]}; color: {text_color};'>
                    <h3 style='color: {text_color};'>{labels[i]}</h3>
                    <p>{outputs[i]}</p>
                </div>
                """
            
            # Close the div
            html_content += "</div>"
            
            # Display the HTML content in the Jupyter Notebook cell
            display(HTML(html_content))
            
        return wrapper
    return decorator

if __name__ == "__main__":
    # Example usage with a decorated function
    @compare_print(labels=["Model A", "Model B", "Model C"])
    def generate_llm_outputs():
        # Simulate generating outputs from LLMs
        return [
            "This is the output of the first LLM.",
            "This is the output of the second LLM.",
            "This is the output of the third LLM."
        ]

    # Call the decorated function to display the outputs
    generate_llm_outputs()
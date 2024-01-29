import os
import jsbeautifier

# Path to the JavaScript directory
js_directory = ""

# Function to concatenate and beautify JavaScript files
def beautify_js_chunks(directory):
    # Concatenating the content of all JavaScript files
    combined_js = ""
    for filename in os.listdir(directory):
        if filename.endswith('.js'):
            with open(os.path.join(directory, filename), 'r') as file:
                combined_js += file.read() + "\n"
            
    # Beautifying the combined JavaScript content
    beautified_js = jsbeautifier.beautify(combined_js)

    # Output file path
    output_file = os.path.join(directory, "combined_beautified.js")
    with open(output_file, 'w') as file:
        file.write(beautified_js)

    print(f"Combined and beautified JavaScript saved to {output_file}")

# Call the function with the specified directory
beautify_js_chunks(js_directory)
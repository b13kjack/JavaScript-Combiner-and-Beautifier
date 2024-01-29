import os
import jsbeautifier

# Path to the JavaScript directory
js_directory = ""

# Function to concatenate and beautify JavaScript files
def beautify_js_chunks(directory):
    try:
        # Concatenating the content of all JavaScript files
        combined_js = ""
        print("Starting to concatenate JavaScript files...")
        js_files = [filename for filename in os.listdir(directory) if filename.endswith('.js')]
        if len(js_files) == 0:
            print("No JavaScript files found, aborting script")
            return
        elif len(js_files) == 1:
            print("Found one file only, skipping concatenation")
        else:
            for filename in js_files:
                with open(os.path.join(directory, filename), 'r') as file:
                    combined_js += file.read() + "\n"
            print("Concatenation completed.")

        # Beautifying the combined JavaScript content
        print("Starting to beautify the combined JavaScript content...")
        beautified_js = jsbeautifier.beautify(combined_js)
        print("Beautification completed.")

        # Output file path
        output_file = os.path.join(directory, "combined_beautified.js")
        print(f"Writing beautified JavaScript to {output_file}...")
        with open(output_file, 'w') as file:
            file.write(beautified_js)
        print(f"Combined and beautified JavaScript saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the specified directory
beautify_js_chunks(js_directory)
import os

def list_md_files(directory, output_file):
    # Open the output file in write mode
    with open(output_file, 'w') as f:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check for .md extension
                if file.endswith('.md'):
                    # Write the filename without the extension to the text file
                    f.write(os.path.splitext(file)[0] + '\n')

# Define the directory to search and output file path
directory = fr'C:\Users\Ulfzerk\Documents\logseq_notes\pages'
output_file = 'node_names.txt'

# Call the function
list_md_files(directory, output_file)

print(f"File names have been written to {output_file}")

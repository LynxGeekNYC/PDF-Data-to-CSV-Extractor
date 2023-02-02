import PyPDF2
import pandas as pd

def extract_table_from_pdf(pdf_file):
    # Open the PDF file
    pdf = PyPDF2.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF
    num_pages = pdf.getNumPages()

    # Initialize an empty list to store the extracted data
    data = []

    # Loop over each page of the PDF
    for i in range(num_pages):
        page = pdf.getPage(i)
        text = page.extractText()
        lines = text.splitlines()

        # Loop over each line of text
        for line in lines:
            # Split the line into words
            words = line.split()

            # Check if the line contains a table row
            if len(words) > 1:
                data.append(words)

    # Convert the extracted data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Return the DataFrame
    return df

# Call the function to extract the table from the PDF
df = extract_table_from_pdf('example.pdf')

# Write the DataFrame to a CSV file
df.to_csv('example.csv', index=False)

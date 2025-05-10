import csv

def extract_reviews(input_file, output_file):
    try:
        # Open the CSV file
        with open(input_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            # Extract the 'review_description' column
            reviews = [row['review_description'] for row in reader if 'review_description' in row]
        
        # Join reviews with a comma and a new line
        formatted_reviews = ',\n'.join(reviews)
        
        #write the formatted reviews to the text file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(formatted_reviews)
        
        print(f"Successfully extracted {len(reviews)} reviews to '{output_file}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# file containing data
input_file = 'Reviews.csv'

# Output file
output_file = 'Reviews.txt'




# Call the function to extract reviews
extract_reviews(input_file, output_file)
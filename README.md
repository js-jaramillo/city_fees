# City Fees
City Fees is a web scraping program that extracts information about city fees from the City of Houston website. The program is written in Python and uses the Scrapy framework.

City of Houston Fee Schedule Page: https://cohweb.houstontx.gov/FIN_FeeSchedule/default.aspx

## Installation
To run the progam, you will need to have Python 3.10 installed and Scrapy 2.9. Once you have Python installed, you can install Scrapy using the following command:

pip install Scrapy

## Usage
To use the City Fees program, you will need to navigate to the city_fees directory in your terminal and use the following command:

scrapy crawl feespider

The Feespider will then extract the following information from the fee schedule page:

Fee name
Fee description
Statutory authority
Fee amount
As of date

The extracted information will be saved in a JSON file. The JSON file will be named city_fees.json and it will be saved in the current directory. If you have a JSON file with the same name, it will overwrite it.

## Example
Here is an example of the output of the program:

{
"fees": [
{
"name": "Building Permit Fee",
"description": "Fee for a building permit",
"statutory_authority": "City Code Chapter 22",
"amount": 250,
"as_of_date": "2023-05-29"
},
{
"name": "Plan Review Fee",
"description": "Fee for plan review",
"statutory_authority": "City Code Chapter 23",
"amount": 100,
"as_of_date": "2023-05-29"
},
{
"name": "Inspection Fee",
"description": "Fee for inspection",
"statutory_authority": "City Code Chapter 24",
"amount": 50,
"as_of_date": "2023-05-29"
}
]
}

## Contributing
This is an open source project and contributions are welcome. If you would like to contribute, please fork the project on GitHub and submit a pull request.

## License
City Fees is licensed under the MIT License.
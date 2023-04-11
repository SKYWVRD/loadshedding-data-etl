# loadshedding-data-etl
A dataflow setup using the eskom se push API

This will make use of AWS lambda functions triggered by cloudwatch that will write the json files to an S3 bucket
Once the S3 bucket recieves the new json file, it will trigger the next Lamda function to parse the file and upload its data to documentdb
Once the file is completely written the lamda function will move the parsed file to an archived folder in the fucket

This data will then be accessed by a dashboard to show the amount of loadshedding we have had, as well as the amount of each stage we have had.
This will be split between Cape Town and Eskom direct, as well as both together

This repo will store the documentation as well as the various AWS lambda functions used 

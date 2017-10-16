# Polly-text2speech

This project uses Python 3.6, Amazon Poly, and the AWS CLI in order to parse a text file (needs work) and send the pieces to Amazon Polly for Speech to text Translation.

Amazon Polly is a web service that provides text-2-speech services.


## Requirements
* Amazon Web Services Account
* Amazon IAM and Access Keys (Check the Amazon Polly Getting Started Page for a walkthrough on most of this)
* Amazon CLI installed (Command Line Interface)
* Amazon CLI Config File set up (Usually you do this after you install the CLI)
* Python 3.6 installed
* A text file of the book you want to have translated

## Process Flow
* Change the Source File to the location of the text you want translated
* Choose a destination for your output files
* Make sure you have your AWS account and IAM configured (Follow the walkthrough on Amazon Polly Getting Started)
* Run the python script
* Find a way to combine the Audio Files

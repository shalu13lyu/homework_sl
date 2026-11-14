# Day 03 Assignment

In this week's assignment, we learned how to use AI in VS Code to write a Python program.

## What I did

I decided to work with transmission electron microscopy (TEM) images, since this is related to my PhD research.

I wanted to create a website where I could upload an EM image of a carbon grid and automatically count how many circular vesicles are located inside a selected grid hole.

I used Python with OpenCV to detect circular structures in the image, and Flask, HTML, CSS, and JavaScript to create an interactive website.

The website allows the user to upload an image, select a carbon-grid hole, and get the number of detected vesicle candidates. It also displays the image with green circles marking the detected structures.

## My Workflow

1. **Choosing the project:** I chose vesicle counting because analyzing TEM images is related to my research, and I wanted to automate part of the image analysis.

2. **Creating `detector.py`:** I used Python and OpenCV to detect circular structures using the Hough Circle Transform and count those inside a selected grid hole.

3. **Creating `app.py`:** I used Flask to connect the Python detection function to the website, so users can upload their own images.

4. **Creating `index.html`:** I used HTML, CSS, and JavaScript to design the website, allow users to select a circular region, and display the results.

5. **Testing the website:** I ran the Python application in VS Code and opened the website in Chrome to test the image upload and vesicle detection.

6. **GitHub:** I prepared the project files for version control and sharing through GitHub.

## Prompts I Used

My first prompt was:

> I specifically want to do a program that counts how many circular vesicles there are in a circle of a carbon grid, like in the TEM image I uploaded.

At first, I planned to create only a Python program, but then I decided to make it more interactive by creating a website.

My next prompt was:

> From the beginning, I want to create using VS Code an HTML website that, when you upload a picture of a grid EM, counts how many circular vesicles there are in a circle of a carbon grid and tells you the result.

I then asked AI to guide me through creating the Python files:

> I created and saved detector.py. Please guide me through the next step: creating app.py in VS Code.

Finally, I asked for help creating the HTML website:

> I created index.html. Write at least a few stages for me to do.

## Results

I created a local website that allows users to upload TEM images, select a carbon-grid hole, and automatically count circular vesicle candidates.

The detection is still preliminary, and the parameters may need to be adjusted to improve accuracy.

## Website Address

**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

This website runs locally on my computer using Flask.

To open the website, first run the Python application in VS Code:

`py app.py`

Then open the address above in a web browser.

## Project Files

- `detector.py` — Detects and counts circular vesicle candidates.
- `app.py` — Connects Python to the website using Flask.
- `index.html` — Website interface for uploading images and displaying results.
- `requirements.txt` — Lists the required Python libraries.

## How to Run

Install the required libraries:

`py -m pip install -r requirements.txt`

Run the application:

`py app.py`

Open the website:

**[http://127.0.0.1:5000](http://127.0.0.1:5000)**
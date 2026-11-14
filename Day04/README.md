# Day 04 Assignment — EM Vesicle Counter Website

## What I Did

For this week's assignment, I continued working on my Day03 project, an EM Vesicle Counter website related to my PhD research.

The goal of my project is to automatically detect and count circular vesicles inside a selected carbon-grid hole in transmission electron microscopy (TEM) images.

I copied my previous project into a new `Day04` folder to keep the original version unchanged. I continued developing the application using Python, Flask, OpenCV, HTML, CSS, and JavaScript.

For Day04, I wanted to improve the counting process by adding manual correction options and make the website accessible to other people through a public link.

## My Workflow

1. **Creating Day04:** I created a new `Day04` folder and copied my Day03 files to keep the original project intact.

2. **Testing the application:** I checked that both the original Day03 application and the copied Day04 application were working.

3. **Improving the website:** I updated `index.html` to add a manual correction interface. The user can add missed vesicles, undo corrections, and reset the results. I also added an option for removing detections, although this feature still needs improvement.

4. **Preparing for deployment:** I updated `requirements.txt` to include the libraries needed to run the application on a server.

5. **Connecting GitHub to Render:** I connected my GitHub repository to Render to publish the website online.

6. **Testing the public website:** After fixing a deployment error, I successfully opened the website using the public Render link.

## Deploying My Website Using Render

For Day04, I wanted to make my EM Vesicle Counter website accessible to other people, not only on my computer.

First, I updated `requirements.txt` and added Gunicorn, which is a production web server used to run Flask applications. I also changed OpenCV to the headless version because the server does not need a graphical interface.

Next, I pushed my Day04 files to GitHub and connected my `homework_sl` repository to Render. I selected Python, set the Root Directory to `Day04`, and configured the build command (`pip install -r requirements.txt`) and start command (`gunicorn app:app`).

My first deployment failed because Render could not find `requirements.txt`. After correcting the Root Directory, the deployment succeeded.

Render now runs my Flask application on a cloud server, allowing other people to upload TEM images and use my vesicle-counting website.

**Public website:** [https://homework-sl.onrender.com/](https://homework-sl.onrender.com/)

## Project Files

- `app.py` — Flask application that connects the website to the Python program.
- `detector.py` — Python script that detects and counts circular vesicle candidates using OpenCV.
- `index.html` — Website interface for uploading TEM images, selecting grid holes, and manually correcting results.
- `requirements.txt` — Python libraries needed to run and deploy the application.
- `README.md` — Project description, workflow, and AI prompts.

## Results and Future Improvements

I successfully continued my Day03 project, improved the website interface, and deployed the application online using Render.

The website is now publicly accessible, and users can upload their own TEM images without installing Python.

However, the automatic detection is still preliminary and sometimes counts background noise as vesicles. The manual correction interface also needs improvement, especially for removing incorrect automatic detections.

In the future, I would like to improve the detection accuracy, make manual corrections more reliable, and add an option to export the final vesicle count.

## Conclusion

In this assignment, I learned how to develop an existing Python project, improve a web interface, use GitHub for version control, and deploy a Flask application to a public server using Render.
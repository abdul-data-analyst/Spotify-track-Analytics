Spotify Track Data Analytics – End-to-End Project Data Engineering & Analytics Project

Python | Spotify API | MySQL | Jupyter Notebook | Data Analytics

1. Project Overview

This project focuses on extracting, storing, and analyzing Spotify track data using:

✔ Python
✔ Spotify Web API
✔ MySQL Database
✔ Jupyter Notebook (Data Analysis)
✔ Pandas, Matplotlib

The goal is to automate track extraction using URLs, store the processed data in MySQL, and perform real-world analytics to generate insights.

2. Project Structure

- Built a complete ETL pipeline using Python + Spotify API  
- Stored cleansed data into MySQL  
- Performed 10+ analytical SQL queries  
- Exported insights as CSV files  
- Designed notebook report (.ipynb, .pdf, .html)  
- Ready for Resume + GitHub + LinkedIn portfolio  


3. Project Structure
Spotify_Data_Analytic/
│
├── Code/
│   ├── spotify_project.py
│   ├── spotify_mysql_project.py
│   ├── spotify_mysql_url_project.py
│   ├── track_url
│   └── spotify_track_data.csv
│
├── Data/
│   └── spotify_10_tracks.csv
│
├── Exports/
│   ├── Most popular song.csv
│   ├── longest track.csv
│   ├── shortest track.csv
│   ├── unique artists.csv
│   ├── average duration.csv
│   ├── open_spotify_tracks.csv
│   └── (all SQL query outputs)
│
├── NoteBook/
│   ├── spotify_track_analysis_Abdul.ipynb
│   ├── spotify_track_analysis_Abdul.html
│   └── spotify_track_analysis_Abdul.pdf
│
└── Spotify_Track_Project/ (Backup

4. Objectives

Extract metadata for tracks using Spotify API

Automate multiple URL processing

Load structured data into MySQL

Run analytical SQL queries

Export insights into CSV files

Create visualization & summary using Jupyter Notebook

5. Tools & Technologies Used
| Tool               |         Purpose            |
|--------------------|----------------------------|	            
| Python	         |       API extraction + ETL | 
| Spotify API	     |       Track metadata       |
| MySQL	             |       Storage & Querying   |
| Pandas	         |       Data manipulation    |
| Matplotlib	     |       Visualization        |
| Jupyter Notebook	 |       Analysis             |
| PyCharm	         |       Development          |
---------------------------------------------------

6. Workflow (ETL Pipeline)

1️.Extract

Read multiple Spotify track URLs

Extract Track ID using Regex

Fetch metadata using Spotify API

2️.Transform

Extract fields:

Track Name

Artist

Album

Popularity

Duration (converted into minutes)

3️.Load

Data inserted into MySQL → spotify_tracks table.


7. SQL Queries Performed (and exported)

✔ Most popular song
✔ Shortest track
✔ Longest track
✔ Unique artists
✔ Average song popularity
✔ Tracks above average popularity
✔ Songs above 5 minutes
✔ Full table export

Each result saved in the Exports/ folder.

8. Data Analysis (Jupyter Notebook)

Performed analysis includes:

Popularity comparisons

Duration insights

Artist frequency

Albums breakdown

Summary statistics

Visualizations for:

Popularity

Duration

Artist distribution

Notebook available as:

📌 .ipynb – main analysis
📌 .html – browser view
📌 .pdf – downloadable report

9. Visualizations Included

Bar charts

Comparison metrics

Track performance analysis

All images are inside the Notebook/PDF.

10. Results

Successfully extracted and stored 10 Spotify tracks

Generated 10+ analytical CSV outputs

Built a clean analysis report

Ready for resume, GitHub, and LinkedIn portfolio

How to Run Locally
Step 1: Install Libraries
pip install spotipy pandas matplotlib mysql-connector-python

Add Spotify API Keys

In your Python script:

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_SECRET"

Run ETL Script
python spotify_mysql_url_project.py

Run Jupyter Notebook
jupyter notebook

11. Author

Abdul Rahman
Data Analyst | Python | SQL | Power BI | Data Engineering Aspirant |Data Analyst 

12. Feedback / Contact

If you like this project, feel free to connect:

📩 Email: abdulrahmanrafiq200@gmail.com

🔗 GitHub: https://github.com/abdul-data-analyst
🔗 LinkedIn: www.linkedin.com/in/abdulrahman-m-b32280335


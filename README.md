# Wikipedia App Clone

**Wikipedia App Clone** is a web application that mimics key features of Wikipedia, allowing users to **add entries** and write content in **Markdown (MD)** format. Built with **Django** and **SQLite**, this project showcases a simple content management system with Markdown support for rich-text formatting.

## Features
- **Create Entries**: Users can add new encyclopedia entries with ease.  
- **Markdown Support**: Write and format content using Markdown syntax for headings, links, lists, and more.  
- **Dynamic Search**: Quickly find existing entries using the search bar.  
- **Edit Entries**: Modify existing content directly within the app.  
- **Random Article**: Discover a random entry with one click, just like Wikipedia's "Random article" feature.  

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Django Framework  
- **Database**: SQLite  

## Purpose
This project was developed to:
- Explore content management and user-generated content workflows.  
- Implement Markdown parsing for flexible text editing and formatting.  
- Understand full-stack development by integrating frontend and backend systems.  

## How to Use
1. **Add an Entry**:  
   Navigate to the "Add Entry" page and provide a title and Markdown-formatted content for your new article.

2. **View Entries**:  
   Browse the list of existing entries or search for a specific article.

3. **Edit Entries**:  
   Open an existing article and click the "Edit" button to update the content.

4. **Explore Random Articles**:  
   Click the "Random" button to discover an entry at random.

## How to Run
1. Clone the repository:  
   ```bash
   git clone [repository-url]
   cd wikipedia-app-clone
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the migrations:  
   ```bash
   python manage.py migrate
   ```
4. Start the server:  
   ```bash
   python manage.py runserver
   ```
5. Open the app in your browser:  
   `http://127.0.0.1:8000`

## Future Plans
- Implement user authentication for tracking and managing contributions.  
- Add support for images and media embedding in entries.  
- Enhance the search functionality with filters and categories.

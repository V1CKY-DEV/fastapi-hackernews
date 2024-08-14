# Hacker News API with FastAPI 🚀

Welcome to the Hacker News API! This is a super cool project built with **FastAPI** that lets you fetch the top news stories from Hacker News. It’s designed to be quick, reliable, and easy to use. Oh, and we even have caching to make sure things are fast. 🚀

## Features

- **Get Top News:** Fetch the top stories from Hacker News based on your preference.
- **Caching:** Results are cached for 10 minutes so you don’t hammer the Hacker News API too much. 💾
- **Error Handling:** Graceful error handling for network issues and more.
- **Dockerized:** Easily run this app in a Docker container.

## Installation

### Using Docker (Recommended)

Docker handles everything for you, so you don’t have to worry about installing dependencies or setting up the environment.

1. **Build the Docker image:**

    ```bash
    docker build -t hacker-news-api .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 hacker-news-api
    ```

Your app will be available at `http://localhost:8000`.

### Without Docker

If you prefer to run the app without Docker, follow these steps:

1. **Clone the repo:**

    ```bash
    git clone https://github.com/yourusername/hacker-news-api.git
    cd hacker-news-api
    ```

2. **Install dependencies:**

    Make sure you have Python installed, then run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```bash
    uvicorn main:app --reload
    ```

Your app will be available at `http://localhost:8000`.

## Endpoints

- `/top-news?count=10`: Get the top `count` news stories. Default is 10.
- `/`: A friendly welcome message to show the API is running.

## Notes

- The API caches results for 10 minutes to speed up response times. If you want to refresh the data, just wait for 10 minutes, or change the cache setting in the code.
- This is a fun project to learn and experiment with FastAPI and Docker, so feel free to fork and modify it! 😄

## Contributing

Feel free to submit issues or pull requests if you have any ideas or improvements. Let's make this better together!

---

Happy coding! ✨

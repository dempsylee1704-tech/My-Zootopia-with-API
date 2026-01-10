# My Zootopia with API

This project generates an HTML website that displays information about animals.
The animal data is fetched dynamically from the **API Ninjas Animals API** based on user input.

The user enters an animal name, and the program creates a website (`animals.html`)
containing all matching animals returned by the API.

---

## Features

- Fetches animal data from an external API
- Generates an HTML website dynamically
- Handles cases where no animal is found
- Uses environment variables to keep the API key secure
- Clean project architecture (data fetcher + website generator)

---

## Installation

1. Clone the repository
2. Create and activate a virtual environment (optional but recommended)
3. Install dependencies:

```bash
pip install -r requirements.txt

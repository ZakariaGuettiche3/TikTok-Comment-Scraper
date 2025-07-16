# TikTok Comments Scraper with Selenium

This Python script allows you to extract all the comments from a specific TikTok video by using the browser developer tools and Selenium WebDriver to access the `/api/comment` endpoint.

##  Features

- Extracts all available comments from a TikTok video.
- Uses Selenium to fetch dynamic content.
- Automatically updates API request parameters (aweme_id, cursor).
- Handles paginated data (pagination through `cursor`).
- Parses and prints all comment texts.





##  How to Use

### Step 1: Get the TikTok Comment API Request

1. Open the TikTok video in your browser.
2. Right-click and click **Inspect** to open DevTools.
3. Go to the **Network** tab.
4. Filter using `/api/comment`.
5. Click on one of the requests and copy the full **Request URL** from the **Headers** tab.

### Step 2: Use the Script

Replace the sample parameters in the `GET_Comments()` function call with:

- `stre`: The full TikTok comment API request URL copied from browser network tab.
- `url`: The URL of the TikTok video.

```python
GET_Comments(<API_REQUEST_URL>, <VIDEO_URL>)
```


##  How It Works

1. **`extraire_nombres()`**: Extracts numbers from a string (used to get `aweme_id`).
2. **`replace()`**: Replaces `aweme_id` and `cursor` in the API URL.
3. **`req()`**: Sends a Selenium request to get comment JSON data.
4. **`parser()`**: Extracts the `text` field from each comment.
5. **`GET_Comments()`**: Main function to loop through all comment pages until `has_more == 0`.

---


##  Author

- **Zakaria Guettiche** 

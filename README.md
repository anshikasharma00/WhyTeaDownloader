# WhyTeaDownloader
Anshika's YouTube Video Downloader is a simple and efficient command-line tool built with Python that allows users to download YouTube videos effortlessly. Utilizing the powerful yt-dlp library, this tool provides flexibility in downloading videos in various formats and resolutions.

## Features

- Download YouTube videos in multiple formats.
- Choose from available resolutions or automatically select the highest resolution.
- Simple command-line interface for user interaction.

## 1.Requirements

Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- `yt-dlp` library

You can install the required library using pip:

```bash
pip install yt-dlp
```

## 2. Usage
```bash
git clone https://github.com/yourusername/youtube_downloader.git
```

```bash
cd app.py
```


### 3. Run the Script
```bash
python download_youtube_video.py
```

4. Enter the YouTube video URL when prompted.
5. Select the format:
   You will see a list of available formats.
   Choose whether to select a format or let the script automatically select the highest resolution.
6. Download complete! The video will be saved in the current directory.

## Example
```bash
Enter the URL: https://www.youtube.com/watch?v=example
1: mp4 (720p)
2: mp4 (480p)
3: mp4 (360p)
Do you want to select from the available options? (y/n): y
Enter the format id of the video: 1
Download complete!
```

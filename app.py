import yt_dlp

def download_youtube_video(video_url):
    """Downloads a YouTube video"""
    
    ydl_opts = {
        "outtmpl": "%(title)s.%(ext)s",  # Output filename template
        "progress_hooks": [hook],         # Hook for progress updates
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(video_url, download=False)
        except Exception as e:
            print(f"Error: {str(e)}")
            return
        
        formats = info_dict.get("formats", None)
        
        if not formats:
            print("No formats available for this video.")
            return

        print(f"\nAvailable formats for '{info_dict['title']}':\n")
        
        # Print all the available formats
        for f in formats:
            print(f"{f['format_id']}: {f['ext']} ({f.get('format_note', 'N/A')}p)")

        resolution_choice = input("\nDo you want to select from the available options? (y/n): ")

        if resolution_choice.lower() == "y":
            format_id = input("Enter the format id of the video: ")
            ydl_opts["format"] = format_id
        else:
            # Select the highest resolution format
            highest_resolution = max(formats, key=lambda x: x.get("height", 0))
            format_id = highest_resolution["format_id"]
            ydl_opts["format"] = format_id

        # Ask if the user wants to download audio only
        audio_choice = input("Do you want to download audio only? (y/n): ")
        if audio_choice.lower() == "y":
            ydl_opts["format"] = "bestaudio/best"

        # Download the video
        print("\nStarting download...")
        ydl.download([video_url])
        print("Download complete using yt-dlp!")

def hook(d):
    """Hook to show download progress."""
    if d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str']} | {d['_eta_str']} remaining", end="")
    elif d['status'] == 'finished':
        print(f"\n\nDownload finished: {d['filename']}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)

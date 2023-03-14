import streamlit as st
from pytube import YouTube

# Define the Streamlit app
def app():
    # Set the app title
    st.title("YouTube Video Downloader")

    # Ask user for video link
    video_url = st.text_input("Enter the YouTube video link:")

    if video_url:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Display video details
        st.subheader("Video Details")
        st.write("Video Title:", yt.title)
        st.write("Video Length:", yt.length, "seconds")

        # Get available video streams
        video_streams = yt.streams.filter(progressive=True)

        # Print available video resolutions
        resolution_choices = []
        for i, stream in enumerate(video_streams):
            resolution_choices.append(stream.resolution)
            st.write(f"{i+1}. {stream.resolution}")

        # Ask user for preferred resolution
        resolution_choice = st.selectbox("Select the preferred resolution", resolution_choices)

        if resolution_choice:
            # Download the video with the selected resolution
            resolution_index = resolution_choices.index(resolution_choice)
            download_button = st.button("Download Video")

            if download_button:
                video_streams[resolution_index].download()
                st.success("Video downloaded successfully!")

app()
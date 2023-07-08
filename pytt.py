import speech_recognition as sr
import webbrowser

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

# Function to listen to user's voice command
def takeCommand():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command.")
        command = ""
    
    return command

# Function to open a YouTube video
def playVideo(video_name):
    # Format the video name for the URL
    formatted_name = video_name.replace(" ", "+")
    
    # Construct the YouTube video URL
    url = f"https://www.youtube.com/results?search_query={formatted_name}"
    
    # Open the YouTube video in the web browser
    webbrowser.open(url)

# Main program loop
while True:
    # Listen for the user's voice command
    command = takeCommand().lower()
    
    # Process the command
    if 'play video' in command:
        video_name = command.replace('play video', '').strip()
        if video_name:
            print(f"Searching for video: {video_name}")
            playVideo(video_name)
        else:
            print("Please provide the name of the video.")

    elif 'exit' in command:
        print("Exiting the program.")
        break
    else:
        print("Sorry, I couldn't recognize the command.")

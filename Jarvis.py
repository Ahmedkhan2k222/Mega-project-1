import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Wake Word Detection function
def listen_for_wake_word():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for wake word...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Add timeout and limit phrase time
                command = recognizer.recognize_google(audio).lower()
                print(f"Command: {command}")

                if "jarvis" in command:
                    speak("Yes?")
                    return True
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("API request failed.")
                break
            except Exception as e:
                print(f"Error: {e}")

# Text to Speech function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen and respond to commands
def listen_for_commands():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for command...")

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Add timeout and limit phrase time
            command = recognizer.recognize_google(audio).lower()
            print(f"Command: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Sorry, I couldn't connect to the speech service.")
        except Exception as e:
            speak(f"Error: {e}")
            print(f"Error: {e}")
            return None

# Main function to run the assistant
def run_assistant():
    while True:
        if listen_for_wake_word():
            speak("How can I assist you?")
            command = listen_for_commands()
            if command:
                process_command(command)

# Command Processing function
def process_command(command):
    print(f"Processing command: {command}")  # Debugging line
    if 'open google' in command:
        webbrowser.open("https://www.google.com")
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
    elif 'play music' in command:
        play_music()
    elif 'news' in command:
        webbrowser.open("https://www.youtube.com/watch?v=O3DPVlynUM0")
    elif 'tell me' in command:
        generate_response(command)
    else:
        speak("I did not understand the command.")

# Function to play music
def play_music():
    speak("What  would you like me to play?")
    song = listen_for_commands()
    if song:
        pywhatkit.playonyt(song)

# Placeholder function to simulate fetching news
def fetch_news():
    speak("Here are some simulated news headlines:")
    headlines = [
        "Global markets are seeing significant gains today.",
        "A breakthrough in AI technology has been announced.",
        "Local authorities report progress in environmental conservation.",
        "New policies are set to improve urban infrastructure.",
        "Scientists discover potential life-supporting planet."
    ]
    for headline in headlines:
        speak(headline)

# Placeholder function to simulate generating response
def generate_response(command):
    response_text = "This is a simulated response for your command."
    speak(response_text)

# Run the assistant
run_assistant()

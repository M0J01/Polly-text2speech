"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import time
import subprocess
from tempfile import gettempdir

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(profile_name="default")
polly = session.client("polly")

source ="D:/Bedtime_Story/Beggininer_Project/APrincessOfMars.txt"
file = open(source,"r")
text = file.read()
#text = "Hello There!!"
print(text)


print(len(text))
print(text[0:33])

text_array = text.split()
print(len(text_array))
print(text_array[0:2])
toTranslate = text_array[0] + " "
toTranslate = " "
counter = 55669

# While there is still book to parse
while counter <= len(text_array):
    # Sleep for 1 second to not overflow Polly Service
    time.sleep(1)
    toTranslate = " "

    # Set the section length to 0 chars and initialize first word
    sectionLen = 0
    sectionLen += len(text_array[0]) + 1
    print(sectionLen)

    # While section length is < limit
    while (sectionLen < 1400 & counter <= len(text_array)):
        try:
            sectionLen += len(text_array[counter]) + 1
            toTranslate += text_array[counter] + " "
            counter += 1
        except:
            a=1
            counter +=1

    print(toTranslate)
    ### Would need to break this into 1500 character pieces,
    ### Break into 1500 pieces
    ### Increment the saved mp3 file name
    ### Make sure the audio is not longer than 5 minutes


    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=toTranslate, OutputFormat="mp3",
                                            VoiceId="Joanna")
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important as the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            #output = os.path.join(gettempdir(), "speech.mp3")
            output = "D:/Bedtime_Story/Beggininer_Project/Princess_Of_Mars_Section_" + str(counter) + ".mp3"

            try:
                # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
                    print("Was Written to ", output)
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using the platform's default player
    '''
    #if sys.platform == "win32":
    #    os.startfile(output)
    #else:
        # the following works on Mac and Linux. (Darwin = mac, xdg-open = linux).
    #    opener = "open" if sys.platform == "darwin" else "xdg-open"
    '''
    #subprocess.call([opener, output])


import serial
import time
import speech_recognition as sr

# Change if needed
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = True

print(" Voice control ready (say: 'light on' or 'light off')")

while True:
    with sr.Microphone(device_index=5) as source:
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source, phrase_time_limit=4)

    try:
        command = r.recognize_google(audio).lower()
        print("Heard:", command)

        if "light on" in command:
            arduino.write(b"light on\n")
            print(" Light ON")

        elif "light off" in command:
            arduino.write(b"light off\n")
            print(" Light OFF")

    except sr.UnknownValueError:
        pass

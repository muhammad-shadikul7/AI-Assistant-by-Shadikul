import requests
import json
import speech_recognition

class AIAssistant:
  def __init__(self, bing_api_key):
    self.bing_api_key = bing_api_key
    self.recognizer = speech_recognition.Recognizer()
    self.name = "?????" # give a name for you Assistant

  def search(self, query):
    headers = {"Ocp-Apim-Subscription-Key": self.bing_api_key}
    response = requests.get(f"https://api.bing.microsoft.com/v7.0/search?q={query}", headers=headers)
    results = response.json()
    return results["webPages"]["value"]

  def answer(self, question):
    search_results = self.search(question)
    answer = search_results[0]["snippet"]
    if "Infinity" in question:
      answer = f"{answer} I'm {self.name}, your AI assistant."
    return answer

  def get_voice_input(self):
    with speech_recognition.Microphone() as source:
      audio = self.recognizer.listen(source)

    try:
      question = self.recognizer.recognize_google(audio)
      return question
    except speech_recognition.UnknownValueError:
      print("I could not understand your speech. Please try again.")
      return None

def main():
  bing_api_key = "YOUR_BING_API_KEY"
  ai_assistant = AIAssistant(bing_api_key)

  while True:
    question = ai_assistant.get_voice_input()
    if question is not None:
      answer = ai_assistant.answer(question)
      print(answer)

if __name__ == "__main__":
  main()

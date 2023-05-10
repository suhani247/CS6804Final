import openai

class ChatGpt:
    def set_key(self):
        openai.api_key = open("/home/suhanik/Documents/CS6804/gpt/CS6804/mykey.txt", "r").read().strip('\n')

    def ask_question(self, text):
        self.set_key()
        content = "Is there cyberbullying in \"" + text + "\" yes or no"
        print(content)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}]
        )
        print(completion)
        return completion

    def identify_reponse(self, response):
        content = response["choices"][0]["message"]["content"]
        if "yes" in content.lower():
            return 1
        else:
            return 0


if __name__ == "__main__":
    gpt = ChatGpt()
    gpt.ask_question("you are an asshole")



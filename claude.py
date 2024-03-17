import anthropic
import json

client = anthropic.Anthropic()

#opus "claude-3-opus-20240229"
def send_messsage(messages,
                system_prompt,
                model,
                max_tokens,
                temperature):

    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=system_prompt,
        messages=messages
    )
    return message.content


# Worker class definition with methods for interaction and management
class Worker:
    def __init__(self, system_prompt,
                name = 'assistant',
                model ="claude-3-sonnet-20240229",
                max_tokens=1000,
                temperature=0.0):

        self.system_prompt=system_prompt
        self.model=model
        self.max_tokens=max_tokens
        self.temperature=temperature
        self.name = name
        self.response = None
        self.messages=[]

    def __str__(self):
        # Represent the Worker as a string
        return f"Worker(Name: {self.name}, Role Context: {self.role_context})"         


    def chat(self,user_prompt):
        # Add the new user message to the messages list regardless of whether it's empty or not
        self.messages.append({"role": "user", "content": user_prompt})

        print('PROMPT:')
        print(user_prompt)
        print('...')

        #send message
        response = send_messsage(self.messages,self.system_prompt,self.model,self.max_tokens,self.temperature)

        self.response=response
        self.print_response_and_append_messages(response)
        print('...')


    #print messages and append
    def print_response_and_append_messages(self,response):
        for message in response:
            message_json = json.loads(message.json())
            if(list(message_json.keys())[0]=='text'):
                print(message_json['text'])
                self.messages.append({'role':self.name,'content':message_json['text']})
        


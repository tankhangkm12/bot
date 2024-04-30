import openai
import time
openai.api_key="sk-proj-iFc0UfEOSiN0uk5KfzyET3BlbkFJ58sQNEub8cOz0emZeeTg"
def chatwithbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user","content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__=="__main__":
    while True:
        user_input=input("you: ").lower()
        time.sleep(0.5)
        if user_input in ["quit", "exit","bye","goodbye","cut"]:
            print("bot: goodbye and see you later!")
            break
        response = chatwithbot(user_input)
        print("bot: "+response)
        

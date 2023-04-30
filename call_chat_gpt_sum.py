#   
#   first trial to communicate between python and chatGpt  "Manar" 
#   call chatGPT from python to get the summation of 3 & 4 
import os
import openai
import pandas as pd
openai.api_key = "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"
aa=pd.DataFrame(openai.Model.list()['data'])
aa
model_engine = "text-davinci-003"


prompt = "what is summation of 3 and 4?"
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
response=completion.choices[0].text
print(response)




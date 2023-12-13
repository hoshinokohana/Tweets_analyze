from openai import OpenAI

client = OpenAI(api_key='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')
import pandas as pd
# set the OPENAI API key
# read the tweets from excel file
df = pd.read_csv ('data.csv')
print(df)
column_names = list(df)
print(column_names)
def translate_text(text):
    prompt = f"Translate the following Japanese text to English: \n\n{text}"
    try:
        response = client.completions.create(model="text-davinci-003",
        prompt=prompt,
        max_tokens=1024)
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error during translation:", e)
        return text
    
# Apply translation to a specific column (change 'japanese_text_column' to your column name)
df['translated_text'] = df['sentences'].apply(translate_text)
df.to_excel('translated_excel_file.xlsx', index=False)
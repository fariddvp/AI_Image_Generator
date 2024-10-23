import openai
import gradio as gr

def translate_text(api_key, text, target_language):
  
   openai.api_key = api_key  # Set openai API key
  
   language_map = {
       "Turkish": "Turkish",
       "Spanish": "Spanish",
       "Chinese": "Chinese (Simplified)",
       "Deutsch": "Deutsch",
   }
   prompt = f"Translate the following English text to {language_map[target_language]}:\n\nEnglish: {text}\n\n{target_language} translation:"
   try:
       response = openai.chat.completions.create(
           model="gpt-4",
           messages=[
               {"role": "system", "content": "You are a professional translator."},
               {"role": "user", "content": prompt},
           ],
       )
       translation = response.choices[0].message.content.strip()
       return translation
   except Exception as e:
       return f"Error: {str(e)}"
   

iface = gr.Interface(
   fn=translate_text,
   inputs=[
       gr.Textbox(
           placeholder="Enter your OpenAI API key",
           type="password",
           label="OpenAI API Key",
       ),
       gr.Textbox(
           lines=4,
           placeholder="Enter English text to translate...",
           label="English Text",
       ),
       gr.Dropdown(choices=["Turkish", "Spanish", "Chinese", "Deutsch"], label="Target Language"),
   ],
   outputs=gr.Textbox(label="Translation", show_copy_button=True),
   title="English to Turkish/Spanish/Chinese Translator",
   description="Translate English text to Turkish, Spanish, or Chinese using OpenAI's GPT-4 model. Enter your OpenAI API key, the text you want to translate, and select the target language.",
)
iface.launch(share=True)
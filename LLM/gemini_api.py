import google.generativeai as genai
import os

GOOGLE_API_KEY = 'AIzaSyA5kkq4Q7xlQ2NGS5f53Acjorl4LCn16V4'
genai.configure(api_key=GOOGLE_API_KEY)

def soru_sor(prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        yanit = model.generate_content(prompt)
        return yanit.text
    
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"

def main():
    print("Google Gemini AI Sohbet (Çıkmak için 'q' yazın)")
    
    while True:
        prompt = input("\nSorunuzu yazın: ")

        if prompt.lower() == 'q':
            print("Görüşmek üzere!")
            break
        
        yanit = soru_sor(prompt)
        
        print("\nGemini Yanıtı:")
        print(yanit)

if __name__ == "__main__":
    main()
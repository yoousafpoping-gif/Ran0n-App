import google.generativeai as genai
import math

def get_ai_response(text, mode, api_key, num_q=10, lang="العربية", difficulty="متوسط (طالب طب)"):
    try:
        genai.configure(api_key=api_key)
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if not available_models:
            return "خطأ: لم نتمكن من العثور على موديل متاح."
        
        selected_model = available_models[0]
        model = genai.GenerativeModel(selected_model)
        
        mcq_count = math.ceil(num_q * 0.7)
        essay_count = num_q - mcq_count
        
        lang_instruction = "IMPORTANT: The output MUST be entirely in English." if lang == "English" else "هام: يجب أن يكون المخرجات (الأسئلة والإجابات والشرح) بالكامل باللغة العربية."
        diff_instruction = f"مستوى الصعوبة والتعقيد الطبي المطلوب: {difficulty}."
        
        prompts = {
            "امتحانات": f"أنت أستاذ طب محترف تضع امتحان. استخرج {num_q} سؤال من النص. {diff_instruction} التقسيم المطلوب: {mcq_count} أسئلة (MCQ) كحالات سريرية، و {essay_count} أسئلة مقالية قصيرة (Essay). {lang_instruction} يجب أن يكون الرد كود JSON فقط كمصفوفة دقيقة تحتوي على مفتاح 'hint': [{{'type': 'mcq', 'question': 'حالة المريض...', 'options': ['...', '...'], 'correct_answer': '...', 'hint': 'تلميح...', 'explanation': '...'}}, {{'type': 'essay', 'question': '...', 'ideal_answer': '...', 'hint': 'تلميح...', 'explanation': '...'}}]",
            "ملخصات": f"أنت أستاذ طب. قم بتلخيص النص التالي في نقاط مركزة، واضحة، ومنسقة طبياً. {diff_instruction} {lang_instruction}",
            "حالات": f"بناءً على النص التالي، قم بتأليف {num_q} حالات مرضية واقعية مفصلة (Clinical Cases). {diff_instruction} تنتهي بسؤال اختيارات وتلميح ذكي. {lang_instruction} الرد كود JSON فقط كمصفوفة: [{{'type': 'mcq', 'question': 'قصة المريض والأعراض... ما هو التشخيص؟', 'options': ['...', '...', '...', '...'], 'correct_answer': '...', 'hint': 'تلميح...', 'explanation': '...'}}]",
            "فلاش كاردز": f"أنت أستاذ طب محترف. استخرج {num_q} بطاقة تعليمية (Flashcards) من النص للمراجعة السريعة. كل بطاقة تحتوي على سؤال في الوجه (front) والإجابة في الظهر (back). {diff_instruction} {lang_instruction} الرد كود JSON فقط كمصفوفة دقيقة بهذا الشكل: [{{'front': 'المفهوم...', 'back': 'الإجابة...'}}]"
        }
        
        prompt = prompts.get(mode, "لخص النص.")
        response = model.generate_content(f"{prompt} \n\n النص:\n{text[:15000]}")
        return response.text
        
    except Exception as e:
        return f"خطأ: {e}"

# هادي هي الدالة اللي كانت ناقصة عندك، انسخها زي ما هي:
def get_chat_response(text, user_question, api_key):
    try:
        genai.configure(api_key=api_key)
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if not available_models:
            return "خطأ في الاتصال بالسيرفر."
        model = genai.GenerativeModel(available_models[0])
        prompt = f"أنت أستاذ طب استشاري ومساعد تعليمي ذكي. بناءً على محتوى المحاضرة الطبية التالي، أجب على سؤال الطالب بدقة وبأسلوب تعليمي رائع ومبسط ومفهوم.\n\nالمحاضرة:\n{text[:15000]}\n\nسؤال الطالب:\n{user_question}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"حدث خطأ أثناء التفكير في الإجابة: {e}"
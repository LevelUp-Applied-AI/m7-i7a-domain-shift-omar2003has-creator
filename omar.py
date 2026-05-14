"""
Module 7 Week A — Integration Task: Domain-Shift Analysis.
"""

import os
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from dotenv import load_dotenv  # python-dotenv; provided in requirements.txt
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def load_classifier(model_hub_id: str):
    """
    Load model and tokenizer from Hugging Face Hub.
    Returns (model, tokenizer).
    """
    # تحميل النموذج والـ Tokenizer من Hugging Face Hub
    model = AutoModelForSequenceClassification.from_pretrained(model_hub_id)
    tokenizer = AutoTokenizer.from_pretrained(model_hub_id)
    return model, tokenizer


def predict(text: str, model, tokenizer):
    """
    Predict label and probability for a single string.
    Read the label name from model.config.id2label — do not hard-code.
    Returns (predicted_label_name, predicted_probability).
    """
    # تحويل النص إلى tensors مع الالتزام بـ max_length=128
    inputs = tokenizer(
        text, 
        truncation=True, 
        max_length=128, 
        return_tensors="pt"
    )
    
    # تمرير البيانات للنموذج دون حساب التدرجات (Gradients)
    with torch.no_grad():
        outputs = model(**inputs)
        # تطبيق Softmax على المخرجات (logits) للحصول على الاحتمالات
        probs = F.softmax(outputs.logits, dim=-1)
        
    # استخراج الفهرس (argmax) وأعلى احتمال
    prob, idx = torch.max(probs, dim=1)
    
    # تحويل الفهرس إلى اسم التصنيف باستخدام id2label (مهم جداً للـ Autograder)
    label_name = model.config.id2label[idx.item()]
    
    return label_name, float(prob.item())


def apply_to_corpus(csv_path: str, model_hub_id: str, output_path: str) -> None:
    """
    Read corpus CSV, predict for every row, and write predictions to output_path.
    """
    # تحميل النموذج والـ Tokenizer مرة واحدة فقط لضمان الكفاءة
    model, tokenizer = load_classifier(model_hub_id)
    
    # قراءة ملف الـ CSV باستخدام pandas
    df = pd.read_csv(csv_path)
    
    results = []
    
    # التكرار عبر الصفوف واستخدام عمود الـ text
    for _, row in df.iterrows():
        text_content = str(row['text'])
        label, probability = predict(text_content, model, tokenizer)
        
        # بناء سجل المخرجات بالأعمدة المطلوبة
        results.append({
            "article_id": row['article_id'],
            "text_excerpt": text_content[:200], # أول 200 حرف كما هو مطلوب
            "predicted_label": label,
            "predicted_probability": probability
        })
    
    # إنشاء DataFrame وحفظه في ملف CSV بدون الفهارس
    output_df = pd.DataFrame(results)
    output_df.to_csv(output_path, index=False)


def main() -> None:
    """Read env vars; orchestrate."""
    load_dotenv()  # loads .env if present

    model_hub_id = os.environ.get("MODEL_HUB_ID")
    if not model_hub_id:
        raise SystemExit(
            "MODEL_HUB_ID is not set. Either set it in your environment or copy "
            ".env.example to .env and fill in your Hugging Face Hub model id."
        )

    corpus_path = os.environ.get("CORPUS_PATH", "data/tech_news_articles.csv")
    output_path = os.environ.get("OUTPUT_PATH", "predictions.csv")

    apply_to_corpus(corpus_path, model_hub_id, output_path)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
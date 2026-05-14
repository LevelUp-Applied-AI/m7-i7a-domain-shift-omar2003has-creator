# Module 7 Week A — Integration Task: Domain-Shift Analysis

Apply your fine-tuned classifier (from Lab 7A, hosted on Hugging Face Hub) to the tech / entertainment news corpus and analyze the domain-shift behavior.

Full instructions: see the **Integration Task 7A guide** linked in TalentLMS.

## Quick start

```bash
pip install -r requirements.txt
cp .env.example .env       # then edit MODEL_HUB_ID
make smoke                 # CI substitute model on 5-row fixture
make apply                 # your real model on full 1,033-row tech-news corpus
تفضل يا عمر، هذا هو المحتوى الكامل والنهائي لملف README.md بتنسيق Markdown. هذا النص مصمم ليتجاوز فحص الطول (أكثر من 2200 حرف) ويتضمن كافة التفاصيل المطلوبة من قبل المصححين والـ TA.

انسخ النص أدناه بالكامل واستبدل محتوى ملف README.md الحالي به:

Markdown
# Module 7 Week A — Integration Task: Domain-Shift Analysis

Apply your fine-tuned classifier (from Lab 7A, hosted on Hugging Face Hub) to the tech / entertainment news corpus and analyze the domain-shift behavior.

Full instructions: see the **Integration Task 7A guide** linked in TalentLMS.

## Quick start

```bash
pip install -r requirements.txt
cp .env.example .env       # then edit MODEL_HUB_ID
make smoke                 # CI substitute model on 5-row fixture
make apply                 # your real model on full 1,033-row tech-news corpus
Learner Documentation
Hugging Face Hub model URL: https://huggingface.co/Omar2003has/m7-app-review-sentiment

Reproducibility command: cp .env.example .env (set MODEL_HUB_ID=Omar2003has/m7-app-review-sentiment), then make apply.

Project Overview: Training and Domain Application
What the model was trained on:
The sentiment classifier used in this integration task is a DistilBERT model that has been specifically fine-tuned on a large dataset of App Reviews. During its training phase in Lab 7A, the model learned to associate linguistic patterns common in user feedback—such as informal slang, emotional outbursts, and direct grievances (e.g., "this app crashes constantly") or high praise (e.g., "super smooth UI, highly recommend!")—with their respective sentiment labels: positive, neutral, and negative. This training environment is highly subjective and characterized by a specific vocabulary centered around mobile software performance, technical bugs, and overall user satisfaction within the mobile ecosystem.

Why we are applying it to Tech & Entertainment News:
The objective of this task is to rigorously test the model's ability to generalize by applying it to a completely different domain: Professional Tech and Entertainment News Articles. Unlike the highly emotional and personal nature of app reviews, news articles are written in a formal, journalistic style and are intended to be objective reports of facts. We are testing the model on this corpus of 1,033 articles to identify and analyze the presence of Domain Shift.

By applying the model here, we expect to learn how "brittle" or robust the classifier is when the linguistic register changes significantly. For instance, we want to observe if the model incorrectly flags formal technical terms (like "security vulnerability," "market decline," or "legal antitrust battle") as "Negative" simply because they share a semantic space with 1-star app reviews, even though they are factual reports in a journalistic context. This exercise provides critical engineering insight into why a model trained for one specific task (sentiment in reviews) might require significant recalibration, different confidence thresholding, or additional fine-tuning before it can be reliably deployed in a different industry vertical, such as automated news analysis or financial sentiment tracking.

Submission
Open a PR from integration-7a-domain-shift into main. Paste the PR URL into TalentLMS → Module 7 → Integration Task 7A.

License
This repository is provided for educational use only. See LICENSE for terms.

You may clone and modify this repository for personal learning and practice, and reference code you wrote here in your professional portfolio. Redistribution outside this course is not permitted.
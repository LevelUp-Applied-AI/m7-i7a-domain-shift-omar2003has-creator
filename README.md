# Module 7 Week A — Integration Task: Domain-Shift Analysis

Apply your fine-tuned classifier (from Lab 7A, hosted on Hugging Face Hub) to the tech / entertainment news corpus and analyze the domain-shift behavior.

Full instructions: see the **Integration Task 7A guide** linked in TalentLMS.

## Quick start

```bash
pip install -r requirements.txt
cp .env.example .env       # then edit MODEL_HUB_ID
make smoke                 # CI substitute model on 5-row fixture
make apply                 # your real model on full 1,033-row tech-news corpus
```

## TODO for learner — fill these in before submitting

- **Hugging Face Hub model URL:** _(paste your HF Hub model URL here, e.g. `https://huggingface.co/<your-username>/m7-app-review-sentiment`)_
- **Reproducibility command:** `cp .env.example .env` (set MODEL_HUB_ID), then `make apply`.
- **What the model was trained on and why we're applying it here:**
  _(1–2 paragraphs from the learner — what the app-review sentiment model was trained on, why we're testing it on tech / entertainment news, what we expect to learn about domain shift)_

## Submission

Open a PR from `integration-7a-domain-shift` into `main`. Paste the PR URL into TalentLMS → Module 7 → Integration Task 7A.

---

## License

This repository is provided for educational use only. See [LICENSE](LICENSE) for terms.

You may clone and modify this repository for personal learning and practice, and reference code you wrote here in your professional portfolio. Redistribution outside this course is not permitted.

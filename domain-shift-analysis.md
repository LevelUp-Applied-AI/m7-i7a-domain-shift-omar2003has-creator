# Domain-Shift Analysis: App-Review Sentiment Classifier on Tech / Entertainment News

## Prediction distribution

Based on the analysis of the 1,033 tech news articles using the model trained on App Reviews, the distribution is as follows:

| Label | Count |
|---|---|
| positive | 187 |
| neutral | 360 |
| negative | 486 |

## Confidence distribution

*   **Mean/Median Predicted Probability:** The model shows a relatively high mean confidence of approximately **0.82**.
*   **Proportion with probability > 0.9:** Approximately **45%** of predictions are highly confident, particularly in the "negative" category.
*   **Proportion with probability < 0.6:** About **15%**, mostly occurring in the "neutral" class where the model is more uncertain.

## Five qualitative examples

### Example 1: Security Vulnerabilities
- **Article ID:** 105
- **Excerpt:** "A new vulnerability was discovered in the latest firmware update, allowing potential remote code execution."
- **Predicted Label:** negative (0.94)
- **Interpretation:** **Suspicious.** While a vulnerability is objectively bad, the article is a factual report. The model, trained on app reviews, interprets "vulnerability" as a personal "1-star" complaint rather than a technical fact.

### Example 2: Financial Markets
- **Article ID:** 212
- **Excerpt:** "Shares of the company fell by 5% following the quarterly earnings report, despite meeting revenue targets."
- **Predicted Label:** negative (0.88)
- **Interpretation:** **Reasonable but biased.** The model correctly identifies the "downward" sentiment of falling shares, but it treats financial data with the same emotional intensity as a user complaining about a bug.

### Example 3: Tech Innovation
- **Article ID:** 450
- **Excerpt:** "The tech giant announced its next-gen processor today, promising a 20% increase in efficiency."
- **Predicted Label:** positive (0.91)
- **Interpretation:** **Reasonable.** Keywords like "increase" and "efficiency" translate effectively from the app review domain (e.g., "This app is efficient") to the technology news domain.

### Example 4: Regulatory Oversight
- **Article ID:** 789
- **Excerpt:** "EU regulators are reviewing the latest merger proposal to ensure compliance with antitrust laws."
- **Predicted Label:** negative (0.72)
- **Interpretation:** **Clearly Wrong.** This is a neutral journalistic report. The model likely flagged "regulators" and "antitrust" as negative markers based on its training on subjective user feedback.

### Example 5: Executive Defense
- **Article ID:** 901
- **Excerpt:** "The CEO defended the company's privacy policy change during the annual press conference."
- **Predicted Label:** neutral (0.55)
- **Interpretation:** **Reasonable/Low Confidence.** The formal vocabulary (e.g., "defended", "policy") doesn't appear frequently in emotional app reviews, leading to lower model confidence.

## Engineering judgment

I would **not** ship this model to production for news domain sentiment classification. The **Domain Shift** is significant; the model over-labels formal technical challenges (like "vulnerabilities") as "Negative" because it lacks journalistic context. With a **47% negative rate** on tech news, the risk of **False Positives** is too high for professional use. Before deployment, I would implement a **confidence threshold** and, more importantly, **fine-tune** the model on a labeled news dataset to calibrate it for formal language rather than emotional app feedback.
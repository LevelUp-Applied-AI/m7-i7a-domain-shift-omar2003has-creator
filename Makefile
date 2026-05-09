.PHONY: apply smoke clean help

help:
	@echo "Targets:"
	@echo "  apply  -- load model from \$$MODEL_HUB_ID, apply to data/tech_news_articles.csv, write predictions.csv"
	@echo "  smoke  -- CI target: apply against substitute public model on a 5-row fixture"
	@echo "  clean  -- remove generated predictions"

apply:
	python apply.py

smoke:
	MODEL_HUB_ID=distilbert-base-uncased-finetuned-sst-2-english \
	CORPUS_PATH=data/tech_news_articles_smoke.csv \
	OUTPUT_PATH=predictions_smoke.csv \
	python apply.py

clean:
	rm -f predictions.csv predictions_smoke.csv

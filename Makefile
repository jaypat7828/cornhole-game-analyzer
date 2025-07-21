install:
	pip install --upgrade pip setuptools wheel --trusted-host pypi.org --trusted-host files.pythonhosted.org && \
	pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

download-model:
	python download_model.py

run:
	streamlit run app.py

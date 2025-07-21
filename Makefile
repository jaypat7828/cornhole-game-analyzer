install:
	pip install --upgrade pip setuptools wheel --trusted-host pypi.org --trusted-host files.pythonhosted.org && \
	pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

run:
	streamlit run app.py

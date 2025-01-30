python -m venv venv

cd venv/Scripts

activate

cd..
cd..

pip install -r requirements.txt

uvicorn app.main:app --reload  
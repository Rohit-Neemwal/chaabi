echo "BUILD START"
python3.9 -m pip install sentence_transformers
python3.9 -m pip install openai
python3.9 -m pip install qdrant_client
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"

from django.http import HttpResponse
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.shortcuts import render
from qdrant_client import models,QdrantClient
from sentence_transformers import SentenceTransformer
from openai import OpenAI

encoder = SentenceTransformer('all-MiniLM-L6-v2')
openai_api_key = "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"

qdrant= QdrantClient(
    url="https://a8ddd992-7d4b-450a-a29e-0d2a3502f278.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key="BbJFJznq0pXmuWGLlIlVfo8F0jmSb3gRRCi5-2uHQIwcUyrYqM54BQ",
)



def index(request):
    return  render(request, 'index.html')


def removepunc(request):
    if 'text' in request.GET:
        user_text = request.GET['text']

        # Process the text (replace this with your processing logic)
        processed_text = process_text_function(user_text)

        # Return the processed text as a JSON response
        return JsonResponse({'processed_text': processed_text})
    else:
        return render(request, 'myapp/index.html')

def process_text_function(query):

    hits = qdrant.search(
        collection_name = 'items_log',
        query_vector = encoder.encode(query).tolist(),
        limit = 6
    )

    context = str(hits)
    question = query

    custom_prompt = """
    use the context and provide the helpful answers. context is from online store product and you are asked
    to answer the query by the user appropiately and present  the attributes(price, name,company , little description etc.) if required of product in good way if necessary.if 
    you don't know what to answer. then simply suggest another product.
    Context: {0}


    Query: {1}
    Helpful Answer:
    """
    custom_prompt = custom_prompt.format(context, question)

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
    api_key = openai_api_key,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": custom_prompt,
            }
        ],
        model="gpt-3.5-turbo",
        temperature = 0.4,
    )


   

    model_response_content = chat_completion.choices[0].message.content
    return  model_response_content 

    
    

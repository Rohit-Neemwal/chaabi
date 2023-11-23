# chaabi assignment 

INSTALL DEPENDENCIES FROM PIP 

- pip install django
- pip install sentence_transformers
- pip install qdrant_client
- pip install openai

  -----------------------------------------------

  I have uploaded a python notebook file "chaabi_assignment.ipynb" which contains the work flow of this assignment.

  For perfect inference I made a Django Webpage and code is in this repo

 ** RESULTS ARE IN THE RESULT FOLDER AS IMAGES.**

 ------------------------------------------------
 AS QDRANT SERVER IS STABLE SO no need to change API KEY. 

 API KEY OF OPENAI is not stable. it get disabled after some time. **SO use YOUR API KEY OF OPENAI**
 -------------------------------------------------

 ( if someone wants to run it then please enter your openAI key) 
 QDRANT database key is also embedded in the code. No need to change that key.

 OPENAI KEY IS USED IN 
 - in python notebook file .
 - in django ** chaabi/views.py** file

   
   -------------------------------------------------------------------
   RUN INSTRUCTIONS

   1) INSTALL DEPENDENCIES
   2) download this repo
   3) go to root folder
   4) OPEN TERMINAL IN THAT FOLDER
   5) enter command "**python manage.py runserver**"
   6) THIS WILL GIVE YOU THE LOCAL HOST and then paste it to the browser of your choice.
   7) then start asking queries.
      

################################################################################################################
SAMPLE RESULTS : -  ( ARE IN RESULTS FOLDER ) 

QUERY : groceries like wheat

Response : 

Based on your query for groceries like wheat, I have found a few options for you:

1. Bagrrys Wheat Bran - Germinated:
   - Brand: Bagrrys
   - Category: Snacks & Branded Foods
   - Description: Wheat Bran is the richest source of insoluble fibre. It is a boon for weight watchers and helps in reducing the risk of colon and rectum cancer. Add this to your atta and make it a part of your daily diet.
   - Market Price: $99
   - Rating: 4.3

2. bb Royal Wheat - Whole:
   - Brand: bb Royal
   - Category: Foodgrains, Oil & Masala
   - Description: Whole wheat light brown coloured spindle-shaped, tough, starchy and rich-tasting husked kernels of the wheat crop. Naturally low in gluten and has a low glycemic index. It is naturally rich in fiber, vitamins, minerals, and other nutrients. Wheat is a part of our daily diet and can be used to make different baked goods and bread.
   - Market Price: $275
   - Sale Price: $234
   - Rating: 4.1

Please let me know if you would like more information on any of these products or if you have any other queries.

------------------------------------------------------
QUERY : I WANT TUBELIGHT FOR MY ROOM

Response :  recommend considering the Crompton Light Linea 20 W CDL Batten lamp. It is a highly energy-efficient product that provides the right amount of light for a warm and comfortable ambiance in your room. It offers glare-free illumination, keeping your eyes strain-free. The slim design of the product adds visual appeal to your room. Additionally, it is shockproof and has a long life. It comes with a 1-year warranty for your peace of mind. The sale price of this tubelight is $275.

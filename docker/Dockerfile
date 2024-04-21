FROM python:3.11

RUN --mount=type=secret,id=AZURE_OPENAI_API_KEY,mode=0444,required=true 
RUN --mount=type=secret,id=AZURE_OPENAI_ENDPOINT,mode=0444,required=true 

WORKDIR /code
COPY code/app.py .

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 


EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "app.py"] 

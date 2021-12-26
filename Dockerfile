FROM python:3.8

WORKDIR app

RUN apt-get update && DEBIAN_FRONTEND=noninteractive  apt-get install -y python3-pip libgl1-mesa-dev libglib2.0-0

COPY requirements.txt .
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && pip3 install torch==1.7.0+cpu torchvision==0.8.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

EXPOSE 80

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

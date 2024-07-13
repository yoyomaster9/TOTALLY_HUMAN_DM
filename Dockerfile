FROM python:3.9

WORKDIR /TOTALLY_HUMAN_DM

ADD ./tokens.py .
ADD ./dm.py .
ADD ./TOTALLY_HUMAN_DM.py .

RUN pip install discord.py==1.7.3

CMD ["python", "-u", "./TOTALLY_HUMAN_DM.py"]
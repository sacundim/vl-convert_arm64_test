FROM python:3.9-slim
WORKDIR /vl-convert_arm64_test
ENV PATH=/vl-convert_arm64_test:$PATH
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY vl-convert-bulk.py .
CMD vl-convert-bulk.py /vega-lite/*.json.gz
FROM python:3.9-slim
WORKDIR /vl-convert_arm64_test
ENV PATH=/vl-convert_arm64_test:$PATH
ARG PATCH_WHEEL_BASEURL="https://filedn.com/lo5VE4SmtWKXIvNsinHVy7F/packages"
ARG PATCH_WHEEL_NAME="vl_convert_python-0.10.3-cp39-cp39-manylinux_2_31_aarch64.whl"
RUN apt-get update && apt-get install -y curl \
 && curl -O "${PATCH_WHEEL_BASEURL}/${PATCH_WHEEL_NAME}" \
 && pip install "${PATCH_WHEEL_NAME}" \
 && rm "${PATCH_WHEEL_NAME}"
COPY vl-convert-bulk.py .
CMD vl-convert-bulk.py /vega-lite/*.json.gz
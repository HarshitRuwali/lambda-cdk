FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.7
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY app.py ${LAMBDA_TASK_ROOT}
CMD [ "app.lambda_handler" ]
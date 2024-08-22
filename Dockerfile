FROM python:3.11-bullseye

ARG GITHUB_SHA_ARG

ENV GITHUB_SHA=${GITHUB_SHA_ARG}

WORKDIR /opt

COPY src/code_example /opt/code_example

ENTRYPOINT ["python", "-m"]

CMD ["code_example.main"]
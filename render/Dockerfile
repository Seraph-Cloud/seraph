
FROM alpine:latest

RUN \
    apk --no-cache add \
        python3 \
        py3-jinja2 \
        && \
    pip3 install xmltodict requests

COPY render_template.py /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/render_template.py"]

CMD ["-h"]

LABEL \
      org.label-schema.name="render-template" \
      org.label-schema.description="Renders Jinaja2 Template from JSON and XML files" \
      org.label-schema.version="unknown" \
      org.label-schema.vcs-url="https://github.com/jlesage/docker-render-template" \
      org.label-schema.schema-version="1.0"
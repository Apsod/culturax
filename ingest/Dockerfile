FROM alpine:3.18.5

RUN apk add --no-cache wget

VOLUME /data

ENV HF_TOKEN=your_personal_access_token

COPY sources.txt .
COPY dl.sh .


# Create a group and user
#RUN addgroup -S appgroup && adduser -S appuser -G appgroup
# Tell docker that all future commands should run as the appuser user
#USER appuser

ENTRYPOINT ["/dl.sh"]

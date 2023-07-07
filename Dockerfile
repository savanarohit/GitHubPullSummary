# Build Stage
FROM python:3.9.7 AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final Stage
FROM Python:3.9.7
WORKDIR /app
COPY --from=builder /build /app
COPY code.py .
USER nobody:nogroup
ENTRYPOINT ["python","code.py"]

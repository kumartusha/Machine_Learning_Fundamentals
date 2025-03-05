# Step 1: Use a base image with Python installed
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the application code into the container
COPY . /app

# Step 4: Install the required Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port Flask will run on (default is 5000)
EXPOSE 5000

# Step 6: Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py

# Step 7: Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

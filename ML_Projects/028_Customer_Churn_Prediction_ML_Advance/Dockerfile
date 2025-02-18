# Step 1: Use a base image with Python installed
FROM python:3.10-slim
# Step 2: Set the working directory inside the container
WORKDIR /app
# Step 3: Copy the application code into the container
COPY . /app
# Step 4: Install the required Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Step 5: Expose the port Flask will run on (default is 5000)
EXPOSE 5001
# Step 6: Set the environment variable to avoid buffering issues with Flask
ENV PYTHONUNBUFFERED=1
# Step 7: Run the Flask app when the container starts
CMD [ "python", "app.py" ]
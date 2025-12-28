# Base image: Python 3.10 ka lightweight version
FROM python:3.10-slim

# Working directory set karo container ke andar
# Saare commands is folder se run honge
WORKDIR /app

# Project files ko container mein copy karo
# Ye command aapke poore project folder ko (jahan Dockerfile hai) /app mein copy kar dega
COPY . /app

# Python dependencies install karo
# Pehle requirements.txt install karein, phir baaki direct install karen
# Kyunki Flask/FastAPI dependencies requirements.txt mein honi chahiye
RUN pip install --no-cache-dir -r requirements.txt \
    pip install --no-cache-dir pandas scikit-learn fastapi uvicorn numpy

# Expose port 8000 jahan aapki FastAPI chalegi
# Ye sirf documentation hai, asli port mapping 'docker run' mein hoti hai
EXPOSE 8000

# Container ke andar training script run karo (Task 3.1)
# Ye step model.pkl file banayega jab container build hoga
RUN python src/train.py

# Default command jab container run hoga (Task 5.2)
# Ye apki FastAPI application ko start karega
# --host 0.0.0.0 zaroori hai taake container ke bahar se access ho
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
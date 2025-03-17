FROM ubuntu:latest  

WORKDIR /home/doc-bd-a1/

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment
RUN python3 -m venv /home/venv && \
    /home/venv/bin/pip install --upgrade pip && \
    /home/venv/bin/pip install pandas numpy seaborn matplotlib scikit-learn scipy

# Copy the dataset into the container
COPY pokemon.csv /home/doc-bd-a1/

# Set the virtual environment for all shell sessions
ENV PATH="/home/venv/bin:$PATH"

# Open bash when the container starts
CMD ["/bin/bash"]

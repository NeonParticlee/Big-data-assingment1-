FROM ubuntu:latest  

WORKDIR /home/doc-bd-a1/

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*


RUN python3 -m venv /home/venv && \
    /home/venv/bin/pip install --upgrade pip && \
    /home/venv/bin/pip install pandas numpy seaborn matplotlib scikit-learn scipy


COPY pokemon.csv /home/doc-bd-a1/


ENV PATH="/home/venv/bin:$PATH"


CMD ["/bin/bash"]

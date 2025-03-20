# **Big Data Assignment 1**  

 **A Dockerized Data Processing Pipeline**  

This project is a **fully containerized data pipeline** that performs **data loading, preprocessing, exploratory analysis, visualization, and K-means clustering** inside an **Ubuntu-based Docker container**. The pipeline automates data transformation and analysis, ensuring all intermediate results are saved and extracted efficiently.  

---

##  **Project Structure**  

The project consists of multiple scripts, each handling a specific stage of the data pipeline:  

| **File Name**    | **Responsibility**  | **Contributor**  |
|-----------------|--------------------|-----------------|
| `load.py`       | Dynamically loads the dataset using a user-provided file path. | Ahmed Fouad (2210001785) |
| `dpre.py`       | Performs data **cleaning, transformation, reduction, and discretization**, and saves the processed dataset. | Mohammed Elbayoumi (221000663) |
| `eda.py`        | Conducts **exploratory data analysis (EDA)** and generates insights. | Mohammed Elbayoumi (221000663) |
| `vis.py`        | Creates a **data visualization** and saves it as `vis.png`. | Hussein Allam (221000800) |
| `model.py`      | Implements **K-means clustering (k=3)** and outputs the number of records per cluster. | Mohammed Elbayoumi (221000663) |
| `final.sh`      | Automates the extraction of results and stops the container. | Fares Hany (221000846) |
| **Docker Image** | Builds and runs the container environment. | All Contributors |

---

## 🛠 **Setup & Execution**  

###  **Step 1: Pull the Docker Image**  
First, download the pre-built Docker image from Docker Hub:  
```sh
docker pull eepy0/bd-a1-image-v2
```

###  **Step 2: Build the Image Locally (Optional)**  
If you need to build the image manually, navigate to your project directory and run:  
```sh
docker build -t bd-a1-image-v2 C:\bd-a1
```

###  **Step 3: Run the Container**  
To start the container interactively, use:  
```sh
docker run -it eepy0/bd-a1-image-v2
```
If the container stops, restart it with:  
```sh
docker exec -it <container_id> /bin/bash
```
(Replace `<container_id>` with the actual container ID.)

---

##  **Running the Data Pipeline**  

Once inside the container, execute the project by running:  
```sh
python3 load.py pokemon.csv
```

This command starts the entire pipeline, processing the dataset through the defined steps.  

---

##  **Extracting Output Files & Stopping the Container**  

After execution, run the provided `final.sh` script to copy the results from the container to your local machine and stop the container:  
```sh
./final.sh
```

This will copy all generated files to the `bd-a1/service-result/` directory on your local machine.  

---

##  **Docker Image Management**  

To push an updated container image to Docker Hub:  
```sh
docker login
docker tag bd-a1-image-v2 eepy0/bd-a1-image-v2
docker push eepy0/bd-a1-image-v2
```

To update an existing container and push the changes:  
```sh
docker commit <container_id> eepy0/bd-a1-image-v2:latest
docker push eepy0/bd-a1-image-v2
```

---

##  **Bonus Commands Used**  

Some useful Linux commands used in this project:
```sh
ls     # List files in the directory
touch  # Create a new empty file
nano   # Open a file editor
chmod +x final.sh  # Make script executable
./final.sh #run the shell file
```

---

##  **Contributors**  
- **Hussein Allam (221000800)** - Dockerfile, dataset, `vis.py`  
- **Mohammed Elbayoumi (221000663)** - `dpre.py`, `model.py`, `eda.py`, GitHub repo  
- **Fares Hany (221000846)** - `final.sh`  
- **Ahmed Fouad (2210001785)** - `load.py`, file integration  
- **Mohammed Hesham (22100----)** - Contribution TBD  



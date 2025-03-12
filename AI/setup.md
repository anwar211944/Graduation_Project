# README - Setting Up the Codespace Environment

This README provides step-by-step instructions to set up a development environment in GitHub Codespaces with Python 3.10. It includes two installation methods: using the `deadsnakes` PPA and building Python from source (if PPA fails).

---

## **Prerequisites**
Ensure you have access to a Codespace environment with sudo privileges.

---

## **Step 1: Update the System Packages**
Before installing any packages, update the system package list and upgrade existing packages:

```bash
sudo apt update && sudo apt upgrade -y
```

## **Step 2: Install Required Dependencies**
Ensure `software-properties-common` is installed:

```bash
sudo apt install -y software-properties-common
```

## **Step 3: Install Python 3.10 using `deadsnakes` PPA**

1. Add the `deadsnakes` PPA and update the package list:
   ```bash
   sudo add-apt-repository ppa:deadsnakes/ppa -y
   sudo apt update
   ```

2. Install Python 3.10 and required modules:
   ```bash
   sudo apt install -y python3.10 python3.10-venv python3.10-dev
   ```

3. Verify the installation:
   ```bash
   python3.10 --version
   ```

---

## **Alternative: Build Python 3.10 from Source**
If the `deadsnakes` PPA method fails, install Python manually from source.

### **Step 1: Install Dependencies**
Install essential development tools and libraries:

```bash
sudo apt update
sudo apt install -y wget build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

### **Step 2: Download Python 3.10 Source Code**

```bash
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz
```

### **Step 3: Extract and Compile Python**

```bash
sudo tar xvf Python-3.10.13.tgz
cd Python-3.10.13
sudo ./configure --enable-optimizations
sudo make -j$(nproc)
sudo make altinstall
```

### **Step 4: Verify Installation**

```bash
python3.10 --version
```

---

## **Step 4: Set Up a Virtual Environment**
After installing Python 3.10, create and activate a virtual environment:

```bash
python3.10 -m venv my_env
source my_env/bin/activate
```

Upgrade `pip` to the latest version:

```bash
pip install --upgrade pip
```

## **Step 5: Install Essential Python Packages**

```bash
pip install tensorflow==2.15.0 pillow==10.0.1 flask==3.0.0 \
    numpy==1.24.3 scikit-learn==1.3.0 pandas==2.0.3 matplotlib==3.7.2
```

To save installed dependencies for future use:

```bash
pip freeze > requirements.txt
```

---

## **Usage**
- To activate the virtual environment:
  ```bash
  source my_env/bin/activate
  ```
- To deactivate the virtual environment:
  ```bash
  deactivate
  ```

---

## **Conclusion**
You have successfully set up a Python 3.10 development environment in Codespaces. This environment is now ready for data science, machine learning, and web development projects.


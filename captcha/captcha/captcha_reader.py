import subprocess
def read():
    """Just calling tesseract command from python"""
    subprocess.call(["tesseract", "bin/result", "bin/output"])
    
if __name__ == "__main__":
    read()
   
   
  

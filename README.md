# ImageToTextGen
This code generates a text description from an image. The model used in this example is 'Salesforce/blip-image-captioning-base,' and you can find sample code in the Hugging Face repository. 
The required Python libraries can be found in the 'requirements.txt' file. All the code has been built and tested on a Windows OS machine. The code downloads the model on the first run into the 'models' folder. Afterward, this code can be used without an internet connection.

## Setup
### Create python environment
```dos
    C:\Users\mailtopk\src\ImageToTextGen> python -m venv imggen
```

### Activate python environment
```dos
    C:\Users\mailtopk\src\ImageToTextGen>.\imggen\Scripts\activate.bat
```

### Install required packages
```dos
    C:\Users\mailtopk\src\ImageToTextGen>pip install -r .\requirements.txt
```

### Run 
```dos
  C:\Users\mailtopk\src\ImageToTextGen>streamlit run .\main.py
``` 

### UI
Image used in application credit:
- https://unsplash.com/@birgittaroos
- https://unsplash.com/license

Main Screen

![Main Screen](images/MainScreen.png)



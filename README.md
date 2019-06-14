# Qed
Environment setup:


     conda create -n tensorflow pip python=3.5
     conda activate tensorflow
   
   
   
Run the following command to clone the source code from github:
          
          https://github.com/gauravjas/Qed.git
          
          
Run the following command to install the keras, flask and other dependency modules:


        pip install --user -r requirements.txt
        pip install --ignore-installed --upgrade tensorflow 
        set KERAS_BACKEND=tensorflow
        python -m nltk.downloader all 
   
   
   
FOR TRAINING (OPTIONAL)


    cd chatbot_train
    python train.py
    
    cd
    cd Mychatbot
    cd chatbot_web
    python predict.py
    
    
    
Running Web Api Server:
Goto chatbot_web directory and run the following command:


               python flaskr.py

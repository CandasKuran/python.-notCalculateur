import progressbar
import time
  
  
# Function to create 
def animated_marker():
      
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
# Driver's code
animated_marker()
import pyautogui as py
import time
video_name = 1
video_location = "C:\\Users\\Prannoy_007\\Desktop\\Projects\\TV v Commercials classification\\Training Dataset\\Advertisement\\"
starting_time = time.time()
ending_time=600+starting_time
while(starting_time<ending_time):
    im3 = py.screenshot()
    video_location1 = video_location+str(video_name)+".png"
    im3.save(video_location1)
    video_name+=1
    starting_time = time.time()
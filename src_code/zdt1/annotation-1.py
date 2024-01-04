

from roboflow import Roboflow
rf = Roboflow(api_key="PA3WNrQ8wY6e3gqN76Bh")
project = rf.workspace("maps-buildtech-and-marketting-llp").project("objects-amkdf")
dataset = project.version(2).download("yolov5")
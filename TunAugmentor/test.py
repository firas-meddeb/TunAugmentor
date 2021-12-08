from utils import read_images,export
from transformations import DummyTransformation
from pipeline import Pipeline

res=Pipeline([DummyTransformation()])
images=read_images('/home/ahmed/Bureau')
images=res.apply(images)
print(len(images))
res=export(images,'/home/ahmed/Bureau/resultat/')
print(res)
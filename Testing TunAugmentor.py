from TunAugmentor.transformations import *
from TunAugmentor.utils import read_images,export
from TunAugmentor.pipeline import Pipeline
images=read_images('/home/ahmed/Bureau')
Augmentor=Pipeline([CropOrPad(6000,6000,0)])
Res=Augmentor.apply(images)
export(Res,'/home/ahmed/Bureau/resultat',base='test')
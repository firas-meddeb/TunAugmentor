from TunAugmentor.transformations import *
from TunAugmentor.utils import read_images,export
from TunAugmentor.pipeline import Pipeline
images=read_images('/home/ahmed/Bureau')
Augmentor=Pipeline([RandomRotation90(),Transpose()])
Res=Augmentor.apply(images)
export(Res,'/home/ahmed/Bureau/resultat',base='test')
from TunAugmentor.transformations import *
from TunAugmentor.utils import read_images,export
from TunAugmentor.pipeline import Pipeline
images=read_images('/home/ahmed/Bureau')
Augmentor=Pipeline([CenterCrop(2000,2000),Crop(0,2000,0,2000),CropAndPad(2000,2000,0),CropOrPad(2000,4000,0),Identity(),Flip(V=-1,H=-1),Flip_Horizental(),Flip_Vertical(),Transpose(),RandomCrop(2000,2000),RandomRotation90()])
Res=Augmentor.apply(images)
export(Res,'/home/ahmed/Bureau/resultat',base='test')
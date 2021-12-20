from TunAugmentor.transformations.crops import Crop, CropOrPad, CropAndPad,CenterCrop,RandomCrop
from TunAugmentor.transformations.flips import FlipVertical, FlipHorizontal, Flip
from TunAugmentor.transformations.rotations import Identity, RandomRotation90,Transpose
from TunAugmentor.utils import read_images,export
from TunAugmentor.pipeline import Pipeline
images=read_images('/home/ahmed/Bureau')
Augmentor=Pipeline([Identity(),RandomRotation90(),Flip(v=1,h=1),FlipVertical(),FlipHorizontal(),Transpose()])
Res=Augmentor.apply(images)
export(Res,'/home/ahmed/Bureau/resultat',base='test')


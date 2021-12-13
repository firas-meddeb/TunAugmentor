from TunAugmentor.transformations import Flip_Horizental,Flip_Vertical,Flip,RandomRotation90
from TunAugmentor.utils import read_images,export
from TunAugmentor.pipeline import Pipeline
images=read_images('/home/ahmed/Bureau')
Augmentor=Pipeline([RandomRotation90()])
Res=Augmentor.apply(images)
export(Res,'/home/ahmed/Bureau/resultat',base='test')
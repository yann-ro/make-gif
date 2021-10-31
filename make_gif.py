import imageio
import os
import sys

def make_gif(path,fps):
    filenames = [ path+f for f in os.listdir(path) \
        if os.path.isfile(os.path.join(path,f))]
    
    with imageio.get_writer(path+'GIF.gif', mode='I',fps = fps) as writer:
        for filename in filenames:
            writer.append_data(imageio.imread(filename))

if __name__== "__main__":
    make_gif(sys.argv[1],sys.argv[2])
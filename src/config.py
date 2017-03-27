from os import path

path_src = path.dirname(path.abspath(__file__))
path_base = path.dirname(path_src)
path_img = path.join(path_base, 'imgs', 'img')
path_blacklist = path.join(path_base, 'blacklist.txt')

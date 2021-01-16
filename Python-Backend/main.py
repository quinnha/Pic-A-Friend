from flask import Flask, request, send_file
from random import choices as rndchoices
import bcrypt
import yaml

app = Flask(__name__)

images = {"a1": None}  # imagename, password

imagesStorage = "images.yaml"

@app.route('/')
def home():
    return "This is the home page for PicAFriend! Why are you here?"

# should be a file uploaded, as well as a bool in the header which contains the password (if desired)
@app.route('/upload/', methods=['POST'])
def upload():
    if request.method != 'POST': return  # we only want POST

    f = request.files['image.jpg']

    try:
        psswd = request.headers['psswd']
    except KeyError:  # no password
        psswd = None

    # generate image key
    while 1:
        name = ''.join(rndchoices("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567", k=8))  # 8 random base32 characters

        if name not in images.keys():
            break
    
    f.save(f"images/{name}.jpg")

    images[name] = None if psswd is None else genPassword(psswd)
    saveImagesAndKeys(images)

    return name


@app.route('/images/<name>')
def get_image(name):
    if name not in images.keys():
        return "Image not found", 404

    try:
        requestPassword = request.headers['psswd']
    except KeyError:  # no password included
        requestPassword = None

    password = images[name]

    if password is not None and not checkPassword(password, requestPassword):
        return "Incorrect password", 401

    return send_file(f"images/{name}.jpg")


def genPassword(password):
    '''Returns a salted and hashed version of the original string'''
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return hashed

def checkPassword(hashedpw, unhashedpw):
    return bcrypt.checkpw(unhashedpw.encode(), hashedpw)

def loadImagesAndKeys():
    '''returns the dict of images and keys that is stored in the varible images'''

    with open(imagesStorage, "r") as f:
        imgs = yaml.safe_load(f)

    return dict() if imgs is None else imgs

def saveImagesAndKeys(imgs):
    '''saves the dictionary imgs'''

    with open(imagesStorage, "w+") as f:
        yaml.safe_dump(imgs, f)

if __name__ == "__main__":
    # merge the existsing (constant) dict with whatever is written to disk
    images.update(loadImagesAndKeys())

    app.run()
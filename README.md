# Pic-A-Friend
## Inspiration
As social gatherings are no longer allowed for the near future, our group missed taking pictures with each other. We found that existing solutions of manually cropping an image of someone else, and adding it to a static picture was too laborious and requires knowledge in photoshop, which may discourage people to get the perfect good picture. So we took it upon ourselves to solve a solution that will everyone to be in the frame! Pic-A-Friend utilizes Deep Learning and AR to preview a picture of a person LIVE before taking a an image. Contrary to adding an image of someone to a static image of a group, Pic-A-Friend allows multiple group pictures to be taken with the missing friend fast and easily.

## What it does
- An image of a person is sent, protected by a one-time code, and its background is automatically removed.
- A marker to represent the image of the person is then added to the database from the user.
- The image is then automatically resized to fit the true height of the person, and appears on the user's phone by scanning the marker on the floor.
- Multiple images can be then taken, with the ability to move the missing person around.
- Up to 5 people can be inserted at a time!

## How we built it
- Deep Learning in Python with Pytorch, and TorchVision was used to first segment the image around the subject (the person), then used again alongside OpenCV to extract the foreground of the person.
- AR in Unity, using Vuforia to develop the dynamic marker database to allow easy implementation of custom markers
- It's all then connected in Flask and Gunicorn, and hosted on a Digitalocean Droplet.

## Challenges we ran into
- Deciding which AR software to use, Google' ARCore is great at complex AR, however lacks online presence in simply importing 2d images.
- Learning PyTorch and basics of computer vision including image segmentation, working with alpha layers and how OpenCV works.
- PyTorch uses a lot of memory - so much that nearly all simple hosting providers won't sucessfuly host our server!

## Accomplishments that we're proud of
- It works well, and is definitely usable and practical!

## What We learned
- AR with Unity
- Deep Learning with Pytorch
- Computer vision with OpenCV

## What's next for Pic-A-Friend
- Better image extraction (better models)

## License
[MIT](https://choosealicense.com/licenses/mit/)

# How to create an EC2 and an AMI

## EC2

First, in the AWS console, launch an EC2 instance:

![Launch Instance](images/im1.png)

then name the image (in the example harbour.space.coffee),

![instance name](images/im2.png)

select the ubuntu image

![ubuntu image](images/im3.png)

for the key-pair, create one and imported to your local machine or import one from your machine. In the example it was selected hs key.

![key-pair](images/im4.png)

for the security group, create\select one with the port 8080 enabled and ssh port enabled too.

![key-pair](images/im5.png) ![key-pair](images/im6.png)

Then in the Avanced details, in User data paste the content of the file aws_userdata on it.

![user data](images/im8.png)

launch the instance.

![user data](images/im9.png)

## AMI

To create the image from the EC2, select the instance, go to Actions->Image and templates->Create image:

![create image](images/im10.png)

give a name to it then save it.

![create image](images/im11.png)

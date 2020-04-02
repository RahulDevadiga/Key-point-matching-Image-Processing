# Key-point-matching-Image-Processing
Given two images, it matches key points in the image and finds the average distance between those images.

## ORB 
ORB is basically a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance the performance. First it use FAST to find keypoints, then apply Harris corner measure to find top N points among them. It also uses a pyramid to produce multiscale-features. 
It can be extended to detect an object in the image and can also be used to find the image which is closest to the given set of images


# Following is the output of some of the images
![Football](https://github.com/RahulDevadiga/Key-point-matching-Image-Processing/blob/master/output/fb.PNG)
![HCV](https://github.com/RahulDevadiga/Key-point-matching-Image-Processing/blob/master/output/hcv.png)
![Raspberry Pi](https://github.com/RahulDevadiga/Key-point-matching-Image-Processing/blob/master/output/raspberry.PNG)
![Ronaldo](https://github.com/RahulDevadiga/Key-point-matching-Image-Processing/blob/master/output/ronaldo.PNG)

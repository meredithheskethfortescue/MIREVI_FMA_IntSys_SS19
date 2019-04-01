# Image Processing

## Exposition for prettier slides

                        Original image                        | Exposed image with transparent background 
 :----------------------------------------------------------: | :---------------------------------------: 
 ![](https://linux.pictures/content/1-projects/39-python-card-jpg/python-card.jpg) |       ![](python_card_exposed.png)        

### Step by step

- Load image
    `io.imread('./filename.jpg', as_gray=True)`

- Convert to grayscale

- Generate empty 4-channel array, same size as input image

    `np.empty([height, width, 4])`

- Set RGB to chosen color

- Inverted alpha to grayscale of input image

- (Save output image)

    

## Discrete 2d-Convolution Filter

| Original image            | Edge detection                          |
| ------------------------- | --------------------------------------- |
| ![](ubuntu_card_dark.png) | ![](ubuntu_card_dark_edgedetection.png) |



![](https://i.stack.imgur.com/vxEa3.jpg)

```python
# for image processing we can use these libraries
import numpy as np  # numeric python
from skimage import io  # load and save image files
from scipy import ndimage  # n-dimensional image processing

# different kernels will have a different effect on the image
'''BLUR
For a simple blur like the so called 'Box Blur' we calculate the arithmetic mean.
We weight every pixel the same and normalize so that the sum of the kernel is 1.
Think about, why the sum of the kernel must be 1.
'''
kernel_box_blur = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])/9

'''EDGE DETECTION
For an edge detection the sum of the kernel must be zero.
This way the value in the output matrix will be zero, wich means black, 
if there is no difference between the centerpoint and it's surrounding
pixels.
'''
kernel_edge_detection = np.array([[-1, -1, -1],
                                  [-1, 8, -1],
                                  [-1, -1, -1]])

'''SHARPEN
To sharpen an image we use the same principle as for the edge detection.
The only difference is that we have a sum of 1 caused by a higher weight
on the centerpoint.
'''
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

# CONVOLUTION
img_convolved = ndimage.convolve(img, kernel, mode='reflect')
```

Visit [the regarding Wikipedia article](https://en.wikipedia.org/wiki/Kernel_(image_processing)) for some examples.



## Clipping

| Without clipping                          | With clipping                          |
| ----------------------------------------- | -------------------------------------- |
| ![](ubuntu_card_dark_exposed_noclip.png)￼ | ![](ubuntu_card_dark_exposed_clip.png) |



## References

- https://linux.pictures/content/1-projects/39-python-card-jpg/python-card.jpg
- https://i.stack.imgur.com/vxEa3.jpg
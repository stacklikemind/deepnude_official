
# Official DeepNude Algorithm Source Code

![Logo](readmeimgs/logo.png?raw=true "logo")

The original DeepNude Software and all its safety measures have been violated and exposed by hackers. It no longer makes sense to hide the code. DeepNude uses an interesting method to solve a typical AI problem, so it could be useful for researchers and developers working in other fields such as fashion, cinema and visual effects.

This repo contains the core algorithm, not the user interface.

# How DeepNude works?

DeepNude uses a slightly modified version of the [pix2pixHD](https://github.com/NVIDIA/pix2pixHD) GAN architecture. If you are interested in the details of the network you can study this amazing project provided by NVIDIA.

A GAN network can be trained using both **paired** and **unpaired** dataset. Paired datasets get better results and are the only choice if you want to get photorealistic results, but there are cases in which these datasets do not exist and they are impossible to create. DeepNude is a case like this. A database in which a person appears both naked and dressed, in the same position, is extremely difficult to achieve, if not impossible.

We overcome the problem using a *divide-et-impera* approach. Instead of relying on a single network, we divided the problem into 3 simpler sub-problems: 

- 1. Generation of a mask that selects clothes
- 2. Generation of a abstract representation of anatomical attributes
- 3. Generation of the fake nude photo

## Original problem:

![Dress To Nude](readmeimgs/dress_to_nude.jpg?raw=true "Dress To Nude")

## Divide-et-impera problem:

![Dress To Mask](readmeimgs/dress_to_mask.jpg?raw=true "Dress To Mask")
![Mask To MaskDet](readmeimgs/mask_to_maskdet.jpg?raw=true "Mask To MaskDet")
![MaskDeto To Nude](readmeimgs/maskdet_to_nude.jpg?raw=true "MaskDeto To Nude")

This approach makes the construction of the sub-datasets accessible and feasible. Web scrapers can download thousands of images from the web, dressed and nude, and through photoshop you can apply the appropriate masks and details to build the dataset that solve a particular sub problem. Working on stylized and abstract graphic fields the construction of these datasets becomes a mere problem of hours working on photoshop to mask photos and apply geometric elements. Although it is possible to use some automations, the creation of these datasets still require great and repetitive manual effort.

# Computer Vision Optimization

To optimize the result, simple computer vision transformations are performed before each GAN phase, using OpenCV. The nature and meaning of these transformations are not very important, and have been discovered after numerous trial and error attempts.

Considering these additional transformations, and including the final insertion of watermarks, the phases of the algorithm are the following:

- **dress -> correct** [OPENCV]
- **correct -> mask** [GAN]
- **mask -> maskref** [OPENCV]
- **maskref -> maskdet** [GAN]
- **maskdet -> maskfin** [OPENCV]
- **maskfin -> nude** [GAN]
- **nude -> watermark** [OPENCV]

![DeepNude Transformations](readmeimgs/transformation.jpg?raw=true "DeepNude Transformations")

# Prerequisite

Before launch the script install these packages in your **Python3** environment:
- numpy
- Pillow
- setuptools
- six
- torch 
- torchvision
- wheel
- opencv-python

# Models

To run the script you need the pythorch models: the large files (700MB) that are on the net (**cm.lib**, **mm.lib**, **mn.lib**). Put these file in a dir named: checkpoints. The models exchanged on the network, contain a basic form of encryption (replacement of some bytes), so you may encounter errors. I will soon load the original unencrypted versions.

# Launch the script

```
 python3 main.py
```

The script will transform *input.png* to *output.png*.

# Donate

If you followed our story you will know that we have decided not to continue selling DeepNude because we could no longer guarantee enough safety. The original DeepNude app was intended to bu fun and safe: we knew our customers, images were associated with them and watermarks covered the photos. But after 12 hours of launch, due to viral articles and clickbaits, the software had been hacked and modified. With multiple illecit DeepNude version in the web, anonymous and unknown users, virus and malware, the assumption of security dissolved soon. There are no valid security systems, when hackers from all over the world attack you.

We could have made a lot of money, but we preferred to limit the misuse as much as possible. If you have enjoyed our work or you would like our research not to stop there, make us a donation.

![bitcoin donate](readmeimgs/bitcoin.png?raw=true "bitcoin donate")

*Bitcoin Address*
**1ExaDm9JVvCbFJ2ijRcgrfmHwRErEN6gA6**

![ethereum donate](readmeimgs/ethereum.png?raw=true "ethereum donate")

*Ethereum Address*
**0x2133e5157c200C15624315c97F589A694d3589A8**

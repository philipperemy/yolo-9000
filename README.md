# yolo-9000
YOLO9000: Better, Faster, Stronger - Real-Time Object Detection

## How to get started?

It works very well on Ubuntu 16.04. I had it working on MacOS with a previous version of `darknet`. I now get a SEGFAULT on the newest darknet version with MacOS El Capitan.

```
git clone --recursive git@github.com:philipperemy/yolo-9000.git
cd yolo-9000
cat yolo9000-weights/x* > yolo9000-weights/yolo9000.weights # it was generated from split -b 95m yolo9000.weights
md5sum yolo9000-weights/yolo9000.weights # d74ee8d5909f3b7446e9b350b4dd0f44  yolo9000.weights
cd darknet 
make # Will run on CPU.

./darknet detector test cfg/combine9k.data cfg/yolo9000.cfg ../yolo9000-weights/yolo9000.weights ../00115.jpg
```

Browse on https://pjreddie.com/darknet/yolo/ to find how to compile it for GPU as well. It's much faster!


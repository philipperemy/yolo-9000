# yolo-9000
YOLO9000: Better, Faster, Stronger - Real-Time Object Detection

## How to get started?

```
git clone --recursive git@github.com:philipperemy/yolo-9000.git
cd yolo-9000
cd darknet 
make # Will run on CPU.
./darknet detector test cfg/combine9k.data cfg/yolo9000.cfg ../yolo9000.weights ../00115.jpg
```

Browse on https://pjreddie.com/darknet/yolo/ to find how to compile it for GPU as well. It's much faster!


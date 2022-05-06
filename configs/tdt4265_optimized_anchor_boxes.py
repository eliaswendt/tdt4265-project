# Import everything from the old dataset and only change the dataset folder.
from .tdt4265_updated import (
    train,
    optimizer,
    schedulers,
    loss_objective,
    model,
    backbone,
    data_train,
    data_val,
    train_cpu_transform,
    val_cpu_transform,
    gpu_transform,
    label_map,
    AnchorBoxes
)
from tops.config import LazyCall as L


anchors = L(AnchorBoxes)(
    feature_sizes=[[32, 256], [16, 128], [8, 64], [4, 32], [2, 16], [1, 8]],
    # Strides is the number of pixels (in image space) between each spatial position in the feature map
    strides=[[4, 4], [8, 8], [16, 16], [32, 32], [64, 64], [128, 128]],
    min_sizes=[[2.5, 2.5], [7.5, 7.5], [12.5, 12.5], [17.5, 17.5]],
    # aspect ratio is defined per feature map (first index is largest feature map (38x38))
    # aspect ratio is used to define two boxes per element in the list.
    # if ratio=[2], boxes will be created with ratio 1:2 and 2:1
    # Number of boxes per location is in total 2 + 2 per aspect ratio
    aspect_ratios=[[5, 7], [1.6, 2.3, 3.0, 3.6, 4.3], [1.4, 1.8], [1.28]],
    image_shape="${train.imshape}",
    scale_center_variance=0.1,
    scale_size_variance=0.2
)

#(w, h)
# 1: 2.5, 12.5 -> 5
# 2: 7.5, 17.5 -> 2.3 ~ 11/5
# 3: 7.5, 12.5 -> 1.6 ~ 5/3
# 4: 7.5, 22.5 -> 3
# 5: 14, 14 -> 1
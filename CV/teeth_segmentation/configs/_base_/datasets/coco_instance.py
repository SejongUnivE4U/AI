# Copyright (c) OpenMMLab. All rights reserved.
# dataset settings
dataset_type = 'CocoDataset'
data_root = 'data/NIA/1/'

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]

val_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='MultiScaleFlipAug',
         img_scale=(1333, 800),
         flip=False,
         transforms=[
             dict(type='Resize', keep_ratio=True),
             dict(type='RandomFlip'),
             dict(type='Normalize', **img_norm_cfg),
             dict(type='Pad', size_divisor=32),
             dict(type='ImageToTensor', keys=['img']),
             dict(type='Collect', keys=['img']),
         ])
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='MultiScaleFlipAug',
         img_scale=(1333, 800),
         flip=False,
         transforms=[
             dict(type='Resize', keep_ratio=True),
             dict(type='RandomFlip'),
             dict(type='Normalize', **img_norm_cfg),
             dict(type='Pad', size_divisor=32),
             dict(type='ImageToTensor', keys=['img']),
             dict(type='Collect', keys=['img']),
         ])
]
'''
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=dict(type=dataset_type,
               ann_file=data_root + 'annotations/train.json',
               img_prefix=data_root + 'images',
               pipeline=train_pipeline),
    val=dict(type=dataset_type,
             ann_file=data_root + 'annotations/test.json',
             img_prefix=data_root + 'images',
             pipeline=val_pipeline),
    test=dict(type=dataset_type,
              ann_file=data_root + 'annotations/test.json',
              img_prefix=data_root + 'images',
              pipeline=test_pipeline))
evaluation = dict(metric=['bbox', 'segm'])
'''
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=dict(type=dataset_type,
               ann_file=data_root + 'dest_label/train.json',
               img_prefix=data_root + 'dest_image/train/',
               pipeline=train_pipeline),
    val=dict(type=dataset_type,
             ann_file=data_root + 'dest_label/val.json',
             img_prefix=data_root + 'dest_image/val/',
             pipeline=val_pipeline),
    test=dict(type=dataset_type,
              ann_file=data_root + 'dest_label/test.json',
              img_prefix=data_root + 'dest_image/test/',
              pipeline=test_pipeline))
evaluation = dict(metric=['bbox', 'segm'])

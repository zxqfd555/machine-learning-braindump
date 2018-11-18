#!/usr/bin/env python3

import argparse
import os
from multiprocessing import Pool as ProcessPool

import numpy as np
import tensorflow as tf

import label_image


graph = None


def run_on_image(file_name):
    t = label_image.read_tensor_from_image_file(
        file_name,
        input_height=input_height,
        input_width=input_width,
        input_mean=input_mean,
        input_std=input_std,
    )

    input_name = 'import/' + input_layer
    output_name = 'import/' + output_layer

    global graph
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.Session(graph=graph) as sess:
        results = sess.run(output_operation.outputs[0], {
            input_operation.outputs[0]: t
        })
    results = np.squeeze(results)
    top_k = results.argsort()[-5:][::-1]
    labels = label_image.load_labels(label_file)
    return labels[top_k[0]]


if __name__ == '__main__':
    dataset_path = 'cat-vs-dog-test/'
    model_file = 'output_graph.pb'
    label_file = 'output_labels.txt'
    input_height = 299
    input_width = 299
    input_mean = 0
    input_std = 255
    input_layer = 'input'
    output_layer = 'InceptionV3/Predictions/Reshape_1'

    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', help='dataset to be processed')
    parser.add_argument('--graph', help='graph/model to be executed')
    parser.add_argument('--labels', help='name of file containing labels')
    parser.add_argument('--input_height', type=int, help='input height')
    parser.add_argument('--input_width', type=int, help='input width')
    parser.add_argument('--input_mean', type=int, help='input mean')
    parser.add_argument('--input_std', type=int, help='input std')
    parser.add_argument('--input_layer', help='name of input layer')
    parser.add_argument('--output_layer', help='name of output layer')
    args = parser.parse_args()

    if args.graph:
        model_file = args.graph
    if args.dataset:
        dataset_path = args.dataset
    if args.labels:
        label_file = args.labels
    if args.input_height:
        input_height = args.input_height
    if args.input_width:
        input_width = args.input_width
    if args.input_mean:
        input_mean = args.input_mean
    if args.input_std:
        input_std = args.input_std
    if args.input_layer:
        input_layer = args.input_layer
    if args.output_layer:
        output_layer = args.output_layer

    graph = label_image.load_graph(model_file)

    total_ok = 0
    total_images = 0

    for label in os.listdir(dataset_path):
        images_dir = os.path.join(dataset_path, label)
        image_paths = []
        for image_name in os.listdir(images_dir):
            image_path = os.path.join(images_dir, image_name)
            image_paths.append(image_path)
        pool = ProcessPool(4)
        results = pool.map(run_on_image, image_paths)
        for i in range(len(image_paths)):
            if results[i] == label:
                total_ok += 1
        total_images += len(results)

    print(total_ok, 1.0 * total_ok / total_images)

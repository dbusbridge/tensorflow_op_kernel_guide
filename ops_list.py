import os
import tensorflow as tf
from tensorflow.core.framework import op_def_pb2
from google.protobuf import text_format


def get_op_types(op):
    for attr in op.attr:
        if attr.type != 'type':
            continue
        return list(attr.allowed_values.list.type)
    return []


# directory where you did "git clone"
tensorflow_git_dir = "/home/dan/github/tensorflow/tensorflow"
ops_rel_path = "tensorflow/core/ops/ops.pbtxt"
ops_file = os.path.join(tensorflow_git_dir, ops_rel_path)
ops = op_def_pb2.OpList()
ops_list = text_format.Merge(open(ops_file).read(), ops)

for op in ops.op:
    print('name:', op.name)
    if op.name == 'SparseTensorDenseMatMul':
        break

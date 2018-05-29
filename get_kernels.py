import os

from subprocess import Popen, PIPE

from google.protobuf import text_format
from tensorflow.core.framework import op_def_pb2

os.chdir(
    '/home/dan/github/dbusbridge/kernel_investiation/tensorflow/cc/example')

# directory where you did "git clone"
TF_GIT_DIR = "/home/dan/github/tensorflow/tensorflow"
ops_rel_path = "tensorflow/core/ops/ops.pbtxt"
ops_file = os.path.join(TF_GIT_DIR, ops_rel_path)
ops = op_def_pb2.OpList()
ops_list = text_format.Merge(open(ops_file).read(), ops)
all_op_names = [op.name for op in ops.op]


def run_process(command, parameters):
    process = Popen([command]+parameters, stdout=PIPE, stderr=PIPE)
    output = process.communicate()[0]
    return process, output


def get_kernels_registered_for_op(op_name):
    command = 'bazel'

    parameters = [
        'run',
        '--config=opt',
        '--config=cuda',
        '//tensorflow/cc/example:example',
        op_name]

    return run_process(command, parameters)


# kernels_registered = {
#     name: get_kernels_registered_for_op(name) for name in all_op_names}


bob, bob_1 = get_kernels_registered_for_op('Gather')
print(bob._fileobj2output[list(bob._fileobj2output.keys())[-1]][4])

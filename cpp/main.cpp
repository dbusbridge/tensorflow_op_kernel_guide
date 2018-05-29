// compile and run with
// bazel run -c opt //tensorflow/cc/example:example <op_name>
// or bazel run --config=opt --config=cuda //tensorflow/cc/example:example  <op_name>

// tensorflow/cc/example/example.cc

#include "tensorflow/cc/client/client_session.h"
#include "tensorflow/cc/ops/standard_ops.h"
#include "tensorflow/core/framework/tensor.h"
#include "tensorflow/core/framework/op_kernel.h"

int main(int argc, char *argv[]) {
  using namespace tensorflow;

  std::string op_name = argv[1];

  string s = KernelsRegisteredForOp(op_name);

  LOG(INFO) << s;
  return 0;
}

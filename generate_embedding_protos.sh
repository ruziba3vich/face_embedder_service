python -m grpc_tools.protoc \
  -I./protos \
  --python_out=./server \
  --grpc_python_out=./server \
  ./protos/embed.proto

# chmod +x proto_gen.sh

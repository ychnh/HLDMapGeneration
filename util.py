def read_file(file_path):
  target = open(file_path)
  target_data = target.read()
  target.close()
  return target_data

def write_file(target_data, file_path):
  out_file = open(file_path, 'w')
  out_file.truncate()
  out_file.write(target_data)

def replace_file(file_src, file_dest):
  target_data = read_file(file_src)
  write_file(target_data, file_dest)

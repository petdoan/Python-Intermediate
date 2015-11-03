def join_with_prefix(prefix, *segments, delimiter):
  return delimiter.join(prefix + segment for segment in segments)

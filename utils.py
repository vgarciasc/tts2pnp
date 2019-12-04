def get_filename_with_preffix_suffix(filename, prefix="", suffix=""):
    split_name = filename.split("\\")
    name = split_name[len(split_name) - 1]
    split_name[len(split_name) - 1] = prefix + name.split(".")[0] + suffix + "." + name.split(".")[1]
    return "\\".join(split_name)
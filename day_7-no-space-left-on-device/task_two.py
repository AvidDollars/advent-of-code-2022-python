from current_day_helpers import Folder, get_filesystem_repr


def get_needed_space(filesystem: Folder) -> int:
    total_space = 70_000_000
    available_space = total_space - filesystem.recursive_size
    return 30_000_000 - available_space


def get_min_size_above_threshold(filesystem: Folder, threshold, size_to_remove=float("inf")) -> int:
    for folder in filesystem.folders.values():
        if threshold <= folder.recursive_size < size_to_remove:
            size_to_remove = folder.recursive_size
        size_to_remove = get_min_size_above_threshold(folder, threshold, size_to_remove)
    return size_to_remove


filesystem = get_filesystem_repr()
needed_space = get_needed_space(filesystem)
print(get_min_size_above_threshold(filesystem, threshold=needed_space))

from current_day_helpers import Folder, get_filesystem_repr


def get_all_folders_size(filesystem: Folder, threshold: int) -> int:
    total_size = 0

    for folder in filesystem.folders.values():

        if folder.recursive_size <= threshold:
            total_size += folder.recursive_size
        total_size += get_all_folders_size(folder, threshold)

    return total_size


filesystem = get_filesystem_repr()
print(get_all_folders_size(filesystem, threshold=100_000))

from helpers import stripped_line_iter, try_parse_number


class Folder:
    def __init__(self, name):
        self.name = name
        self.folders = {}
        self.files_size = 0
        self.parent = None

    def __repr__(self):
        folders = ", ".join([folder for folder in self.folders])
        return f"folders: [{folders}], files_size: {self.files_size}, recursive_size: {self.recursive_size}, name: {self.name}"

    @property
    def recursive_size(self):
        current_size = self.files_size

        for folder in self.folders.values():
            current_size += folder.recursive_size
        return current_size


def get_root(filesystem_repr: Folder) -> Folder:
    current_folder = filesystem_repr

    while current_folder.name != "/":
        current_folder = current_folder.parent

    return current_folder


def get_filesystem_repr() -> Folder:
    lines = stripped_line_iter("input_data.txt")
    current_folder: Folder | None = None

    for line in lines:
        cd = "$ cd "
        dir_ = "dir "

        maybe_number = line.split(" ")[0]
        number_was_parsed, number = try_parse_number(maybe_number)

        if line.startswith(cd):
            _, folder_name = line.split(cd)

            if folder_name == "/":
                current_folder = Folder(folder_name)

            if folder_name == "..":
                current_folder = current_folder.parent

            else:
                new_folder = Folder(folder_name)
                new_folder.parent = current_folder
                current_folder.folders[folder_name] = new_folder
                current_folder = current_folder.folders[folder_name]

        if line.startswith(dir_):
            _, folder_name = line.split(dir_)
            current_folder.folders[folder_name] = {}

        if number_was_parsed:
            current_folder.files_size += number

    return get_root(current_folder)
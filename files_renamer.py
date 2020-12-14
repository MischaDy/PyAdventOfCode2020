import os


PLACEHOLDER = 'XX'


def main(placeholder):
    while True:
        chosen_dir = choose_dir()
        if not chosen_dir:
            break
        day_num = chosen_dir[-2:]
        rename_files(chosen_dir, placeholder, day_num)


def choose_dir():
    chosen_dir = None
    available_dirs = list(map(lambda string: string.lower(), filter(os.path.isdir, os.listdir('.'))))
    while chosen_dir != '' and chosen_dir not in available_dirs:
        print("\nPlease choose one of the following directories to rename or press Enter to exit.")
        print('\n'.join(available_dirs))
        chosen_dir = input().strip().lower()
    return chosen_dir


def rename_files(chosen_dir, placeholder, day_num):
    os.chdir(chosen_dir)
    file_names = os.listdir('.')
    for file_name in file_names:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        renamed_lines = list(map(lambda line: line.replace(placeholder, day_num), lines))
        new_file_name = file_name.replace(placeholder, day_num)
        os.rename(file_name, new_file_name)
        with open(new_file_name, 'w') as file:
            file.writelines(renamed_lines)
    os.chdir('..')


if __name__ == '__main__':
    main(PLACEHOLDER)

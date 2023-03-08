
def write(files=['sorted/1.txt', 'sorted/2.txt', 'sorted/3.txt'], write_file='sorted/all.txt'):
    unsorted = {}
    for filename in files:
        with open(filename) as file:
            lines = file.readlines()
            unsorted[filename] = {'count': len(lines), 'lines': lines}

    def sorted_by_count(filename):
        return unsorted[filename]['count']
    sorted_files = sorted(unsorted, key=sorted_by_count)

    with open(write_file, 'w') as file:
        for sorted_file in sorted_files:
            file_data = unsorted[sorted_file]
            file.writelines([
                f"{sorted_file}\n",
                f"{file_data['count']}\n"
            ])
            last_line = file_data['lines'].pop()
            file.writelines(file_data['lines'])
            file.write(last_line.strip("\n") + "\n")


write()

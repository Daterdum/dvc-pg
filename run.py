import json

from dvc import api as dvc_api


def main():
    params = dvc_api.params_show()
    print(params)

    # DVCFileSystem https://dvc.org/doc/api-reference/dvcfilesystem
    ls_path = './data/params_dir'
    fs = dvc_api.DVCFileSystem(".")
    print(fs.ls(ls_path))

    # Opening stored file
    print("Reading remote files")
    with fs.open('./data/tracked_file.txt') as f:
        print(f.read())

    text = fs.read_text("./data/tracked_file.txt", encoding="utf-8")
    print(text)

    contents = fs.read_bytes("./data/tracked_file.txt")
    print(contents)

    print(fs.find("/", detail=False, dvc_only=True))  # dvc_only=False shows all files

    # Downloading/getting file
    fs.get_file("./data/tracked_file.txt", "tracked_file.txt")
    # And dir
    fs.get("./data", "./data", recursive=True)

    # Experiments
    print(json.dumps(dvc_api.exp_show()))





if __name__ == '__main__':
    main()

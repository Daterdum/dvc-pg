from dvc import api as dvc_api


def main():
    params = dvc_api.params_show()
    print(params)
    print(dvc_api.artifacts_show('data/artifact.txt.dvc'))



if __name__ == '__main__':
    print("Start")
    main()
    # dvc_api.artifacts.artifacts_show(name="example_artifact_id_name")

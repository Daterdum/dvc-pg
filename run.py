from dvc import api as dvc_api

if __name__ == '__main__':
    print("Doing something")
    params = dvc_api.params_show()
    dvc_api.artifacts.artifacts_show(name="example_artifact_id_name")
    print(f"params: {params}")

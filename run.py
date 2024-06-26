from dvc import api as dvc_api

if __name__ == '__main__':
    print("Doing something")
    params = dvc_api.params_show()
    print(f"params: {params}")

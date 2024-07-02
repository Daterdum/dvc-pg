import random
from pathlib import Path

from dvclive import Live
from PIL import Image


def dvc_live_example():
    EPOCHS = 2

    with Live(report="html", dvcyaml='./dvc.yaml') as live:
        live.log_param("epochs", EPOCHS)

        for i in range(EPOCHS):
            live.log_metric("metric", i + random.random())
            live.log_metric("nested/metric", i + random.random())
            live.log_image(f"img/{live.step}.png", Image.new("RGB", (50, 50), (i, i, i)))
            Path("model.pt").write_text(str(random.random()))
            live.next_step()

        live.log_artifact("model.pt", type="model", name="mymodel")
        live.log_sklearn_plot("confusion_matrix", [0, 0, 1, 1], [0, 1, 0, 1])
        live.log_metric("summary_metric", 1.0, plot=False)


if __name__ == "__main__":
    dvc_live_example()

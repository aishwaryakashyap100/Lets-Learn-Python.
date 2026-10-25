import multiprocessing
import requests
import os

def downloadFile(url, name):
    print(f"Started Downloading {name}")

    response = requests.get(url)
    os.makedirs("files", exist_ok=True)

    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)

    print(f"Finished Downloading {name}")


if __name__ == "__main__":

    url = "https://picsum.photos/200/300"
    pros = []

    for i in range(5):
        p = multiprocessing.Process(
            target=downloadFile,
            args=(url, i)
        )
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

    print("All files downloaded successfully!")
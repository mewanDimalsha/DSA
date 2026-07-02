from threading import Thread
from downloader import download_images
from multiprocessing import Process


class MyThread(Process):
    def __init__(self, count, name, urls, results):
        super(MyThread, self).__init__()
        self.name = name
        self.count = count
        self.urls = urls
        self.results = results

    def run(self):
        print(f"Starting {self.name}")

        for i, url in enumerate(self.urls):
            download_images(url, f"{self.name}_{i}")
        print(f"Exiting {self.name}")

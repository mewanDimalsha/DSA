# https://picsum.photos/id/1/200/300

import utils.clients
import utils.http_session
import utils.transport
import utils.session
import time
from my_tread import MyThread
from multiprocessing import Queue


def get_image_url(count) -> str:
    for i in range(0, count):
        url = f"https://picsum.photos/id/{i}/200/300"
        yield url


if __name__ == "__main__":
    start = time.time()
    urls = list(get_image_url(100))
    print(urls)
    url_list = []
    number_of_threads = 10

    for i in range(0, len(urls), number_of_threads):
        l = urls[i : i + number_of_threads]
        # print(l)
        url_list.append(l)
    # print(url_list)

    threads = []
    results = Queue()

    for i in range(number_of_threads):
        thread = MyThread(i, f"Thread-{i}", url_list[i], results)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()

    # for i, url in enumerate(urls):
    #     download_images(url, i)

    total = 0

    while not results.empty():
        print(results.get())
        total += results.get()

    print(f"Total downloaded images: {total}")
    diff = time.time() - start
    print(f"Downloaded 100 images in {diff} seconds")
